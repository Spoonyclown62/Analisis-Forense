import hashlib
import Crypto.Util.number
import random
import string

CDT=256
hashlib_CDT=hashlib.sha256(str(CDT).encode())
print(hashlib_CDT.hexdigest())

txt1024 = ''.join(random.choices(string.ascii_letters + string.digits, k=128))
hashlib_txt1024=hashlib.sha256(str(txt1024).encode())
print(hashlib_txt1024.hexdigest())

with open("PDFP.pdf", "rb") as f:
    h1 = hashlib.sha256(f.read()).digest()
    print(h1.hex())

with open("PDFP2.pdf", "rb") as f2:
    h2 = hashlib.sha256(f2.read()).digest()
    print(h2.hex())