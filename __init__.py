from flask import Flask,render_template, request, jsonify
import openai


app = Flask(__name__) #creating flask app name



# Configuration de l'API OpenAI
openai.api_key = None
openai.api_base = "https://api.openai.com/v1"



# Route pour l'interaction avec le chatbot
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['user_message']
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_message,
        temperature=0.7,
        max_tokens=150
    )
    bot_reply = response.choices[0].text.strip()
    return jsonify({'bot_reply': bot_reply})


@app.route('/') #comm4
def home():
    return render_template("resume_2.html")

@app.route('/resume_1')
def resume_1():
    return render_template("resume_1.html")

@app.route('/resume_2')
def resume_2():
    return render_template("resume_2.html")

@app.route('/resume_template')
def resume_template():
    return render_template("resume_template.html")

if(__name__ == "__main__"):
    app.run(debug=True)
