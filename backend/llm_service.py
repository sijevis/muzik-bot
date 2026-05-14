import os
import json
import logging
import time
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """Sen DJ AI'sin — yapay zeka destekli, Türkçe konuşan,.samimi ve doğal bir müzik asistanı.

KİMLİK:
- Samimi, doğal, arkadaşça konuşursun. Robot gibi davranmazsın.
- Kullanıcıyla gerçek bir sohbet ediyorsun — hazır cevaplar fırlatmazsın.
- Türkçe konuşursun.
- Gereksiz uzun cevap vermezsin; doğal ve akıcı olursun.

ANA GÖREVLER:
- Kullanıcıyla sohbet etmek
- Ruh halini ve müzik zevkini anlamak
- İstenirse müzik önermek veya playlist oluşturmak
- Geçmiş tercihleri hatırlamak ve kullanmak

SOHBET KURALLARI:
- Her mesajı müzik isteği olarak yorumlama. Kullanıcı sadece sohbet edebilir.
- Önce anlamaya çalış, hemen öneri fırlatma.
- Yeterli bilgi yoksa kısa doğal sorular sor: "Daha sakin mi olsun?", "Türkçe mi yabancı mı?", "Benzer sanatçı ister misin?"
- Bağlamı takip et — bir önceki mesajdaki ruh halini, türü, aktiviteyi hatırla.

ÖNERİ KURALLARI:
- "bir şey öner" → 1-3 öneri
- "playlist yap", "liste yap", "karışık liste" → playlist moduna geç
- "rock öner" → birkaç rock önerisi
- Tek şarkı isteniyorsa tek öner

ŞARKI VERİSİ KURALI (ÇOK ÖNEMLİ):
- Şarkı isimlerini ASLA uydurma.
- Sanatçı isimlerini ASLA uydurma.
- Albüm isimlerini ASLA uydurma.
- Sadece sistem tarafından sağlanan gerçek müzik verisini kullan.
- Eğer veri yoksa şöyle de: "Nasıl bir şey arıyorsun? Tür, ruh hali ya da sanatçı söylersen ona göre bakabilirim."

RUH HALİ ANALİZİ:
Kullanıcının mesajından şu ruh hallerini anlamaya çalış:
- üzgün, mutlu, enerjik, stresli, sakin, öfkeli, romantik, nostaljik, odaklı, uykulu, motivasyonsuz

AKTİVİTE ANALİZİ:
- spor, ders çalışma, araba sürme, gece yolculuğu, parti, dinlenme, çalışma, uyku öncesi, yürüyüş, gaming

TON:
- Sıcak, doğal, samimi, yardımcı, akıcı, modern
- KAÇIN: robot gibi konuşma, gereksiz formal olma, her mesajı müzik isteği sanma, uzun monologlar, olmayan şarkılar üretme, emoji spam

ÖRNEK İYİ DAVRANIŞ:
Kullanıcı: "Bugün biraz kötüyüm"
Sen: "Off, öyle günler gerçekten yorucu olabiliyor. Daha sakin bir şeyler mi iyi gelir yoksa enerjini toparlayacak bir şey mi ararsın?"

ÖRNEK KÖTÜ DAVRANIŞ:
Kullanıcı: "Bugün biraz kötüyüm"
Sen: \"İşte sana 10 şarkı.\""""


class LLMService(ABC):
    @abstractmethod
    def generate_response(self, conversation_history, analysis_context):
        pass

    @abstractmethod
    def is_available(self):
        pass

    @abstractmethod
    def get_status(self):
        pass


