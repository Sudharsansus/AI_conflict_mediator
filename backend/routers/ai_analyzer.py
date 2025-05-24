# backend/routers/ai_analyzer.py

def analyze_text(message: str):
    # Placeholder logic – replace with OpenAI or custom model logic later
    sentiment = "neutral"
    conflict_score = 0.3
    emotion = "calm"

    return {
        "message": message,
        "sentiment": sentiment,
        "conflict_score": conflict_score,
        "emotion": emotion
    }
