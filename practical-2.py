def create_monoalphabetic_key(key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = key.lower()

    key = ''.join(sorted(set(key), key=key.index))

    if len(key) != 26:
        return None  #

    key_mapping = {}

    for i in range(26):
        key_mapping[alphabet[i]] = key[i]

    return key_mapping


def monoalphabetic_cipher(text, key, action="encrypt"):
    key_mapping = create_monoalphabetic_key(key)

    if key_mapping is None:
        return "Invalid key"

    result = []

    for char in text:
        if char.isalpha():
            char_lower = char.lower()
            if char_lower in key_mapping:
                if char.isupper():
                    result.append(key_mapping[char_lower].upper())
                else:
                    result.append(key_mapping[char_lower])
            else:
                result.append(char)
        else:
            result.append(char)

    return ''.join(result)


key = "zyxwvutsrqponmlkjihgfedcba"
text = input("Enter Plain text: ")

encrypted_text = monoalphabetic_cipher(text, key, action="encrypt")
print("Encrypted:", encrypted_text)

decrypted_text = monoalphabetic_cipher(encrypted_text, key, action="decrypt")
print("Decrypted:", decrypted_text)
