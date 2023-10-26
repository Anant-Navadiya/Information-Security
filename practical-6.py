def rail_fence_cipher(text, rails, action="encrypt"):
    text = text.replace(" ", "")
    result = ""

    if action == "encrypt":
        fence = ['' for _ in range(rails)]
        rail = 0
        direction = 1

        for char in text:
            fence[rail] += char
            rail += direction

            if rail == rails - 1 or rail == 0:
                direction *= -1

        result = "".join(fence)

    elif action == "decrypt":
        fence = ['' for _ in range(rails)]
        rail = 0
        direction = 1

        for i in range(len(text)):
            fence[rail] += '-'
            rail += direction

            if rail == rails - 1 or rail == 0:
                direction *= -1

        idx = 0
        for rail in range(rails):
            for char in range(len(fence[rail])):
                fence[rail] = fence[rail][:char] + text[idx] + fence[rail][char+1:]
                idx += 1

        rail = 0
        direction = 1
        for char in range(len(text)):
            result += fence[rail][0]
            fence[rail] = fence[rail][1:]
            rail += direction

            if rail == rails - 1 or rail == 0:
                direction *= -1

    return result

rails = int(input("Enter rail: "))
text = input("Enter Plain text: ")
encrypted_text = rail_fence_cipher(text, rails, action="encrypt")
print("Encrypted:", encrypted_text)

decrypted_text = rail_fence_cipher(encrypted_text, rails, action="decrypt")
print("Decrypted:", decrypted_text)
