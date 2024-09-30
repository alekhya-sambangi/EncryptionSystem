import re

def generate_playfair_matrix(key):
    key = re.sub(r"[^a-zA-Z]", "", key).upper()
    key = "J" + key
    key = re.sub(r"J", "I", key)

    result = []
    for char in key:
        if char not in result:
            result.append(char)

    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    for char in alphabet:
        if char not in result:
            result.append(char)

    playfair_matrix = [result[i: i + 5] for i in range(0, 25, 5)]
    return playfair_matrix


def encrypt_message(message, key):
    playfair_matrix = generate_playfair_matrix(key)
    message = re.sub(r"[^a-zA-Z]", "", message).upper()
    message = re.sub(r"J", "I", message)

    new_message = []
    for i in range(0, len(message), 2):
        pair = message[i: i + 2]

        if len(pair) < 2:
            pair += "X"

        if pair[0] == pair[1]:
            pair = pair[0] + "X"

        new_message.append(pair)

    encrypted_message = ""
    for pair in new_message:
        char1, char2 = pair[0], pair[1]
        r1, c1 = get_position(playfair_matrix, char1)
        r2, c2 = get_position(playfair_matrix, char2)

        if r1 == r2:
            encrypted_message += playfair_matrix[r1][(c1 + 1) % 5]
            encrypted_message += playfair_matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:
            encrypted_message += playfair_matrix[(r1 + 1) % 5][c1]
            encrypted_message += playfair_matrix[(r2 + 1) % 5][c2]
        else:
            encrypted_message += playfair_matrix[r1][c2]
            encrypted_message += playfair_matrix[r2][c1]

    return encrypted_message


def decrypt_message(message, key):
    playfair_matrix = generate_playfair_matrix(key)

    decrypted_message = ""
    for i in range(0, len(message), 2):
        pair = message[i: i + 2]
        char1, char2 = pair[0], pair[1]
        r1, c1 = get_position(playfair_matrix, char1)
        r2, c2 = get_position(playfair_matrix, char2)

        if r1 == r2:
            decrypted_message += playfair_matrix[r1][(c1 - 1) % 5]
            decrypted_message += playfair_matrix[r2][(c2 - 1) % 5]
        elif c1 == c2:
            decrypted_message += playfair_matrix[(r1 - 1) % 5][c1]
            decrypted_message += playfair_matrix[(r2 - 1) % 5][c2]
        else:
            decrypted_message += playfair_matrix[r1][c2]
            decrypted_message += playfair_matrix[r2][c1]

    return decrypted_message


def get_position(matrix, char):
    for r, row in enumerate(matrix):
        if char in row:
            return r, row.index(char)


# Example usage:
key = "HELLO"
message = "ENCRYPTION"
print("original message:ENCRYPTION")
encrypted_message = encrypt_message(message, key)
print(f"Encrypted message: {encrypted_message}")
decrypted_message = decrypt_message(encrypted_message, key)
print(f"Decrypted message: {decrypted_message}")
