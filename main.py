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

    message = f"📦 **Yangi yuk e'loni!**\n\n👤 Rol: {role}\n📞 Telefon: {phone}\n📦 Yuk turi: {cargo_type}\n⚖ Yuk hajmi: {cargo_weight} tonna\n📌 Manzil: {location}\n💰 Narx: {price}\n📝 Izoh: {comments}"

    send_telegram_message(message)
    return "Ma'lumot yuborildi!", 200

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
    requests.post(url, data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
