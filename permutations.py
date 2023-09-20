'''
Crea un programa que sea capaz de generar e imprimir todas las 
permutaciones disponibles formadas por las letras de una palabra.
- Las palabras generadas no tienen por qué existir.
- Deben usarse todas las letras en cada permutación.
- Ejemplo: sol, slo, ols, osl, los, lso 
'''
'''
Solución
    se crea un metodo recursivo donde se optienen todas las combinaciones posibles apartir de 3 caracteres
    el método recursivo reduce el arreglo a 2 generando las combinaciones posibles.
    al retornar agrega el siguente elemento a la lista creando nueas secuencias
    ie
    word 0 "abcd"
    se recuce a bcd -> cd, obteniendo la siguiente combinación [cd,dc]
    re combina con la b que es la sigueinte en la lista para obtener [bcd,cbd,cdb,bdc,dbc,dcb]
    se vuelve a combinar agregando la a generando
    ['abcd', 'abdc', 'acbd', 'adbc', 'acdb', 'adcb', 'bacd', 'badc', 'cabd', 'dabc', 'cadb', 'dacb', 
    'bcad', 'bdac', 'cbad', 'dbac', 'cdab', 'dcab', 'bcda', 'bdca', 'cbda', 'dbca', 'cdba', 'dcba']
    asi con cualquier arreglo.
'''
def search_permutations(word, combinations):
    word_len = len(word)
    char = word[0]
    if word_len == 1:
        return word
    if word_len == 2 :
        return [word, word[1]+word[0]]
    if word_len >= 3:
        combinations = search_permutations(word[1:], combinations)
        items = []
    for i in range(word_len):
        for item in combinations:
            items.append(item[:i] + char + item[i:])
        
    return items




def permutations(word: str):
    return search_permutations(word,[])

print((permutations("sol")))

        
    

