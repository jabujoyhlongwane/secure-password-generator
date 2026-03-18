# generator.py
import secrets
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_numbers=True, use_symbols=True):
    """
    Generates a cryptographically secure random password.

    Args:
        length (int): The desired length of the password.
        use_uppercase (bool): Include uppercase letters?
        use_lowercase (bool): Include lowercase letters?
        use_numbers (bool): Include numbers?
        use_symbols (bool): Include symbols?

    Returns:
        str: The generated password, or an error message if no character sets are selected.
    """
    # Create a pool of characters based on user selection
    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    # Check if at least one character set was selected
    if not characters:
        return "Error: Select at least one character type."

    # Use the 'secrets' module for cryptographically strong randomness
    # This is important for security-sensitive applications like passwords.
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

# Example of how to use it (you can test this later)
# if __name__ == "__main__":
#     new_pass = generate_password(length=16)
#     print(f"Generated Password: {new_pass}")