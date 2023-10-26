import numpy as np

def prepare_message(message, key_size):
    message = message.replace(" ", "").upper()
    while len(message) % key_size != 0:
        message += 'X'
    return message


def matrix_inverse(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det_inverse = -1
    for i in range(0, modulus):
        if (det * i) % modulus == 1:
            det_inverse = i
            break
    if det_inverse == -1:
        return None

    adjoint_matrix = np.round(np.linalg.inv(matrix) * det)
    inverse_matrix = (adjoint_matrix * det_inverse) % modulus
    return inverse_matrix


def hill_cipher(message, key_matrix, action="encrypt"):
    key_size = key_matrix.shape[0]
    modulus = 26

    if action == "encrypt":
        message = prepare_message(message, key_size)
        result = []

        for i in range(0, len(message), key_size):
            block = message[i:i + key_size]
            block_vector = [ord(char) - ord('A') for char in block]
            encrypted_block = np.dot(key_matrix, block_vector) % modulus
            encrypted_chars = [chr(encrypted + ord('A')) for encrypted in encrypted_block]
            result.extend(encrypted_chars)

        return ''.join(result)

    elif action == "decrypt":
        inverse_matrix = matrix_inverse(key_matrix, modulus)
        if inverse_matrix is None:
            return "Matrix not invertible"

        result = []
        for i in range(0, len(message), key_size):
            block = message[i:i + key_size]
            block_vector = [ord(char) - ord('A') for char in block]
            decrypted_block = np.dot(inverse_matrix, block_vector) % modulus
            decrypted_chars = [chr(decrypted + ord('A')) for decrypted in decrypted_block]
            result.extend(decrypted_chars)

            return ''.join(result)
        else:
            return "Invalid action"


key_matrix = np.array([[6, 24], [1, 13]])
text = input("Enter Plain text: ")
encrypted_text = hill_cipher(text, key_matrix, action="encrypt")
print("Encrypted:", encrypted_text)

decrypted_text = hill_cipher(encrypted_text, key_matrix, action="decrypt")
print("Decrypted:", decrypted_text)

