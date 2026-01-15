from flask import Flask, render_template, request
from nlp_engine import preprocess_text, detect_emotion, detect_intent, generate_res

app = Flask(__name__) #creates web app
@app.route("/", methods=["GET", "POST"])   #@app.route("/")→ Homepage URL
def home():
    user_text = ""
    processed_tokens = []
    emotions = ""
    intent = ""
    response = ""
    if request.method =="POST":
        user_text = request.form.get("user_input") #request.form.get("user_input")→ This is how real apps receive data
        processed_tokens = preprocess_text(user_text)
        emotions = detect_emotion(processed_tokens)
        intent = detect_intent(user_text) #, processed_tokens in future
        response = generate_res(emotions, intent)
    return render_template("index.html", text=user_text, tokens=processed_tokens, emotion=emotions, intent=intent, response=response)
if __name__ == "__main__":
    app.run(debug=True)



