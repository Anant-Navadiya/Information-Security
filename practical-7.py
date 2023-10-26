def encrypt(plaintext, key):
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    num_columns = len(key)
    num_rows = -(-len(plaintext) // num_columns)
    grid = [[' ' for _ in range(num_columns)] for _ in range(num_rows)]

    for i, char in enumerate(plaintext):
        row = i // num_columns
        col = i % num_columns
        grid[row][col] = char

    ciphertext = ''.join(grid[row][key_order[col]] for col in range(num_columns) for row in range(num_rows))
    return ciphertext

def decrypt(ciphertext, key):
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    num_columns = len(key)
    num_rows = -(-len(ciphertext) // num_columns)
    empty_cells = num_columns * num_rows - len(ciphertext)
    grid = [[' ' for _ in range(num_columns)] for _ in range(num_rows)]
    empty_cells_in_last_row = num_columns - empty_cells % num_columns
    pos = 0

    for col in range(num_columns):
        col_index = key_order.index(col)
        row = 0
        if col_index >= empty_cells_in_last_row:
            row = 1
        for _ in range(num_rows - row):
            grid[row][col_index] = ciphertext[pos]
            pos += 1
            row += 1

    plaintext = ''.join(grid[row][col_index] for row in range(num_rows) for col_index in key_order)
    return plaintext

key = input("Enter the encryption key: ")
plaintext = input("Enter the plaintext: ")
ciphertext = encrypt(plaintext, key)
print("Ciphertext:", ciphertext)
decrypted_text = decrypt(ciphertext, key)
print("Decrypted Text:", decrypted_text)
