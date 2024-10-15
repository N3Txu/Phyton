from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend
import os, base64


#generar clave
def generate_key(password: str, salt: bytes)->bytes:
    kdf=Scrypt(salt=salt, length=32, n=2**14, r=8, p=1, backend=default_backend())
    return kdf.derive(password.encode())

#funcion para cifrar
def encrypt(plaintext: str, key: bytes, nonce: bytes)->bytes:
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(nonce, plaintext.encode(), None)
    return base64.b64encode(ciphertext).decode()

#funcion para decifrar
def decrypt(ciphertext: str, key: bytes, nonce: bytes)->str:
    try:
        aesgcm = AESGCM(key)
        ciphertext = base64.b64decode(ciphertext)
        plaintext = aesgcm.decrypt(nonce, ciphertext, None)
        return plaintext.decode()
    except Exception as e:
        print("error during decryption:", e)
        return ""
    
if __name__ == "__main__":
    #ejemplo de uso
    password = "3215966266"
    salt = os.urandom(16)
    key = generate_key(password, salt)
    nonce = os.urandom(12)
    
    #mensaje a cifrar
    mensaje = "this message will be encrypted"
    
    #cifrado
    cifrado = encrypt(mensaje, key, nonce)
    print("message crypted:", cifrado)
    
    #descifrado
    descifrado = decrypt(cifrado, key, nonce)
    print("message decrypted:", descifrado)