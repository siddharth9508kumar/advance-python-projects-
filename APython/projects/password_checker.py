# PASSWARD STRENGTH CHAEker

def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    elif not any(char.isdigit() for char in password):
        return "Weak: Password must contain at least one digit."
    elif not any(char.isupper() for char in password):
        return "Weak: Pas




