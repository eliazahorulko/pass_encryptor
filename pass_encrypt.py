import random
import string


def pad_to_length(text: str, length: int) -> str:
    if len(text) < length:
        text += ''.join(random.choices(string.ascii_letters + string.digits, k=length - len(text)))
    return text


def xor_encrypt(password: str, key: str) -> str:
    max_length = max(len(password), len(key))
    password = pad_to_length(password, max_length)
    key = pad_to_length(key, max_length)

    # Encrypt password using XOR
    encrypted = [chr(ord(p) ^ ord(k)) for p, k in zip(password, key)]

    # Convert encrypted characters to a readable hex format
    return ''.join(f'{ord(c):02x}' for c in encrypted)


def xor_decrypt(encrypted_hex: str, key: str) -> str:
    max_length = len(encrypted_hex) // 2
    key = pad_to_length(key, max_length)

    # Convert hex back to characters
    encrypted_chars = [chr(int(encrypted_hex[i:i + 2], 16)) for i in range(0, len(encrypted_hex), 2)]

    # Decrypt using XOR again
    decrypted = [chr(ord(c) ^ ord(k)) for c, k in zip(encrypted_chars, key)]

    return ''.join(decrypted)


# Example usage
password = "secret"
key = "mykey"  # The key length is now automatically adjusted

encrypted_password = xor_encrypt(password, key)
print(f"Encrypted password: {encrypted_password}")

# Decryption
decrypted_password = xor_decrypt(encrypted_password, key)
print(f"Decrypted password: {decrypted_password}")
