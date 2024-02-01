#Cifrado Fernet
#importamos Fernet
from cryptography.fernet import Fernet
#Generamos la clave
clave= Fernet.generate_key()
#Generamos la instancia de Fernet
f=Fernet(clave)
token = f.encrypt(b'Mensaje Secreto')
#Mensaje Cifrado
print(token)
#Descifrar
des= f.decrypt(token)
print("\n",des)

Clave2="KazX6oDQZen_bhZNVvRVcGVJKqlzTjJ_ksiNm--WlPk="
f2= Fernet(Clave2)
Mensaje="gAAAAABluwPSDHJ3Pi2kcuWbUs4UTYHJJ65NJ6Aw9f6JTD7r2TGLzZLFKNvJX2CVgIluQb6QbJy-Pnp_4zmIQFiFQJTydukRdoVPm215bDqPTeRZgg19awLqkGcJHMdv2uXgglVuJ2Lr"
result=f2.decrypt(Mensaje)
print(result)
