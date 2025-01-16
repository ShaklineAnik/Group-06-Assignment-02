def encrypt_text(n, m):
    def shift_char(char, n, m):
        # Shift logic for lowercase letters (a-m and n-z)
        if "a" <= char <= "m":
            return chr(((ord(char) - ord("a") + (n * m)) % 13) + ord("a"))
        elif "n" <= char <= "z":
            return chr(((ord(char) - ord("n") - (n + m)) % 13) + ord("n"))
        # Shift logic for uppercase letters (A-M and N-Z)
        elif "A" <= char <= "M":
            return chr(((ord(char) - ord("A") - n) % 13) + ord("A"))
        elif "N" <= char <= "Z":
            return chr(((ord(char) - ord("N") + (m**2)) % 13) + ord("N"))
        else:
            return char

    try:
        with open("raw_text.txt", "r") as file:
            raw_text = file.read()

        # Encrypt the text using the shift logic
        encrypted_text = "".join(shift_char(char, n, m) for char in raw_text)

        # Save the encrypted text to a file
        with open("encrypted_text.txt", "w") as file:
            file.write(encrypted_text)
            print("Encrypted Text:", encrypted_text)

        print("\nEncryption complete. Encrypted text saved to 'encrypted_text.txt'.")
        return encrypted_text
    except FileNotFoundError:
        print("File 'raw_text.txt' not found.")


def decrypt_text(n, m):
    def reverse_shift_char(char, n, m):
        # Reverse shift logic for lowercase letters (a-m and n-z)
        if "a" <= char <= "m":
            return chr(((ord(char) - ord("a") - (n * m)) % 13) + ord("a"))
        elif "n" <= char <= "z":
            return chr(((ord(char) - ord("n") + (n + m)) % 13) + ord("n"))
        # Reverse shift logic for uppercase letters (A-M and N-Z)
        elif "A" <= char <= "M":
            return chr(((ord(char) - ord("A") + n) % 13) + ord("A"))
        elif "N" <= char <= "Z":
            return chr(((ord(char) - ord("N") - (m**2)) % 13) + ord("N"))
        else:
            return char

    try:
        with open("encrypted_text.txt", "r") as file:
            encrypted_text = file.read()

        # Decrypt the text using the reverse shift logic
        decrypted_text = "".join(
            reverse_shift_char(char, n, m) for char in encrypted_text
        )

        # Save the decrypted text to a file
        with open("decrypted_text.txt", "w") as file:
            file.write(decrypted_text)
            print("\nDecrypted Text:", decrypted_text)

        print("\nDecryption complete. Decrypted text saved to 'decrypted_text.txt'.")
        return decrypted_text
    except FileNotFoundError:
        print("File 'encrypted_text.txt' not found.")
        return ""


def verify_decryption(raw_text, decrypted_text):
    if raw_text == decrypted_text:
        print(
            "\nDecryption successfully verified: The original and decrypted texts match."
        )
    else:
        print("\nDecryption failed: The original and decrypted texts do not match.")


# Example usage
if __name__ == "__main__":
    # Get the keys (n and m) from the user
    n = int(input("Enter the value for n: "))
    m = int(input("Enter the value for m: "))

    # Encrypt the text
    encrypted_text = encrypt_text(n, m)

    try:
        # Read the raw text from file for verification
        with open("raw_text.txt", "r") as file:
            original_text = file.read()

        # Decrypt the text
        decrypted = decrypt_text(n, m)

        # Verify the decryption
        verify_decryption(original_text, decrypted)

    except FileNotFoundError:
        print("File 'raw_text.txt' not found. Cannot verify decryption.")
