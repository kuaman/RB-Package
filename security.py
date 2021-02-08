from cryptography.fernet import Fernet
import base64
import hashlib


def encrypt(dec):
    m = hashlib.sha256()
    m.update(
        b"v*8+DpVHD9Ny9JrJt^kG#G3n=@!8z3_GuZ%9ke*@6Xs621Yxq-buC^s-R4vqe!1Te8?TbaSVj$+AyWT332pj4s=uZ2FKdWU-@^E7A2v!@zUp")
    key = base64.urlsafe_b64encode(m.digest())
    dec = bytes(dec, 'utf-8')
    result = Fernet(key)
    return result.encrypt(dec)


def decrypt(enc):
    m = hashlib.sha256()
    m.update(
        b"v*8+DpVHD9Ny9JrJt^kG#G3n=@!8z3_GuZ%9ke*@6Xs621Yxq-buC^s-R4vqe!1Te8?TbaSVj$+AyWT332pj4s=uZ2FKdWU-@^E7A2v!@zUp")
    key = base64.urlsafe_b64encode(m.digest())
    cipher_suite = Fernet(key)
    decoded_text = cipher_suite.decrypt(enc)
    return decoded_text.decode('utf-8')
