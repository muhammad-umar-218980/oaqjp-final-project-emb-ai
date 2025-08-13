from EmotionDetection.emotion_detector import emotion_detector

# Test cases
tests = [
    ("I am glad this happened", "joy"),
    ("I am really mad about this", "anger"),
    ("I feel disgusted just hearing about this", "disgust"),
    ("I am so sad about this", "sadness"),
    ("I am really afraid that this will happen", "fear"),
]

# Run tests
for statement, expected in tests:
    result = emotion_detector(statement)
    dominant = result['dominant_emotion']
    print(f"Statement: {statement}")
    print(f"Expected: {expected}, Detected: {dominant}")
    print("PASS" if dominant == expected else "FAIL")
    print("-" * 40)
