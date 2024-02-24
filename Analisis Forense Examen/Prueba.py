import hashlib
import Crypto.Util.number
import hashlib

def dvdstring(string, longitud):
    subcadenas = []
    for i in range(0, len(string), longitud):
        subcadenas.append(string[i:i+longitud])
    return subcadenas

#Cifrado de mensaje
#Numero de bits 
bits= 1024
A=Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)

B=Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)

#print("A:", A)
#print("B:", B)

#Obtener los primos para Alice y Bob
pA=Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)

pB=Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)

#print("pA:", pA)
#print("pB:", pB)

na=A*B

#print("na:", na)

nb=pA*pB

#print("nb:", nb)

phiA=(A-1)*(B-1)

#print("phiA:", phiA)

phiB=(pA-1)*(pB-1)

#print("phiB:", phiB)

#por razones de eficiencia usaremos el numero 4 de fer,at, 65537, debido a que es un primo largo y no es potencia de 2
#y como forma parte de la clave pública no es necesario calcularlo
e=65537

#Caclular la llave privada de alice y bob

dA=Crypto.Util.number.inverse(e, phiA)
#print("dA:", dA)

dB=Crypto.Util.number.inverse(e, phiB)
#print("dB:", dB)

# Generar mensaje aleatorio
M = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur maximus metus sed erat euismod aliquam. Integer posuere erat ut nibh rhoncus lacinia. Morbi ac convallis urna. Aliquam quis leo venenatis, tincidunt odio quis, hendrerit odio. In hac habitasse platea dictumst. Duis a ultricies libero. Praesent et dui finibus, aliquam lorem id, volutpat lacus. Donec condimentum consectetur ex eget feugiat. Vivamus auctor nisi at tempus varius. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vivamus in commodo arcu. Suspendisse potenti. Suspendisse commodo orci metus, ut ornare elit semper vel. Mauris et porta magna. Maecenas vel scelerisque enim. Aliquam sed orci id justo maximus ullamcorper at vitae nibh. Vivamus condimentum finibus nisl, in condimentum elit condimentum vitae. Sed vel quam ac mauris lobortis luctus. Nulla id dui ut sem ultricies ornare. Cras egestas nisl sed tellus maximus ornare. Pellentesque porttitor pulvinar dolor. Nullam porttitor venenatis dolor id vestibulum. In ex justo, sollicitudin non purus in, sagittis dictum ipsum."
longitud_subcadena = 128

subcadenas = dvdstring(M, longitud_subcadena)

c=[]

for i in subcadenas:
    m=int.from_bytes(i.encode('utf-8'), byteorder='big')
    c.append(pow(m, e, nb))
    #print("Mensaje cifrado:", c)
    #print("Mensaje en numero :", m)

des=[]
mdcf=[]
for i in c:
    mc=c.pop()
    des.append(pow(mc, dB, nb))
    
    #mdcf = des.to_bytes((des.bit_length() + 7) // 8, byteorder='big')
    #mdcf += mdcf.decode('utf-8')

print("Mensaje descifrado:", des)
msgjoin="".join(des)
print("Mensaje unido:", msgjoin)

#for subcadena in subcadenas:
 #   print(subcadena)    
# Calcular hash del mensaje 
    
h = hashlib.sha256(M.encode()).hexdigest()
print(h)

