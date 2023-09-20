# Code challenges
Este repositorio mostrará como resolvi algunos de los challenges o retos de programación que encontre por internet
Contiuación 

## Reto  Permutaciones
El reto consiste en crear un programa que sea capaz de generar e imprimir todas las permutaciones disponibles formadas por las letras de una palabra.
- Las palabras generadas no tienen por qué existir.
- Deben usarse todas las letras en cada permutación.
- Ejemplo: sol, slo, ols, osl, los, lso 

### solución
Ee crea un metodo recursivo donde se optienen todas las combinaciones posibles apartir de 3 caracteres
el método recursivo reduce el arreglo a 2 generando las combinaciones posibles.
al retornar agrega el siguente elemento a la lista creando nueas secuencias
> #### Ejemplo
> Para este caso utilizaremos la seguiente secuencia  **"abcd"**
> Se reduce a **bcd**  luego a  **cd**, obteniendo la siguiente combinación **[cd,dc]**
> Luego se  combina con la **b** que es la sigueinte en la lista para obtener **[bcd,cbd,cdb,bdc,dbc,dcb]**
> se vuelve a combinar agregando la **a** generando
> **['abcd', 'abdc', 'acbd', 'adbc', 'acdb', 'adcb', 'bacd', 'badc', 'cabd', 'dabc', 'cadb', 'dacb', 'bcad', 'bdac', 'cbad', > 'dbac', 'cdab', 'dcab', 'bcda', 'bdca', 'cbda', 'dbca', 'cdba', 'dcba']**
> asi con cualquier arreglo.

Ver solución [aquí](/challenges/permutations.py)

## Reto abaco
Crea una función que sea capaz de leer el número representado por el ábaco.
- El ábaco se representa por un array con 7 elementos.
- Cada elemento tendrá 9 **O** (aunque habitualmente tiene 10 para realizar  operaciones) para las cuentas y una secuencia de  **---** para el alambre.
- El primer elemento del array representa los millones, y el último las unidades.
- El número en cada elemento se representa por las cuentas que están a   la izquierda del alambre.

### Ejemplo de array y resultado:
> 
> ["O---OOOOOOOO ",
>  "OOO---OOOOOO",
> "---OOOOOOOOO",
>  "OO---OOOOOOO",
>  "OOOOOOO---OO",
>  "OOOOOOOOO---",
>  "---OOOOOOOOO"]
> 
>  Resultado: 1.302.790
 
### Solución
Se creo una función llamada get number que analizará cada item del arreglo por separado.
En cada item se realizará un string split utilizando **---** como referencia, retornando una lista con dos elementos, el primero con la cantidad de 0 previos al **---** que representan la cantidad de bolotas seleccionadas para ese item.
luego se eso se cuentan las el largo del string para obtener el numero que le corresponde ie:

> Valor original "OO---OOOOOOO" se realiza el split obteniendo ["OO",OOOOOOO], realizamos un count para el primer valor el cual nos retorna un **2**

El siguiente paso es crear un loop que recorra el arreglo y obtenga el valor correspondiente a cada item para asi obtener el resultado total.

Ver código [aqui](/challenges/abaco.py)

## Reto Teclado T9
Los primeros dispositivos móviles tenían un teclado llamado T9 con el que se podía escribir texto utilizando únicamente su teclado numérico (del 0 al 9).

Crea una función que transforme las pulsaciones del T9 a su representación con letras.
- Debes buscar cuál era su correspondencia original.
- Cada bloque de pulsaciones va separado por un guión.
- Si un bloque tiene más de un número, debe ser siempre el mismo.
 Ejemplo:
> Entrada: **777-88-3-999-0-6-666-66-8-666-999-2**
> Salida: **RUDY MONTOYA**

### Solución
Se creo una lista para mapear cada la combinación de del teclado
> T9 = {"2" : "ABC",
      "3" : "DEF",
      "4" : "GHI",
      "5" : "JKL",
      "6" : "MNO",
      "7" : "PQRS",
      "8" : "TUV",
      "9" : "WXYZ",
      "0" : " "}
     
Mediante esta lista se obtiene el valor buscado segun la cantidad de numeros indicados, si se dan **777** se cuenta la cantidad de numeros y se retorna la 3ra posición del arreglo correspondiente a **7** que corresponde a **R**.
De esta forma se recorre cada combinación de numeros. hasta lograr decifrar toda la pablabra.

Ver solución [aqui](/challenges/teclado_t9.py)

 ## Reto Clave Cesar
 Crea un programa que realize el cifrado César de un texto y lo imprima. 
 También debe ser capaz de descifrarlo cuando así se lo indiquemos.
### Que es clave cesar
El principio básico del cifrado César consiste en desplazar cada letra del mensaje original un número fijo de posiciones en el alfabeto. Por ejemplo, si se utiliza un desplazamiento de 3 posiciones hacia adelante, la letra 'A' se convierte en 'D', 'B' se convierte en 'E', 'C' se convierte en 'F', y así sucesivamente. Este desplazamiento se llama "clave" y determina cómo se cifra el mensaje.
Para descifrar el mensaje, se realiza el proceso inverso: se desplazan las letras hacia atrás en el alfabeto utilizando la misma clave. Es importante que el remitente y el destinatario conozcan la clave utilizada para cifrar y descifrar los mensajes.
### Solución
Se mapean los caracterés en mayuscula y en minuscula para tener referencia a ellos. Los demás caracteres incluidos números quedarás tal como se escriben.
Mapa de datos
> UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
> DOWN = "abcdefghijklmnopqrstuvwxyz"

Acorde al desplazamiento se moveran hacia adelante para obtener el caracter que corresponda, si el caracter se sale del arreglo, e iniciará de nuevo ie: si es deplazamiento de 3 y se seleccionala **Z** el resultado seria **C**.
Para decodificar se realiza el paso a la inverza en lugar de sumar el desplazamiento, este se le resta, para obtener el mensaje.
Ver solución [aquí](/challenges/clave_cesar.py)
