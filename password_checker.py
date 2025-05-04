import re
import getpass

def check_password_strength(password):
    """
    Check the strength of a password based on length and character variety.
    """
    score = 5
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    upper_error = re.search(r"[A-Z]", password) is None
    lower_error = re.search(r"[a-z]", password) is None
    special_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    if length_error:
        print("Password must be at least 8 characters long.")
        score-=1
    if digit_error:
        print("Password must contain at least one digit.")
        score-=1
    if upper_error:
        print("Password must contain at least one uppercase letter.")
        score-=1
    if lower_error:
        print("Password must contain at least one lowercase letter.")
        score-=1
    if special_error:
        print("Password must contain at least one special character.")
        score-=1
    
    if score == 5: strength = "Strong"
    elif score == 4: strength = "Good"
    elif score == 3: strength = "Moderate"
    elif score == 2: strength = "Weak"
    else: strength = "Extremely Weak"

    print(f"Password strength: {strength}")


#test
user_input = getpass.getpass("Enter a password: ")
check_password_strength(user_input)
# This script checks the strength of a password based on length and character variety.