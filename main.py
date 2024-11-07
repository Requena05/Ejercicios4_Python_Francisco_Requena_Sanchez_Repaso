'''Ejercicio 1. Crea una función que devuelva los número primos entre un rango de
números, i.e.: ej1(10, 15) devolvería [11, 13]'''

def es_primo(num1)->bool:
    valid=False
    for x in range(1,num1):
        for i in range(2, num1):
            if (num1 % i) == 0:
                return False
        return True

def rango_primos(num1,num2)->list:
    nums=list(range(num1,num2))

    L1=[x for x in nums if es_primo(x)]

    return L1

print(rango_primos(12,24))

'''Ejercicio 2. Crea una función que dada una lista de palabras devuelva otra lista con
solo aquellas palabras cuya longitud sea igual o mayor a una longitud dada'''

def longitud_palabra(longitud,lista)->list:
   lista_completa=[]
   for valor in lista:
       if len(valor)>=longitud:
            lista_completa.append(valor)

   return lista_completa

print(longitud_palabra(4,["Biotecnología","Nanotecnología","Electromagnetismo","DRO"]))


'''Ejercicio 3. Crea una función que dada una lista con número devuelva otra lista con el
cuadrado de dichos números'''



'''Ejercicio 4. Crea una función que reciba dos listas de entrada (l1 y l2) y que inserte
los elementos de l2 que no están en l1 al final de l1'''


'''Ejercicio 5. Crea una función que dada una lista de palabras y una palabra elimine
todas apariciones de la palabra en la lista'''


'''Ejercicio 6. Crea una función que dadas dos listas (l1 y l2) elimine todos los
elementos de l1 que se encuentran en las posiciones especificadas por l2 😱'''


'''Ejercicio 7. Crea una función que dada una lista de números y un número devuelva
una lista con los índices de todas las apariciones de dicho número en la lista 😱


Ejercicio 8. Dada la siguiente lista: ['Borja', 'borja@mail.com', 989565222, 'Marta',
'marta@mail.com', 989565333, 'Ricardo', 'raicar@mail.com', 989565444] que contiene
datos de contactos en la forma: ‘nombre’, ‘correo’, telf, ‘nombre’, ‘correo’, telf...
Crea una función que dada una lista en dicho formato y un número n, devuelva todos
los datos del contacto en la posición n'''



'''Ejercicio 9. Crea una función que dada una lista devuelva una lista con dos listas, la
primera que sea la parte izquierda de la lista de entrada y la segunda lista la parte
derecha, e.g.: ej9([1, 2, 3, 4]) devolvería [[1, 2], [3, 4]]'''



'''Ejercicio 10. Crea una función que dada una lista determina si la lista es simétrica, es
decir si se lee de izquierda a derecha que de derecha a izquierda, e.g.: [1, 2, 3, 2, 1] es
una lista simétrica y [3, 6, 9] no lo sería'''