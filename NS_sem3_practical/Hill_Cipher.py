import numpy as np

# Function to generate the key matrix
def generate_key_matrix(key):
    key_matrix = np.array([[ord(key[0]) - 65, ord(key[1]) - 65], [ord(key[2]) - 65, ord(key[3]) - 65]])
    return key_matrix

# Function to encrypt a message using the Hill cipher
def encrypt(message, key):
    message = message.upper().replace(" ", "")
    while len(message) % 2 != 0:
        message += 'X'

    key_matrix = generate_key_matrix(key)
    message_matrix = np.array([ord(char) - 65 for char in message])
    message_matrix = message_matrix.reshape(-1, 2)
    encrypted_text = ""
    for chunk in message_matrix:
        chunk = np.transpose([chunk])
        result = np.dot(key_matrix, chunk) % 26
        for num in np.nditer(result):
            encrypted_text += chr(num + 65)

    return encrypted_text

# Function to decrypt a message using the Hill cipher
def decrypt(ciphertext, key):
    key_matrix = generate_key_matrix(key)
    determinant = key_matrix[0][0] * key_matrix[1][1] - key_matrix[0][1] * key_matrix[1][0]
    multiplicative_inverse = -1
    for i in range(26):
        if (determinant * i) % 26 == 1:
            multiplicative_inverse = i
            break
    inverse_matrix = np.array([[key_matrix[1][1], -key_matrix[0][1]], [-key_matrix[1][0], key_matrix[0][0]]])
    inverse_matrix = (multiplicative_inverse * inverse_matrix) % 26

    decrypted_text = ""
    for i in range(0, len(ciphertext), 2):
        chunk = np.array([ord(ciphertext[i]) - 65, ord(ciphertext[i + 1]) - 65])
        chunk = np.transpose([chunk])
        result = np.dot(inverse_matrix, chunk) % 26
        for num in np.nditer(result):
            decrypted_text += chr(num + 65)

    return decrypted_text

# Input from the user
key = input("Enter the 4-letter key: ")
while len(key) != 4:
    print("Please enter a 4-letter key.")
    key = input("Enter the 4-letter key: ")

message = input("Enter the plaintext: ")

# Encrypt the message
encrypted_message = encrypt(message, key)
print("Encrypted message:", encrypted_message)

# Decrypt the encrypted message
decrypted_message = decrypt(encrypted_message, key)
print("Decrypted message:", decrypted_message)

