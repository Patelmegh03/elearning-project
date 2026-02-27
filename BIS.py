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

# Password Suggestion
def generate_suggestion():
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(14))

# Password Strength Check (Entropy Included)
def check_password_strength(password):
    score = 0
    length = len(password)

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*(),.?\":{}|<>" for c in password)

    if length >= 8: score += 1
    if has_upper: score += 1
    if has_lower: score += 1
    if has_digit: score += 1
    if has_special: score += 1

    common_passwords = ["123456", "password", "admin", "qwerty", "abc123", "111111"]
    if password.lower() in common_passwords:
        return "Weak", 10

    if re.search(r"(.)\1{2,}", password):
        score -= 1

    charset = 0
    if has_lower: charset += 26
    if has_upper: charset += 26
    if has_digit: charset += 10
    if has_special: charset += 32

    entropy = length * math.log2(charset) if charset > 0 else 0

    if entropy > 40: score += 1
    if entropy > 60: score += 1

    score = max(score, 0)
    percentage = int((score / 7) * 100)

    if percentage >= 80:
        level = "Strong"
    elif percentage >= 50:
        level = "Medium"
    else:
        level = "Weak"

    return level, percentage

# Hashing
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Caesar Cipher
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

# RSA Encryption
def rsa_encrypt(message):
    key = RSA.generate(1024)
    public_key = key.publickey()
    cipher = PKCS1_OAEP.new(public_key)
    encrypted = cipher.encrypt(message.encode())
    return base64.b64encode(encrypted).decode()

# Main Route
@app.route("/", methods=["GET", "POST"])
def index():
    result = {}

    if request.method == "POST":
        password = request.form.get("password")

        if password:
            strength, percent = check_password_strength(password)
            encrypted_caesar = caesar_encrypt(password)

            result = {
                "strength": strength,
                "percent": percent,
                "hash": hash_password(password),
                "caesar_enc": encrypted_caesar,
                "caesar_dec": caesar_decrypt(encrypted_caesar),
                "rsa": rsa_encrypt(password),
                "suggestion": None if strength == "Strong" else generate_suggestion()
            }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)