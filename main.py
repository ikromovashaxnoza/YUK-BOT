from flask import Flask, render_template, request
import requests

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = "7826238507:AAFD3PBEBL8iUiFqkPGKg5-WpPwumlr3DBA"  # Bot token
CHAT_ID = "-1002675867438"  # Telegram kanal ID

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    role = request.form.get("role")
    phone = request.form.get("phone")
    cargo_type = request.form.get("cargo-type")
    cargo_weight = request.form.get("cargo-weight")
    cargo_name = request.form.get("cargo-name")
    price = request.form.get("price")
    location = request.form.get("location")
    comments = request.form.get("comments")
    
    message = f"""
    📦 **Yangi yuk e'loni!**
    👤 Rol: {role}
    📞 Telefon: {phone}
    📦 Yuk turi: {cargo_type}
    ⚖ Yuk hajmi: {cargo_weight} tonna
    📌 Manzil: {location}
    💰 Narx: {price}
    📝 Izoh: {comments}
    """
    
    if send_telegram_message(message):
        return "Ma'lumot muvaffaqiyatli yuborildi!", 200
    else:
        return "Xatolik yuz berdi, qayta urinib ko'ring!", 500

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
    
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        print(f"Telegram xatosi: {e}")
        return False

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
