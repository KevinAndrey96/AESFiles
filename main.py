import pyaes
import base64

def encrypt(plaintext, key):
    if plaintext:
        if not key:
            raise Exception("No key given to encrypt password")
        aes = pyaes.AESModeOfOperationCTR(key)
        return (base64.b64encode(aes.encrypt(plaintext))).decode("utf-8")

def decrypt(encrypted, key):
    if encrypted:
        if not key:
            raise Exception("No key given to decrypt password")
        aes = pyaes.AESModeOfOperationCTR(key)
        return (aes.decrypt(base64.b64decode(encrypted))).decode("utf-8")
"""
#key_128 = b'CLAVEDE128BITSSS'
#key_192 = b'CLAVE_DE_192_BITS_24BYTE'
#key_256 = b'CLAVE_DE_256_BITS_-_32_BYTES00GG'
"""
Rta=int(input("Bienvenido\n\n1. Cifrar\n2. Descifrar\n\nRta: "))
if Rta==1:
    archivo=input("Ingrese el nombre del archivo a cifrar: ")
    with open(archivo, "rb") as img_file:
        b64image = base64.b64encode(img_file.read())

    Key=bytes(input("Ingrese la clave (16, 24 o 32 carácteres para modo de operación 128 bits, 192 bits o 256 bits respectivamente)\n\nRta: "), 'utf-8')
    print("Archivo en base64: ", b64image)

    encriptada = encrypt(b64image,Key)

    print("Archivo cifrado: ",encriptada)
    #encriptada64=base64.b64encode(encriptada)
    encriptada64=encriptada
    print("Archivo cifrado en base64: ",encriptada64)

    image = open(""+archivo, "wb")
    image.write(base64.b64decode(encriptada64))
    image.close()
    print("Guardado como ",""+archivo)
else:
    archivo = input("Ingrese el nombre del archivo a descifrar: ")
    Key=bytes(input("Ingrese la clave (16, 24 o 32 carácteres para modo de operación 128 bits, 192 bits o 256 bits respectivamente)\n\nRta: "), 'utf-8')
    with open(archivo, "rb") as img_file:
        b64image2 = base64.b64encode(img_file.read())
        #b64image2 = img_file.read()
    print("Archivo leido en base64: ", b64image2)


    #desencriptada=base64.b64decode(b64image2)
    desencriptada=b64image2

    desencriptada=decrypt(desencriptada,Key)

    print("Archivo descifrado en base64: ",desencriptada)

    image = open(""+archivo, "wb")
    image.write(base64.b64decode(desencriptada))
    image.close()
    print("Guardado como ", ""+archivo)