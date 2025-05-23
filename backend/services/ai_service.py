from transformers import pipeline

# Load model once on startup
sentiment_analyzer = pipeline("sentiment-analysis")

def analyze_conflict_message(message: str) -> dict:
    result = sentiment_analyzer(message)[0]
    label = result["label"]
    score = round(result["score"], 4)
    
    # Simple suggestion based on sentiment
    suggestion = "Consider using calmer language." if label == "NEGATIVE" else "Message seems constructive."

    return {
        "sentiment": label,
        "confidence": score,
        "suggestion": suggestion
    }
