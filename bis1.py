from flask import Flask, render_template, request
import random
import string
import hashlib
import base64
import math
import re
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

app = Flask(__name__)

# ================= PASSWORD SUGGESTION =================
def generate_suggestion():
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(14))

# ================= IMPROVED PASSWORD STRENGTH =================
def check_password_strength(password):
    score = 0
    length = len(password)

    # ---- Basic Character Checks ----
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*(),.?\":{}|<>" for c in password)

    if length >= 8:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    # ---- Common Password Check ----
    common_passwords = [
        "123456", "password", "admin",
        "qwerty", "abc123", "111111"
    ]
    if password.lower() in common_passwords:
        return "Weak", 5

    # ---- Sequential Pattern Check ----
    sequences = ["12345", "abcdef", "qwerty", "00000"]
    for seq in sequences:
        if seq in password.lower():
            score -= 1

    # ---- Repeated Characters Check (aaa, 1111) ----
    if re.search(r"(.)\1{2,}", password):
        score -= 1

    # ---- Entropy Calculation ----
    charset = 0
    if has_lower: charset += 26
    if has_upper: charset += 26
    if has_digit: charset += 10
    if has_special: charset += 32

    if charset > 0:
        entropy = length * math.log2(charset)
    else:
        entropy = 0

    # Entropy Bonus
    if entropy > 40:
        score += 1
    if entropy > 60:
        score += 1

    # Normalize Score
    score = max(score, 0)
    max_score = 7
    percentage = int((score / max_score) * 100)

    # Final Level
    if percentage >= 80:
        level = "Strong"
    elif percentage >= 50:
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