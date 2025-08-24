from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import binascii, os

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

#Add Decrypted File to Path
out_file_name = encoded_file_path[:-4] if encoded_file_path.endswith(".ryk") else encoded_file_path + ".decrypt"
with open(out_file_name, "wb") as f:
    f.write(plaintext)
