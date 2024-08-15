def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    
    # Traverse through each character in the text
    for char in text:
        # Encrypt uppercase characters
        if char.isupper():
            encrypted_text += chr((ord(char) -65 + shift) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
        # Non-alphabetic characters remain the same
        else:
            encrypted_text += char
    
    return (encrypted_text)

def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    
    # Traverse through each character in the text
    for char in text:
        # Decrypt uppercase characters
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        # Decrypt lowercase characters
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        # Non-alphabetic characters remain the same
        else:
            decrypted_text += char
    
    return decrypted_text

def main():
    print("Caesar Cipher Program")
    
    # Get user input for encryption or decryption
    choice = input("Would you like to (E)ncrypt or (D)ecrypt? ").upper()
    
    # Get the message from the user
    message = input("Enter your message: ")
    
    # Get the shift value from the user
    shift = int(input("Enter the shift value: "))
    
    if choice == 'E':
        encrypted_message = caesar_cipher_encrypt(message, shift)
        print("Encrypted Message: " + encrypted_message)
    elif choice == 'D':
        decrypted_message = caesar_cipher_decrypt(message, shift)
        print(f"Decrypted Message: {decrypted_message}")
    else:
        print("Invalid choice. Please enter 'E' for encryption or 'D' for decryption.")

if __name__ == "__main__":
    main()
