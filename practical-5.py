def cipher(text, key, action="encrypt"):
    text = text.upper()
    key = key.upper()
    result = []
    key_length = len(key)
    key_index = 0

    for char in text:
        if char.isalpha():
            if action == "encrypt":
                shift = (ord(char) + ord(key[key_index]) - 2 * ord('A')) % 26
                encrypted_char = chr(shift + ord('A'))
            elif action == "decrypt":
                shift = (ord(char) - ord(key[key_index]) + 26) % 26
                encrypted_char = chr(shift + ord('A'))

            result.append(encrypted_char)
            key_index = (key_index + 1) % key_length
        else:
            result.append(char)

    return ''.join(result)

key = input("Enter Key: ")
text = input("Enter Plain text: ")
encrypted_text = cipher(text, key, action="encrypt")
print("Encrypted:", encrypted_text)

decrypted_text = cipher(encrypted_text, key, action="decrypt")
print("Decrypted:", decrypted_text)
