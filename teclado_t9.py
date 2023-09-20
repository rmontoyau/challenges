'''
Los primeros dispositivos móviles tenían un teclado llamado T9
con el que se podía escribir texto utilizando únicamente su
teclado numérico (del 0 al 9).
 *
Crea una función que transforme las pulsaciones del T9 a su
representación con letras.
- Debes buscar cuál era su correspondencia original.
- Cada bloque de pulsaciones va separado por un guión.
- Si un bloque tiene más de un número, debe ser siempre el mismo.
- Ejemplo:
    Entrada: 6-666-88-777-33-3-33-888
    Salida: MOUREDEV
'''

T9 = {"2" : "ABC",
      "3" : "DEF",
      "4" : "GHI",
      "5" : "JKL",
      "6" : "MNO",
      "7" : "PQRS",
      "8" : "TUV",
      "9" : "WXYZ",
      "0" : " "}

def decode(char):    
    idx = len(char) -1
    c = char[0]
    l = T9[c]
    return l[idx]

def teclado(word):
    out = ""
    items = word.split("-")
    for item in items:
        out += decode(item)
    return out

print(teclado("777-88-3-999"))