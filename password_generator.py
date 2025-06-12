import random
import string

def generate_password(length=12):
    if length < 4:
        print("Password length should be at least 4 characters.")
        return None

    # Mix of all character types
    all_chars = string.ascii_letters + string.digits + string.punctuation

    # Ensure at least one from each category
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Fill the rest randomly
    password += random.choices(all_chars, k=length - 4)

    # Shuffle the result
    random.shuffle(password)
    return ''.join(password)

def main():
    print("Password Generator")
    try:
        length = int(input("Enter desired password length (min 4): "))
    except ValueError:
        print("Please enter a valid number.")
        return

    password = generate_password(length)
    if password:
        print(f"Generated Password: {password}")


if __name__ == "__main__":
    1
    main()