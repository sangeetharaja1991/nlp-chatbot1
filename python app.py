from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load NLP model
chatbot = pipeline("text-generation", model="facebook/blenderbot-400M-distill")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")  # Get user input from Landbot
    response = chatbot(user_message, max_length=50)[0]["generated_text"]
    return jsonify({"reply": response})  # Send chatbot response back

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
