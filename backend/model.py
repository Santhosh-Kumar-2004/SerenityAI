# model.py
import requests

GROQ_API_KEY = "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"
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "llama3-8b-8192"

HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

def detect_mood(text: str) -> str:
    text = text.lower()
    if any(word in text for word in ["sad", "depressed", "hopeless", "cry", "lonely"]):
        return "😢"
    elif any(word in text for word in ["angry", "mad", "furious", "annoyed", "frustrated"]):
        return "😡"
    elif any(word in text for word in ["anxious", "nervous", "worried", "panic", "afraid", "can't sleep"]):
        return "😰"
    elif any(word in text for word in ["happy", "grateful", "joy", "excited", "calm"]):
        return "😊"
    elif any(word in text for word in ["tired", "exhausted", "sleepy", "drained"]):
        return "🥱"
    return "😐"

#common chat with AI
def get_ai_response(user_message: str) -> tuple[str, str]:
    system_prompt = (
        "You are SerenityAI, a kind, emotionally intelligent AI therapist. "
        "Your job is to provide comfort, validation, and thoughtful guidance to users dealing with emotional distress, anxiety, sadness, or loneliness. "
        "Always respond gently, calmly, and empathetically. Your tone should make the user feel heard and supported. "
        "If appropriate, you may suggest a short breathing exercise or a calming affirmation."
    )

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        "temperature": 0.7,
        "max_tokens": 60
    }

    try:
        response = requests.post(GROQ_API_URL, headers=HEADERS, json=payload, timeout=15)
        response.raise_for_status()
        reply = response.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print("Groq API error:", e)
        reply = "I'm here to support you, but something went wrong behind the scenes."

    mood = detect_mood(user_message)
    return reply, mood

# Affirmation response
def get_affirmation_response() -> str:
    system_prompt = (
        "You are SerenityAI, an AI mental wellness coach. "
        "Your job is to provide short, positive, emotionally supportive affirmations. "
        "Each response must be a single, original affirmation (not a breathing exercise or instruction). "
        "Affirmations should help the user feel valued, strong, and calm. "
        "Do not repeat previous affirmations or suggest exercises. Only return an affirmative message."
    )

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": "Give me one positive affirmation."}
        ],
        "temperature": 0.6,
        "max_tokens": 40 
    }

    try:
        response = requests.post(GROQ_API_URL, headers=HEADERS, json=payload, timeout=15)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print("Groq API error (affirmation):", e)
        return "You are enough, just as you are. Every day you grow stronger and more resilient."

# Motivation response
def get_motivation_response() -> str:
    system_prompt = (
        "You are SerenityAI, a motivational coach and mentor. "
        "Give a short, powerful motivational message to help the user feel empowered, confident, and ready to take action. "
        "Use an uplifting tone and avoid repeating quotes. Be original and energetic."
    )

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": "Motivate me with one powerful quote or message."}
        ],
        "temperature": 0.8,
        "max_tokens": 50
    }

    try:
        response = requests.post(GROQ_API_URL, headers=HEADERS, json=payload, timeout=15)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print("Groq API error (motivation):", e)
        return "You’ve got what it takes. Believe in your strength — and take the next step!"

# Wellness tip response
def get_wellness_tip() -> str:
    system_prompt = (
        "You are SerenityAI, a mental wellness guide. "
        "Give one short, practical mental health tip that the user can easily try. "
        "Keep it simple, calming, and focused on mindfulness, healthy habits, or emotional care."
    )

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": "Give me one wellness tip to help with mental health."}
        ],
        "temperature": 0.6,
        "max_tokens": 30
    }

    try:
        response = requests.post(GROQ_API_URL, headers=HEADERS, json=payload, timeout=15)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print("Groq API error (tip):", e)
        return "Take a 5-minute break, step outside, and breathe deeply. Your mind will thank you."
