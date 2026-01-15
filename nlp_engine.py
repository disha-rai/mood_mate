import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer 
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()
def preprocess_text(text):
    #1. Lowercase
    text = text.lower()

    #2. Remove punctuation and numbers
    text = re.sub(r'[^a-z\s]', '', text)

    #3. Tokenize
    tokens = word_tokenize(text)

    #4. Remove stopwords
    clean_tokens = [word for word in tokens if word not in stop_words]

    #5. lemmatize
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in clean_tokens]

    return lemmatized_tokens

emotion_keywords = {
    "Happy": ["happy", "excited", "joy", "smile", "cheerful"],
    "Sad": ["sad", "lonely", "cry", "down", "upset"],
    "Angry": ["angry", "mad", "furious", "irritated"],
    "Stress": ["stress", "stressed", "anxious", "nervous", "tired", "worried"]
} #rule-based keyword matching approach
def detect_emotion(tokens):
    emotion_scores = {emotion: 0 for emotion in emotion_keywords}

    for token in tokens:
        for emotion, keywords in emotion_keywords.items():
            if token in keywords:
                emotion_scores[emotion] += 1
    
    detected_emotion = max(emotion_scores, key=emotion_scores.get)

    if emotion_scores[detected_emotion] == 0:
        return "Neutral"
    

    return detected_emotion


def detect_intent (original_text):  #, tokens passing in future
    text = original_text.lower()

    #1. Question
    if "?" in original_text:
        return "Question"
    
    #2. Greeting
    greetings = ["hi", "hello", "good morning", "hey", "good evening", "whats up"]
    if any(word in text for word in greetings):
        return "Greeting"
    
    #3. self-expression
    self_expression_phrases = ["i feel", "i am", "i'm", "feeling"]
    if any(phrase in text for phrase in self_expression_phrases):
        return "self_expression"
    
    #4. default
    return "statement"


def generate_res(emotion, intent):
    responses = {
        "Happy" : {
            "Greeting": "Hey! You sound cheerful today 😊",
            "Self-Expression": "I love that energy 🌸 Keep it going!",
            "Question": "That’s a happy question 😄 How can I help?",
            "Statement": "Nice to hear something positive today!"
        }, 
        "Sad": {
            "Greeting": "Hi… I’m here if you want to talk 🌱",
            "Self-Expression": "That sounds really heavy. You’re not alone 💙",
            "Question": "I’ll try my best to help. Tell me more.",
            "Statement": "Some days are tough. Be gentle with yourself."
        }, 
        "Angry": {
            "Greeting": "Hey. You seem tense. Want to let it out?",
            "Self-Expression": "That frustration is valid. Take a breath 🧘",
            "Question": "Let’s slow this down and think clearly.",
            "Statement": "Strong emotions usually mean something matters."
        },
        "Stress": {
            "Greeting": "Hi. Take a deep breath 🌿",
            "Self-Expression": "That sounds stressful. One step at a time 💪",
            "Question": "Let’s break this problem down together.",
            "Statement": "You’re under pressure — and still showing up."
        },
        "Neutral": {
            "Greeting": "Hello! How can I help today?",
            "Self-Expression": "Thanks for sharing that.",
            "Question": "Good question! Let’s think about it.",
            "Statement": "Alright, noted."
        }
    }
    return responses.get(emotion, {}).get(intent, "I'm here to listen.")
