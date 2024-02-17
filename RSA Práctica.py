#practica de algoritmo RSA
#Cifrado de mensaje

import Crypto.Util.number
import hashlib

#Numero de bits 
bits= 1024
A=Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)

B=Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)

print("A:", A)
print("B:", B)

#Obtener los primos para Alice y Bob
pA=Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)

pB=Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)

print("pA:", pA)
print("pB:", pB)

na=A*B

print("na:", na)

nb=pA*pB

print("nb:", nb)

phiA=(A-1)*(B-1)

print("phiA:", phiA)

phiB=(pA-1)*(pB-1)

print("phiB:", phiB)

#por razones de eficiencia usaremos el numero 4 de fer,at, 65537, debido a que es un primo largo y no es potencia de 2
#y como forma parte de la clave pública no es necesario calcularlo
e=65537

#Caclular la llave privada de alice y bob

dA=Crypto.Util.number.inverse(e, phiA)
print("dA:", dA)

dB=Crypto.Util.number.inverse(e, phiB)
print("dB:", dB)

#ciframos el mensaje
msg= "Hola Bob, soy Alice"

hashed_msg = hashlib.sha256(msg.encode()).hexdigest()
hashed_msg_integer = int(hashed_msg, 16)

print("Mensaje:", msg)
print("Logitud del mensaje en bytes:", len(msg.encode('utf-8')))

#Converit el mensaje a un numero
m=int.from_bytes(msg.encode('utf-8'), byteorder='big')
print("Mensaje en numero:", m)

c=pow(m, e, nb)
print("Mensaje cifrado:", c)

#desciframos el mensaje
des=pow(c, dB, nb)
print("Mensaje descifrado:", des)

msg_final=int.to_bytes(des, len(msg), byteorder='big').decode('utf-8')
print("Mensaje final:", msg_final)

#verificar la firma
C=pow(hashed_msg_integer,dA,na)

Comprueba=pow(C,e,na)

if Comprueba == hashed_msg_integer:
    print("La firma es correcta")
else:
    print("La firma es incorrecta")