class OpenAIService(LLMService):
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY", "")
        self.model = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
        self.base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
        self._client = None
        self._available = False
        self._retry_after = 0
        if self.api_key:
            try:
                from openai import OpenAI
                self._client = OpenAI(api_key=self.api_key, base_url=self.base_url)
                self._available = True
                logger.info("OpenAI servisi başlatıldı")
            except Exception as e:
                logger.warning(f"OpenAI başlatma hatası: {e}")

    def generate_response(self, conversation_history, analysis_context=None):
        if not self.is_available():
            return None
        try:
            messages = [{"role": "system", "content": SYSTEM_PROMPT}]
            if analysis_context and analysis_context.get("summary"):
                messages.append({
                    "role": "system",
                    "content": f"Kullanıcı hakkında bilinenler: {analysis_context['summary']}"
                })
            for msg in conversation_history[-10:]:
                messages.append({
                    "role": msg.get("role", "user"),
                    "content": msg.get("content", "")
                })
            if analysis_context:
                context_msg = self._build_context_message(analysis_context)
                if context_msg:
                    messages.append({"role": "user", "content": context_msg})

            response = self._client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=500,
                temperature=0.8,
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            logger.warning(f"OpenAI yanıt hatası: {e}")
            self._retry_after = time.time() + 60
            return None

    def generate_response_stream(self, conversation_history, analysis_context=None):
        if not self.is_available():
            return None
        try:
            messages = [{"role": "system", "content": SYSTEM_PROMPT}]
            if analysis_context and analysis_context.get("summary"):
                messages.append({
                    "role": "system",
                    "content": f"Kullanıcı hakkında bilinenler: {analysis_context['summary']}"
                })
            for msg in conversation_history[-10:]:
                messages.append({
                    "role": msg.get("role", "user"),
                    "content": msg.get("content", "")
                })
            if analysis_context:
                context_msg = self._build_context_message(analysis_context)
                if context_msg:
                    messages.append({"role": "user", "content": context_msg})

            stream = self._client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=500,
                temperature=0.8,
                stream=True,
            )
            def token_generator():
                for chunk in stream:
                    if chunk.choices and chunk.choices[0].delta and chunk.choices[0].delta.content:
                        yield chunk.choices[0].delta.content
            return token_generator()
        except Exception as e:
            logger.warning(f"OpenAI stream hatası: {e}")
            self._retry_after = time.time() + 60
            return None

    def _build_context_message(self, context):
        parts = []
        if context.get("genre"):
            parts.append(f"Tür: {context['genre']}")
        if context.get("mood"):
            parts.append(f"Ruh hali: {context['mood']}")
        if context.get("activity"):
            parts.append(f"Aktivite: {context['activity']}")
        if context.get("artist"):
            parts.append(f"Sanatçı: {context['artist']}")
        if parts:
            return f"Kullanıcı şu özelliklerde müzik arıyor: {', '.join(parts)}"
        return None

    def is_available(self):
        if self._retry_after and time.time() < self._retry_after:
            return False
        if self._retry_after and time.time() >= self._retry_after:
            self._retry_after = 0
        return self._available and self._client is not None

    def get_status(self):
        return {"available": self._available, "name": "OpenAI", "model": self.model}


class GeminiService(LLMService):
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY", "")
        self.model = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")
        self._client = None
        self._available = False
        self._retry_after = 0
        if self.api_key:
            try:
                from google import genai
                self._client = genai.Client(api_key=self.api_key)
                self._available = True
                logger.info("Gemini servisi başlatıldı (google-genai)")
            except ImportError:
                try:
                    import google.generativeai as genai
                    genai.configure(api_key=self.api_key)
                    self._client = genai.GenerativeModel(self.model)
                    self._available = True
                    logger.info("Gemini servisi başlatıldı (legacy google-generativeai)")
                except Exception as e:
                    logger.warning(f"Gemini başlatma hatası: {e}")
            except Exception as e:
                logger.warning(f"Gemini başlatma hatası: {e}")

    def generate_response(self, conversation_history, analysis_context=None):
        if not self.is_available():
            return None
        try:
            contents = []
            if analysis_context and analysis_context.get("summary"):
                contents.append({"role": "user", "parts": [{"text": f"[System]: {SYSTEM_PROMPT}"}]})
                contents.append({"role": "model", "parts": [{"text": "Anlaşıldı, DJ AI olarak doğal ve samimi bir şekilde yardımcı olacağım."}]})
                contents.append({"role": "user", "parts": [{"text": f"[System - Kullanıcı hakkında bilinenler]: {analysis_context['summary']}"}]})
            else:
                contents.append({"role": "user", "parts": [{"text": f"[System]: {SYSTEM_PROMPT}"}]})
                contents.append({"role": "model", "parts": [{"text": "Anlaşıldı, DJ AI olarak doğal ve samimi bir şekilde yardımcı olacağım."}]})

            for msg in conversation_history[-10:]:
                role = "user" if msg.get("role") == "user" else "model"
                contents.append({"role": role, "parts": [{"text": msg.get("content", "")}]})

            if analysis_context:
                context_msg = self._build_context_message(analysis_context)
                if context_msg:
                    contents.append({"role": "user", "parts": [{"text": context_msg}]})

            from google import genai as genai_mod
            if isinstance(self._client, genai_mod.Client):
                response = self._client.models.generate_content(
                    model=self.model,
                    contents=contents,
                )
                return response.text.strip()
            else:
                prompt = SYSTEM_PROMPT + "\n\n"
                if analysis_context and analysis_context.get("summary"):
                    prompt += f"Kullanıcı hakkında bilinenler: {analysis_context['summary']}\n\n"
                for msg in conversation_history[-10:]:
                    role = "Kullanıcı" if msg.get("role") == "user" else "Asistan"
                    prompt += f"{role}: {msg.get('content', '')}\n"
                if analysis_context:
                    context_msg = self._build_context_message(analysis_context)
                    if context_msg:
                        prompt += f"\nEk bilgi: {context_msg}\n"
                prompt += "\nAsistan:"
                response = self._client.generate_content(prompt)
                return response.text.strip()
        except Exception as e:
            logger.warning(f"Gemini yanıt hatası: {e}")
            self._retry_after = time.time() + 60
            return None

    def _build_context_message(self, context):
        parts = []
        if context.get("genre"):
            parts.append(f"Tür: {context['genre']}")
        if context.get("mood"):
            parts.append(f"Ruh hali: {context['mood']}")
        if context.get("activity"):
            parts.append(f"Aktivite: {context['activity']}")
        if context.get("artist"):
            parts.append(f"Sanatçı: {context['artist']}")
        if parts:
            return f"Kullanıcı şu özelliklerde müzik arıyor: {', '.join(parts)}"
        return None

    def is_available(self):
        if self._retry_after and time.time() < self._retry_after:
            return False
        if self._retry_after and time.time() >= self._retry_after:
            self._retry_after = 0
        return self._available and self._client is not None

    def get_status(self):
        return {"available": self._available, "name": "Gemini", "model": self.model}


