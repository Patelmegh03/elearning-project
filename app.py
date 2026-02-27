from flask import Flask, render_template, request
import random
import string
import hashlib
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

app = Flask(__name__)

# ================= PASSWORD SUGGESTION =================
def generate_suggestion():
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(14))

# ================= PASSWORD STRENGTH =================
def check_password_strength(password):
    checks = [
        len(password) >= 8,
        any(c.isupper() for c in password),
        any(c.islower() for c in password),
        any(c.isdigit() for c in password),
        any(c in "!@#$%^&*(),.?\":{}|<>" for c in password)
    ]
    score = sum(checks)
    percentage = int((score / 5) * 100)

    if percentage == 100:
        level = "Strong"
    elif percentage >= 60:
        level = "Medium"
    else:
        level = "Weak"

    return level, percentage

# ================= HASHING =================
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ================= CAESAR =================
def caesar_encrypt(text, shift=3):
    result = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift=3):
    return caesar_encrypt(text, -shift)

# ================= RSA =================
def rsa_encrypt(message):
    key = RSA.generate(1024)
    public_key = key.publickey()
    cipher = PKCS1_OAEP.new(public_key)
    encrypted = cipher.encrypt(message.encode())
    return base64.b64encode(encrypted).decode()

# ================= FIREWALL =================
def firewall_check(password):
    if len(password) < 6:
        return "Blocked: Password Too Short"
    elif password.lower() == "password":
        return "Blocked: Common Password Detected"
    else:
        return "Access Allowed"

# ================= BRUTE FORCE ESTIMATION =================
def brute_force_time(password):
    return f"Estimated brute force time: {len(password)*3} seconds (demo)"

# ================= MAIN =================
@app.route("/", methods=["GET", "POST"])
def index():
    result = {}

    if request.method == "POST":
        password = request.form.get("password")

        if password:
            strength, percent = check_password_strength(password)
            result = {
                "strength": strength,
                "percent": percent,
                "hash": hash_password(password),
                "caesar_enc": caesar_encrypt(password),
                "caesar_dec": caesar_decrypt(caesar_encrypt(password)),
                "rsa": rsa_encrypt(password),
                "firewall": firewall_check(password),
                "brute": brute_force_time(password),
                "suggestion": None if strength == "Strong" else generate_suggestion()
            }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)