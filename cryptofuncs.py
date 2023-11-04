'''
Utility functions for generating encrypted messages used in sample SIGINT dataset.
'''
import hashlib


def encrypt_message(message_text, key):
    '''
    Encrypts a string using a XOR cipher with a given key.

    Parameters:
        string (str): The string to be encrypted.
        key (str): The key to use for encryption.

    Returns:
        str: The encrypted string in hexadecimal format.

    Raises:
        TypeError: If string or key are not strings.
    '''
    # hash the key using MD5
    key_hash = hashlib.md5(key.encode()).digest()

    # XOR each byte of the message with the corresponding byte from the hash
    encryped_msg = bytearray()
    for i, b in enumerate(message_text.encode()):
        encryped_msg.append(b ^ key_hash[i % len(key_hash)])

    return encryped_msg.hex()


def decrypt_string(encrypted_msg, key):
    '''
    Decrypts a string using a XOR cipher with a given key.

    Parameters:
        string (str): The string to be encrypted.
        key (str): The key to use for encryption.

    Returns:
        str: The decrypted string.

    Raises:
        TypeError: If string or key are not strings.
    '''
    # Hash the key using MD5
    key_hash = hashlib.md5(key.encode()).digest()
    # Convert the encrypted string from hex to bytes
    encrypted_msg = bytearray.fromhex(encrypted_msg)
    # XOR each byte of the encrypted string with the corresponding byte of the hash
    decrypted_msg = bytearray()
    for i, b in enumerate(encrypted_msg):
        decrypted_msg.append(b ^ key_hash[i % len(key_hash)])
    # Return the decrypted string as a normal string
    return decrypted_msg.decode()


# example usage
message = "Hello, world!"
key = "secret"
encrypted = encrypt_message(message, key)
print(encrypted)

decrypted = decrypt_string(encrypted, key)
print(decrypted)
