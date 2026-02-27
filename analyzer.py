import re
from entropy import calculate_entropy

def load_common_passwords():
    with open("wordlist.txt", "r") as file:
        return file.read().splitlines()

def analyze_password(password):
    score = 0
    feedback = []

    length = len(password)

    # Length scoring
    if length >= 12:
        score += 25
    elif length >= 8:
        score += 15
        feedback.append("Increase length to at least 12 characters.")
    else:
        feedback.append("Password too short.")

    # Character diversity
    if re.search(r"[a-z]", password):
        score += 10
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"[A-Z]", password):
        score += 10
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"[0-9]", password):
        score += 10
    else:
        feedback.append("Add numbers.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 15
    else:
        feedback.append("Add special characters.")

    # Dictionary check
    common_passwords = load_common_passwords()
    if password.lower() in common_passwords:
        score = 0
        feedback.append("This password is commonly breached!")

    # Pattern detection
    if re.search(r"(.)\1\1", password):
        score -= 10
        feedback.append("Avoid repeated characters.")

    if re.search(r"123|abc|202[0-9]", password.lower()):
        score -= 10
        feedback.append("Avoid predictable sequences.")

    entropy = calculate_entropy(password)

    # Strength classification
    if score >= 70:
        strength = "STRONG"
    elif score >= 40:
        strength = "MODERATE"
    else:
        strength = "WEAK"

    return score, strength, entropy, feedback