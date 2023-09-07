from Crypto.Cipher import AES
import os

# Generate a random key
key = os.urandom(16)

# Encrypt the message
cipher = AES.new(key, AES.MODE_EAX)
message = input("Enter message to encrypt: ").encode()
ciphertext, tag = cipher.encrypt_and_digest(message)
nonce = cipher.nonce

print("\nEncrypted message: ", ciphertext)
print("tag: ", tag)
print("nonce value: ", nonce)

# Decrypt the message
cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
decrypted = cipher.decrypt_and_verify(ciphertext, tag)

print("\nDecrypted message: ", decrypted.decode())