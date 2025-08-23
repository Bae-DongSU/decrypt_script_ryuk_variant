from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import binascii

key_hex = "" #Write your key here
key = binascii.unhexlify(key_hex)

encoded_file_path = "" #Write your encrypted file's path here
with open(encoded_file_path, "rb") as f:
    data = f.read()

iv = data[:12] #Initial Vector, 12 Bytes
tag = data[-16:] #Authentication Tag, 16 Bytes
ct = data[12:-16] #Other data. It will be changed to plain text.

plaintext = None
try:
    module = AESGCM(key) #GCM Module
    plaintext = module.decrypt(iv, ct + tag, None) #Decrypt with key, iv, Authentication tag
except Exception as e:
    plaintext = str(e) #Plaintext. (Decrypted Ciphertext)

plaintext[:200] if isinstance(plaintext, bytes) else plaintext #You can check 200 bytes from start of File when you successfully decrypted