class LocalLLMService(LLMService):
    def __init__(self):
        self.base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        self.model = os.getenv("OLLAMA_MODEL", "llama3")
        self._available = False
        self._check_availability()

    def _check_availability(self):
        try:
            import requests
            resp = requests.get(f"{self.base_url}/api/tags", timeout=5)
            if resp.status_code == 200:
                models = resp.json().get("models", [])
                if any(self.model in m.get("name", "") for m in models):
                    self._available = True
                    logger.info(f"Local LLM ({self.model}) bulundu")
        except Exception:
            self._available = False

    def generate_response(self, conversation_history, analysis_context=None):
        if not self.is_available():
            return None
        try:
            import requests
            messages = [{"role": "system", "content": SYSTEM_PROMPT}]
            if analysis_context and analysis_context.get("summary"):
                messages.append({
                    "role": "system",
                    "content": f"Kullanıcı hakkında bilinenler: {analysis_context['summary']}"
                })
            for msg in conversation_history[-10:]:
                messages.append({
                    "role": msg.get("role", "user"),
                    "content": msg.get("content", "")
                })
            payload = {
                "model": self.model,
                "messages": messages,
                "stream": False,
            }
            resp = requests.post(
                f"{self.base_url}/api/chat",
                json=payload,
                timeout=30,
            )
            if resp.status_code == 200:
                return resp.json().get("message", {}).get("content", "").strip()
        except Exception as e:
            logger.warning(f"Local LLM yanıt hatası: {e}")
        return None

    def is_available(self):
        return self._available

    def get_status(self):
        return {"available": self._available, "name": "LocalLLM", "model": self.model, "base_url": self.base_url}


class LLMClient:
    def __init__(self):
        self.services = []
        self.demo_mode = True

        openai_service = OpenAIService()
        if openai_service.is_available():
            self.services.append(openai_service)

        gemini_service = GeminiService()
        if gemini_service.is_available():
            self.services.append(gemini_service)

        local_service = LocalLLMService()
        if local_service.is_available():
            self.services.append(local_service)

        if self.services:
            self.demo_mode = False
            logger.info(f"LLM servisleri aktif: {[s.get_status()['name'] for s in self.services]}")
        else:
            logger.info("LLM servisi bulunamadı, demo mod aktif")

    def generate_response(self, conversation_history, analysis_context=None):
        for service in self.services:
            if service.is_available():
                response = service.generate_response(conversation_history, analysis_context)
                if response:
                    return response
        return None

    def generate_response_stream(self, conversation_history, analysis_context=None):
        for service in self.services:
            if service.is_available() and hasattr(service, 'generate_response_stream'):
                stream = service.generate_response_stream(conversation_history, analysis_context)
                if stream:
                    return stream
        return None

    def generate_fallback_stream(self, conversation_history, analysis_context=None):
        import json
        for service in self.services:
            if service.is_available():
                response = service.generate_response(conversation_history, analysis_context)
                if response:
                    yield f"data: {json.dumps({'type': 'token', 'content': response})}\n\n"
                    yield f"data: {json.dumps({'type': 'done'})}\n\n"
                    return

    def get_status(self):
        return {
            "demo_mode": self.demo_mode,
            "available_services": [s.get_status() for s in self.services],
            "total_services": len(self.services),
        }