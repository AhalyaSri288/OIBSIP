import random
import string

while True:
    print("\n--- Random Password Generator ---")

    # Get password length
    try:
        length = int(input("Enter password length (minimum 8): "))

        if length < 8:
            print("Error: Password length must be at least 8.")
            continue

    except ValueError:
        print("Error: Please enter a valid number.")
        continue

    # Choose character types
    print("\nChoose character types:")
    print("1. Uppercase letters")
    print("2. Lowercase letters")
    print("3. Numbers")
    print("4. Symbols")

    choices = input("Enter your choices (example: 1234): ")

    # Remove duplicate choices
    choices = set(choices)

    if len(choices) < 2:
        print("Error: Please select at least 2 character types.")
        continue

    characters = ""
    selected_characters = []

    if "1" in choices:
        characters += string.ascii_uppercase
        selected_characters.append(random.choice(string.ascii_uppercase))

    if "2" in choices:
        characters += string.ascii_lowercase
        selected_characters.append(random.choice(string.ascii_lowercase))

    if "3" in choices:
        characters += string.digits
        selected_characters.append(random.choice(string.digits))

    if "4" in choices:
        characters += string.punctuation
        selected_characters.append(random.choice(string.punctuation))

    # Generate remaining characters
    remaining_length = length - len(selected_characters)

    password = selected_characters + [
        random.choice(characters)
        for _ in range(remaining_length)
    ]

    # Shuffle password
    random.shuffle(password)

    password = "".join(password)

    print("\nGenerated Password:", password)

    # Ask whether to generate another password
    again = input("\nGenerate another password? (yes/no): ").lower()

    if again != "yes":
        print("Thank you for using the Password Generator!")
        break
