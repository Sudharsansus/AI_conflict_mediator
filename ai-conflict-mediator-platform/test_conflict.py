from backend.ai.conflict_detector import detect_conflict

message = "I am absolutely furious about the way you treated me!"
conflict_score, sentiment, emotion = detect_conflict(message)
print(conflict_score, sentiment, emotion)
