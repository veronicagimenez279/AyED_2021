#-----------------------EJERCICIO 05 - ROMANOS A DECIMALES-----------------------#

def romano_a_decimal (numero):
    """Transforma un número Romano en su equivalente decimal."""
    romanos = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 
		       'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900,'M': 1000}
    if (numero == 'I'):
        return 1
    elif numero in romanos: #si el numero es un valor que existe en el diccionario, devuelve ese valor
        return romanos[numero]
    elif romanos[numero[0]]>=romanos[numero[1]]: #si la letra anterior es mayor a la siguiente solo suma los valores
        return romanos[numero[:1]] + romano_a_decimal(numero[1:])
    else:
        return romanos[numero[:2]] + romano_a_decimal(numero[2:]) #si la letra anterior es menor a la siguiente toma 2 letras


# numero = input('Ingrese el número Romano que desea convertir en decimal: ')
# numero = numero.upper()
# print (numero, 'en decimal es', romano_a_decimal(numero))

#-----------------------EJERCICIO 08 - Nº ENTERO A BINARIO-----------------------#

def conversor_binario (numero):
    """Convierte un número entero en sistema decimal a sistema binario."""
    if (numero <= 0):
        return ('')
    else: 
        return conversor_binario(numero//2) + str(numero % 2)

# n = int(input('Ingrese el numero que desea convertir a binario: '))
# print (n, 'en binario es igual a', conversor_binario(n))

#------------------------EJERCICIO 22 - MOCHILA DEL JEDI-------------------------#

from random import shuffle

def usa_la_fuerza (mochila, pos):
    """Saca los objetos de la mochila hasta encontrar un sable de luz o 
       que se acaben los objetos, y muestra cuantos objetos hizo falta sacar hasta encontrarlo."""
    if pos<len(mochila):
        if (mochila[pos] == 'sable de luz'):
            return pos
        else:
            return usa_la_fuerza (mochila,pos+1)
    else:
        return -1

mochila = ['sable de luz', 'comida', 'capa', 'herramientas', 'comunicador']
shuffle(mochila)

# a = usa_la_fuerza (mochila, 0)

# if (a >= 0):
#     print ('Había un sable de luz en la mochila.')
#     print ('Para encontrarlo hizo falta sacar', a, 'elemento(s).')
# else:
#     print ('No habia un sable de luz en la mochila.')

# print ('Los elementos en la mochila son:')
# for elemento in mochila:
#     print (elemento)


#-----------------------EJERCICIO 23 - SALIDA DEL LABERINTO-----------------------#

def salida_del_laberinto (laberinto, x, y, salida = []):
    """Encuentra una salida del laberinto si esta existe, y muestra el camino."""
    if (x >=0 and x <= len(laberinto)-1) and y>=0 and (y<= len(laberinto[0])-1):
        if x == len(laberinto)-1 and y == len(laberinto[0])-1: #probar con la condicion if (x == len(laberinto)-1 and y == len(laberinto[0]-1)
            salida.append([x, y])
            print ('Llegaste a la salida. El camino tomado fue:')            
            print (salida)

        elif (laberinto[x][y] == 1):
            laberinto[x][y] = '*'
            salida.append([x, y])
            salida_del_laberinto(laberinto, x, y+1,salida)
            salida_del_laberinto(laberinto, x, y-1,salida)
            salida_del_laberinto(laberinto, x+1, y,salida)
            salida_del_laberinto(laberinto, x-1, y,salida)
    
    if ([len(laberinto)-1, len(laberinto[0])-1]) not in salida:
        return False

laberinto =     [[1, 1, 1, 1, 0],
                 [0, 1, 0, 1, 0],
                 [0, 1, 0, 1, 0], 
                 [0, 1, 0, 1, 0],
                 [0, 1, 1, 1, 1]]

# if salida_del_laberinto(laberinto, 0, 0) == False:
#     print ('El laberinto no tiene salida.')
# else:
#     salida_del_laberinto(laberinto, 0, 0)




























# for i in range(len(laberinto)): #range(len(laberinto) = range(0,len(laberinto)
#     print (laberinto[i])

# print (laberinto)

# for i in range(len(laberinto)):
#     for j in range(len(laberinto[i])):
#         print(laberinto[i][j], end='  ')
#     print()

