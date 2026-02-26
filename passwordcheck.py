import re

def assess_password(password):
    # Assessment Criteria
    criteria = {
        "Length (8+ chars)": len(password) >= 8,
        "Uppercase Letter": bool(re.search(r'[A-Z]', password)),
        "Lowercase Letter": bool(re.search(r'[a-z]', password)),
        "Numeric Digit": bool(re.search(r'[0-9]', password)),
        "Special Character": bool(re.search(r'[^A-Za-z0-9]', password))
    }
    
    # Calculate score
    score = sum(criteria.values())
    
    # Define Strength Levels
    if score <= 2:
        strength = "Weak "
    elif score <= 4:
        strength = "Moderate "
    else:
        strength = "Strong "
        
    return score, strength, criteria

# User Interface
print("--- Password Strength Checker ---")
user_pwd = input("Enter a password to test: ")
score, rating, results = assess_password(user_pwd)

print(f"\nOverall Strength: {rating}")
print(f"Score: {score}/5")
print("-" * 30)

for criterion, passed in results.items():
    status = "✔" if passed else "✖"
    print(f"[{status}] {criterion}")

if score < 5:
    print("\nTip: Add more variety (numbers, symbols, or length) to improve security.")
