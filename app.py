from flask import Flask,render_template,request,jsonify
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

faq_data = {
    "hello":"Hi,how can I help you today.",
    "what are symptoms of dengue": "Common symptoms include fever, headache, joint pain, and skin rash.",
    "what is covid": "COVID-19 is a viral infection caused by SARS-CoV-2. Symptoms include fever, cough, and difficulty breathing.",
    "vaccination schedule": "Children should receive BCG, DPT, Polio, Hepatitis B, and MMR as per ICMR guidelines.",
    "nearest hospital": "You can visit your district civil hospital or search via Aarogya Setu app.",
    "how to prevent malaria" : "Use mosquito nets, apply repellents, and keep your surroundings clean to avoid mosquito breeding.",
    "what is anemia": "Anemia is a condition in which you lack enough healthy red blood cells to carry oxygen to your body tissues.",
    "what is diabetes": "Diabetes is a chronic disease where the body cannot regulate blood sugar properly. Common symptoms include frequent urination, thirst, and fatigue.",
    "what is blood pressure": "Blood pressure is the force of blood pushing against artery walls. High BP can increase the risk of heart disease and stroke.",
    "what is first aid": "First aid is the immediate assistance given to someone with a minor or serious illness or injury before professional help arrives.",
    "what is balanced diet": "A balanced diet includes carbohydrates, proteins, fats, vitamins, and minerals in proper proportions for good health.",
    "what is dehydration": "Dehydration happens when your body loses more fluids than it takes in. Drink water and oral rehydration solutions to recover.",
    "what is tuberculosis": "Tuberculosis (TB) is a bacterial infection that affects the lungs. Symptoms include cough, fever, and weight loss.",
    "what is polio": "Polio is a viral disease that can cause paralysis. Vaccination is the best prevention.",
    "what is hepatitis b": "Hepatitis B is a liver infection caused by HBV. It spreads through blood and body fluids. Vaccination is available."
}

def chatbot_response(user_input, lang="en"):
    user_input = user_input.lower()

    if lang != "en":
        user_input = translator.translate(user_input, src=lang, dest="en").text.lower()

    for key, value in faq_data.items():
        if key in user_input:
            response = value
            break
    else:
        response = "I'm sorry, I don’t have info on that. Please consult a nearby health center."

    if lang != "en":
        response = translator.translate(response, src="en", dest=lang).text

    return response

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_input = request.json["message"]
    lang = request.json.get("lang", "en")
    return jsonify({"response": chatbot_response(user_input, lang)})

if __name__ == "__main__":
    app.run(debug=True)
