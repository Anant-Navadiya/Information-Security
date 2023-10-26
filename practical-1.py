def caesar_cipher(text, shift, action="encrypt"):
    result = []

    for char in text:
        if char.isalpha():
            shift_amount = shift if action == "encrypt" else -shift
            char_code = ord(char) + shift_amount

            if char.isupper():
                char_code = (char_code - ord('A')) % 26 + ord('A')
            else:
                char_code = (char_code - ord('a')) % 26 + ord('a')

            result.append(chr(char_code))
        else:
            result.append(char)

    return ''.join(result)


text = input("Enter plain text: ")

shift = int(input("Enter Key: "))
encrypted_text = caesar_cipher(text, shift, action="encrypt")
print("Encrypted:", encrypted_text)

decrypted_text = caesar_cipher(encrypted_text, shift, action="decrypt")
print("Decrypted:", decrypted_text)
