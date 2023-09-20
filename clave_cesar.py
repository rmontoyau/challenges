'''
 * Crea un programa que realize el cifrado César de un texto y lo imprima.
 * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
 *
 * Te recomiendo que busques información para conocer en profundidad cómo
 * realizar el cifrado. Esto también forma parte del reto.
 */
 '''
UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DOWN = "abcdefghijklmnopqrstuvwxyz"

def coder(word, desplazamiento):
    encrypt = ""
    for c in word:
        if c.isupper():
            idx = UPPER.index(c)
            encrypt += UPPER[idx + desplazamiento]
        elif c.islower():
            idx = DOWN.index(c)
            encrypt += DOWN[idx + desplazamiento]
        else:            
            encrypt += c
    return encrypt

def decoder(word, desplazamiento):
    dencrypt = ""
    for c in word:
        if c.isupper():
            idx = UPPER.index(c)
            dencrypt += UPPER[idx - desplazamiento]
        elif c.islower():
            idx = DOWN.index(c)
            dencrypt += DOWN[idx - desplazamiento]
        else:            
            dencrypt += c
    return dencrypt

print(coder("Hola Mundo",3))
print(decoder("Krod Pxqgr",3))
