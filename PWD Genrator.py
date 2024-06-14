import string
import random

def generate_password(length):
    """Generate a random password of a specified length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_password_length():
    """Prompt the user to enter the desired password length."""
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length > 0:
                return length
            else:
                print("Length must be greater than zero. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    """Main function to generate and display a random password."""
    length = get_password_length()
    password = generate_password(length)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
