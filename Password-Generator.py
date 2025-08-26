import random, string

def generate_password(length):
    if length < 4:
        return "Length must be >= 4"

    chars = string.ascii_letters + string.digits + string.punctuation

    # must-have characters
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # fill remaining
    password += [random.choice(chars) for _ in range(length - 4)]

    random.shuffle(password)
    return ''.join(password)

length = int(input("Enter password length: "))
print("Generated Password:", generate_password(length))
