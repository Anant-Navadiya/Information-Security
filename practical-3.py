def prepare_message(message):
    message = message.replace(' ', '')
    message = message.upper()
    message = message.replace('J', 'I')
    message_pairs = [message[i:i + 2] for i in range(0, len(message), 2)]

    if len(message) % 2 == 1:
        message_pairs.append(message[-1] + 'X')
    return message_pairs


def build_playfair_matrix(key):
    key = key.replace(' ', '')
    key = key.upper()
    key = key.replace('J', 'I')
    key = ''.join(sorted(set(key), key=key.index))

    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = []

    for char in key + alphabet:
        if char not in matrix:
            matrix.append(char)

    playfair_matrix = [matrix[i:i + 5] for i in range(0, 25, 5)]

    return playfair_matrix


def find_char_positions(matrix, char):
    positions = []
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                positions.append((i, j))
    return positions


def playfair_cipher(message, key, action="encrypt"):
    message_pairs = prepare_message(message)
    playfair_matrix = build_playfair_matrix(key)

    result = []

    for pair in message_pairs:
        char1, char2 = pair[0], pair[1]
        row1, col1 = find_char_positions(playfair_matrix, char1)[0]
        row2, col2 = find_char_positions(playfair_matrix, char2)[0]

        if row1 == row2:
            col1 = (col1 + 1) % 5
            col2 = (col2 + 1) % 5
        elif col1 == col2:
            row1 = (row1 + 1) % 5
            row2 = (row2 + 1) % 5
        else:
            col1, col2 = col2, col1

        result.append(playfair_matrix[row1][col1] + playfair_matrix[row2][col2])

    return ' '.join(result)


key = input("Enter Key: ")
text = input("Enter Plain text: ")
encrypted_text = playfair_cipher(text, key, action="encrypt")
print("Encrypted:", encrypted_text)

decrypted_text = playfair_cipher(encrypted_text, key, action="decrypt")
print("Decrypted:", decrypted_text)
