from Crypto.Util import number
import random
 
#Ejercicio #1
#print("Obtener numero aleatorio de 256 bits usando Random", random.getrandbits(1024),'\n')

#Ejercicio #2
#Obtener numero primo
i=0
while(True):
    i=i+1
    j=random.getrandbits(1024)
    esPrimo= number.isPrime(j)
    if (esPrimo):
        print("En la iteración: ",i," se en5}333333333ontro el numero primo:",j,"\n")
        break

#Ejercicio 3
#Obtener el inverso multiplicativo
def inversoMultiplicativo(x,y):
    print("Ejercicio 3, el inverso multiplicativo del numero X:","\n",x,"\n","y el numero y: ","\n",y,"\n", "es: ","\n",number.inverse(x,y),"\n")

a=random.getrandbits(1024)
b= random.getrandbits(1024)

inversoMultiplicativo(a,b)

#Ejerjcicio #4
#Potencia de un numero  7821564qqqqqqqqqqqq^e mod p, donde "e" es un numero de 256 bits y "p" es un primo de 1024 bits
a=2
b=random.getrandbits(256)
c=j

def potencia(x,y,z):
    print("Ejercicio 4- la potencia de x a la u mod z es:","\n",pow(x,y,z))

potencia(a,b,c)