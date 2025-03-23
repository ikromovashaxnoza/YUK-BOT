from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = "7826238507:AAFD3PBEBL8iUiFqkPGKg5-WpPwumlr3DBA"  # Bot token
CHAT_ID = "-1002675867438"  # Telegram kanal ID

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    try:
        role = request.form.get("role")
        phone = request.form.get("phone")
        cargo_type = request.form.get("cargo-type")
        cargo_weight = request.form.get("cargo-weight")
        cargo_name = request.form.get("cargo-name")
        price = request.form.get("price")
        location = request.form.get("location")
        comments = request.form.get("comments")

        if not (role and phone and cargo_type and cargo_weight and price and location):
            return jsonify({"error": "Barcha maydonlarni to'ldiring!"}), 400

        message = (f"\U0001F4E6 **Yangi yuk e'loni!**\n\n"
                   f"👤 Rol: {role}\n"
                   f"📞 Telefon: {phone}\n"
                   f"📦 Yuk turi: {cargo_type}\n"
                   f"⚖ Yuk hajmi: {cargo_weight} tonna\n"
                   f"📌 Manzil: {location}\n"
                   f"💰 Narx: {price}\n"
                   f"📝 Izoh: {comments}")
        
        response = send_telegram_message(message)
        
        if response:
            return jsonify({"success": "Ma'lumot yuborildi!"}), 200
        else:
            return jsonify({"error": "Telegramga yuborishda xatolik!"}), 500
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def send_telegram_message(text):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        data = {"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
        response = requests.post(url, data=data)
        
        if response.status_code == 200:
            return True
        else:
            print("Telegram xatosi:", response.text)
            return False
    except requests.exceptions.RequestException as e:
        print("So‘rov xatosi:", e)
        return False

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
