import time

def analyze_password(password):
    print(f"🔑 Analyzing password: {password}")

    complexity = len(password) * 2
    common_passwords = ["123456", "password", "qwerty", "admin"]

    if password in common_passwords:
        print("🚨 Weak! This is a common password.")
        return

    # Predict cracking time
    cracking_time = 2**complexity / 1e9  # in seconds
    if cracking_time < 1:
        print("⚠️ Very weak! Can be cracked instantly.")
    elif cracking_time < 3600:
        print(f"⚠️ Weak! Can be cracked in {int(cracking_time)} seconds.")
    else:
        print(f"✅ Strong! Estimated cracking time: {int(cracking_time/3600)} hours.")

    print("✅ Password analysis complete!")
