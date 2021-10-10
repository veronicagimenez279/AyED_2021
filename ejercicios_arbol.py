from arbol_binario import Arbol

#! -------------------------- // EJERCICIO 05 // -------------------------- !#
# 5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe
# (MCU), desarrollar un algoritmo que contemple lo siguiente:
# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano
# que indica si es un héroe o un villano, True y False respectivamente;
# b. listar los villanos ordenados alfabéticamente;
# c. mostrar todos los superhéroes que empiezan con C;
# d. determinar cuántos superhéroes hay el árbol;
# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para 
# encontrarlo en el árbol y modificar su nombre;
# f. listar los superhéroes ordenados de manera descendente;
# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:
# I. determinar cuántos nodos tiene cada árbol;
# II. realizar un barrido ordenado alfabéticamente de cada árbol.

datos = [
    {'nombre':'Iron Man', 'heroe': True},
    {'nombre':'Thanos', 'heroe': False},
    {'nombre':'Kang', 'heroe': False},
    {'nombre':'Captain Marvel', 'heroe': True},
    {'nombre':'Agatha Harkness', 'heroe': False},
    {'nombre':'Captain America', 'heroe': True},
    {'nombre':'Taneleer Tivan', 'heroe': False},
    {'nombre':'Black Widow', 'heroe': True},
    {'nombre':'Doctor Strnge', 'heroe': True},
    {'nombre':'Scarlet Witch', 'heroe': True},
    {'nombre':'Ravonna Renslayer', 'heroe': False},
]

arbol = Arbol()

for personaje in datos:
    arbol = arbol.insertar_nodo(personaje['nombre'], personaje) # por el arbol avl

# arbol.preorden()

#! ---- PUNTO B ----!#
print('Villanos ordenados alfabeticamente:')
arbol.inorden_villanos()
print()

#! ---- PUNTO C ----!#
print('Superheroes que empiezan con C')
arbol.inorden_heroes_C()
print()

#! ---- PUNTO D ----!#
print('En el arbol hay', arbol.contar_nodos(True), 'heroes.')
print()

#! ---- PUNTO E ----!#
buscado = input('Comience a escribir el nombre del personaje que desea cambiar: ')
arbol.busqueda_proximidad(buscado)
buscado = input('Ingrese el nombre completo del personaje que desea cambiar de la lista anterior: ')
pos = arbol.busqueda(buscado)
if (pos):
    nuevo_nombre = input('Ingrese el nuevo nombre: ')
    nombre, superheroe = arbol.eliminar_nodo(buscado)
    superheroe['nombre'] = nuevo_nombre
    arbol = arbol.insertar_nodo(nuevo_nombre, superheroe)
print()
# arbol.inorden()

#! ---- PUNTO F ----!#
print('Superheroes ordenados de manera descendente:')
arbol.postorden_heroes()
print()

#! ---- PUNTO G ----!#

arbol_heroes = Arbol()
arbol_villanos = Arbol()

arbol_heroes = arbol.separar_arbol(arbol_heroes, True)
print('Arbol de superheroes:')
arbol_heroes.inorden()
print('El arbol de superheroes tiene', arbol_heroes.contar_nodos(True), 'nodos.')
print()

arbol_villanos = arbol.separar_arbol(arbol_villanos, False)
print('Arbol de villanos:')
arbol_villanos.inorden()
print('El arbol de villanos tiene', arbol_villanos.contar_nodos(False), 'nodos.')
print()


#! -------------------------- // EJERCICIO 16 // -------------------------- !#
# Una empresa de nano satélites dedicada al monitoreo de lotes campo destinados al agro, tiene
# problemas para la transmisión de los datos recolectados, dado que la ventana de tiempo que
# dispone para enviar los datos antes de una nueva medición es muy corta, por lo que nos solicita
# desarrollar un algoritmo que permita comprimir la información para poder enviarla más rápido,
# para lo cual se debe tener en cuenta los siguientes requerimientos:
# a. la información transmitida por el nano satélite son estado del tiempo, humedad del suelo,
# y tres dígitos que identifican el lote al cual pertenecen los datos;
# b. desarrollar un árbol de Huffman que permita comprimir la información para transmitirla,
# la frecuencia de la información transmitida se observa en la tabla
# c. comprimir un mensaje y descomprimirlo, para ver si no se pierde información durante el
# proceso de codificación, la trama enviada por el nano satélite tiene el siguiente formato
# (estado del clima-humedad del suelo-cod1-cod2-cod3), por ejemplo la siguiente trama es
# válida “Nublado-Baja-1-5-7”, –los guiones son a fines de comprender como está formada la
# trama pero no forman parte de la misma–;
# d. determinar la diferencia en tamaño de memoria utilizada por la trama original y la trama
# comprimida –
# puede utilizar la función getsizeof() de la librería sys–.

arbol = Arbol()

tabla = [['Despejado', 0.22], ['Nublado', 0.15], ['Lluvia', 0.03],['Baja', 0.26],['Alta', 0.14], ['1', 0.05], ['2', 0.01], ['3', 0.035], ['5', 0.06], ['7', 0.02], ['8', 0.025]]
dic  = {}


def como_comparo (arbol):
    return arbol.datos

bosque = []

for info, frecuencia in tabla:
    arbol = Arbol(info, frecuencia)
    bosque.append(arbol)

bosque.sort(key=como_comparo)

# for arbol in bosque:
#     print (arbol.info, arbol.datos)

while (len(bosque)>1):
    arbol1 = bosque.pop(0)
    arbol2 = bosque.pop(0)
    nuevo_arbol = Arbol(datos=arbol1.datos+arbol2.datos)
    nuevo_arbol.izq = arbol1
    nuevo_arbol.der = arbol2
    bosque.append(nuevo_arbol)
    bosque.sort(key=como_comparo) 

arbol_huffman = bosque[0]

def generar_tabla (arbol, cadena = '', dic = None):
    if (arbol is not None):
        if (arbol.izq is None):
            dic[arbol.info] = cadena
            # print(arbol.info, cadena)
        else:
            cadena += '0'
            generar_tabla (arbol.izq,cadena, dic)
            cadena = cadena [0:-1]
            cadena += '1'
            generar_tabla(arbol.der,cadena, dic)

generar_tabla(arbol_huffman, dic=dic)

import re
def codificar (cadena, dic):
    cadena_cod = ''
    palabras_lista = re.findall('[A-Z][^A-Z]*', re.findall('[a-zA-Z]+', cadena)[0])
    numeros_lista = [int(digito) for digito in (re.findall('\d+', cadena)[0])]

    lista = []
    for elemento in palabras_lista: 
        lista.append(elemento)
    for elemento in numeros_lista:
        lista.append(str(elemento))

    for caracter in lista:
        cadena_cod += dic[caracter]
    return cadena_cod

def decodificar (cadena_cod, arbol_huff):
    cadena_deco = ''
    arbol_aux = arbol_huff
    pos = 0
    while (pos < len(cadena_cod)):
        if (cadena_cod[pos] == '0'):
            arbol_aux = arbol_aux.izq
        else:
            arbol_aux = arbol_aux.der
        pos += 1
        if (arbol_aux.izq is None):
            cadena_deco += arbol_aux.info
            arbol_aux = arbol_huff
    return cadena_deco

# #! ---- PUNTO C ----!#
cadena = "NubladoBaja157"
cadena_cod = codificar(cadena, dic)
print (cadena, 'codificada:', cadena_cod)
print(cadena_cod, 'decodificada:', decodificar(cadena_cod, arbol_huffman))
print()

# #! ---- PUNTO D ----!#
# from sys import getsizeof
# print('Tamaño de',cadena, ':', getsizeof(cadena))
# print('Tamaño de', cadena_cod, ':', getsizeof(b'1111001000110011101'))


#! -------------------------- // EJERCICIO 23 // -------------------------- !#
# Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
# resuelva las siguientes consultas:
# a. listado inorden de las criaturas y quienes la derrotaron;
# b. se debe permitir cargar una breve descripción sobre cada criatura;
# c. mostrar toda la información de la criatura Talos;
# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
# e. listar las criaturas derrotadas por Heracles;
# f. listar las criaturas que no han sido derrotadas;
# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
# o dios que la capturo;
# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
# Erimanto indicando que Heracles las atrapó;
# i. se debe permitir búsquedas por coincidencia;
# j. eliminar al Basilisco y a las Sirenas;
# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
# derroto a varias;
# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
# m. realizar un listado por nivel del árbol;
# n. muestre las criaturas capturadas por Heracles.

datos = [ 
    {'nombre' : 'Ceto', 'capturada' : '', 'descripcion' : ''},
    {'nombre' : 'Cerda de Cromión', 'capturada' : 'Teseo', 'descripcion' : ''},
    {'nombre' : 'Tifón', 'capturada' : 'Zeus', 'descripcion' : ''}, 
    {'nombre' : 'Ortro', 'capturada' : 'Heracles', 'descripcion' : ''},
    {'nombre' : 'Equidna', 'capturada' : 'Argos Panoptes', 'descripcion' : ''}, 
    {'nombre' : 'Toro de Creta', 'capturada' : 'Teseo', 'descripcion' : ''},
    {'nombre' : 'Dino', 'capturada' : '', 'descripcion' : ''}, 
    {'nombre' : 'Jabalí de Calidón', 'capturada' : 'Atalanta', 'descripcion' : ''},
    {'nombre' : 'Pefredo', 'capturada' : '', 'descripcion' : ''},
    {'nombre' : 'Carcinos', 'capturada' : '', 'descripcion' : ''},
    {'nombre' : 'Enio', 'capturada' : '', 'descripcion' : ''},
    {'nombre' : 'Gerión', 'capturada' : 'Heracles', 'descripcion' : ''},
    {'nombre' : 'Escila', 'capturada' : '', 'descripcion' : ''},
    {'nombre' : 'Cloto', 'capturada' : '', 'descripcion' : ''},
    {'nombre' : 'Caribdis', 'capturada' : '', 'descripcion' : ''},
    {'nombre' : 'Laquesis', 'capturada' : '', 'descripcion' : ''},
    {'nombre' : 'Euríale', 'capturada' : '', 'descripcion' : ''},
    {'nombre' : 'Atropos', 'capturada' : '', 'descripcion' : ''},
    {'nombre' : 'Esteno', 'capturada' : '', 'descripcion' : ''},
    {'nombre' : 'Minotauro de Creta', 'capturada' : 'Teseo', 'descripcion' : ''},
    {'nombre' : 'Medusa', 'capturada' : 'Perseo', 'descripcion' : ''},
    {'nombre' : 'Harpías', 'capturada' : '', 'descripcion' : ''},
    {'nombre' : 'Ladón', 'capturada' : 'Heracles', 'descripcion' : ''},
    {'nombre' : 'Argos Panoptes', 'capturada' : 'Hermes', 'descripcion' : ''},
    {'nombre' : 'Aguila del Cáucaso', 'capturada' : '', 'descripcion' : ''},
    {'nombre' : 'Aves del Estínfalo', 'capturada' : '', 'descripcion' : ''},
    {'nombre' : 'Quimera', 'capturada' : 'Belerofonte', 'descripcion' : ''},
    {'nombre' : 'Talos', 'capturada' : 'Medea', 'descripcion' : ''},
    {'nombre' : 'Hidra de Lerna', 'capturada' : 'Heracles', 'descripcion' : ''},
    {'nombre' : 'Sirenas', 'capturada' : '', 'descripcion' : ''},
    {'nombre' : 'León de Nemea', 'capturada' : 'Heracles', 'descripcion' : ''},
    {'nombre' : 'Pitón', 'capturada' : 'Apolo', 'descripcion' : ''},
    {'nombre' : 'Esfinge', 'capturada' : 'Edipo', 'descripcion' : ''},
    {'nombre' : 'Cierva de Cerinea', 'capturada' : '', 'descripcion' : ''},
    {'nombre' : 'Dragón de la Cólquida', 'capturada' : '', 'descripcion' : ''},
    {'nombre' : 'Basilisco', 'capturada' : '', 'descripcion' : ''},
    {'nombre' : 'Cerbero', 'capturada' : '', 'descripcion' : ''},
    {'nombre' : 'Jabalí de Erimanto', 'capturada' : '', 'descripcion' : ''} 
]

arbol_criaturas = Arbol()

for criatura in datos:
    arbol_criaturas = arbol_criaturas.insertar_nodo(criatura['nombre'], criatura) 


# # arbol_criaturas.inorden()

#! ---- PUNTO A ----!#
arbol_criaturas.inorden_criaturas()
print()

#! ---- PUNTO B ----!#
criatura = input('Ingrese una criatura para agregarle una breve descripcion: ')
arbol_criaturas.cargar_descripcion(criatura)
print()
# arbol_criaturas.inorden()

#! ---- PUNTO C ----!#
print('Informacion de la criatura Talos:')
arbol_criaturas.mostrar_informacion('Talos')
print()

#! ---- PUNTO D ----!#
def ordenar(elemento):
    return elemento[1]

dic = {}
arbol_criaturas.contador_criaturas_derrotadas(dic)
lista = list(dic.items())
lista.sort(key=ordenar, reverse=True)

print('Los 3 heroes o dioses que derrotaron a la mayor cantidad de criaturas son:')
for i in range (3):
	print(lista[i][0], '(derroto a',  lista[i][1], 'criatura(s))')
print()


#! ---- PUNTO E ----!#
print('Lista de criaturas derrotadas por Heracles:')
arbol_criaturas.criaturas_derrotadas('Heracles')
print()

#! ---- PUNTO F ----!#
print('Lista de criaturas que no han sido derrotadas:')
arbol_criaturas.criaturas_no_derrotadas()
print()

#! ---- PUNTO H ----!#
arbol_criaturas.modificar_captura('Cerbero', 'Heracles')
arbol_criaturas.modificar_captura('Toro de Creta', 'Heracles')
arbol_criaturas.modificar_captura('Cierva de Cerinea', 'Heracles')
arbol_criaturas.modificar_captura('Jabalí de Erimanto', 'Heracles')
print()
# arbol_criaturas.inorden_criaturas()

#! ---- PUNTO I ----!#
clave = input('Comience a escribir parte del nombre de una criatura para buscarla: ')
print('Criaturas que contienen "', clave, '" en su nombre:' )
arbol_criaturas.busqueda_por_coincidencia(clave)
print()

#! ---- PUNTO J ----!#
info, datos = arbol_criaturas.eliminar_nodo('Basilisco')
print (info, 'ha sido eliminado')
info, datos = arbol_criaturas.eliminar_nodo('Sirenas')
print (info, 'ha sido eliminado')
print()
# arbol_criaturas.inorden_criaturas()

#! ---- PUNTO K ----!#
pos = arbol_criaturas.busqueda('Aves del Estínfalo')
if (pos):
    pos.datos['capturada'] = 'Heracles'
    pos.datos['descripcion'] = 'Heracles derrotó a varias.'
# arbol_criaturas.inorden_criaturas()

#! ---- PUNTO L ----!#
pos = arbol_criaturas.busqueda('Ladón')
if (pos):
    nombre, datos = arbol_criaturas.eliminar_nodo('Ladón')
    datos['nombre'] = 'Dragón Ladón'
    arbol_criaturas = arbol_criaturas.insertar_nodo('Dragón Ladón', datos)

# arbol_criaturas.inorden_criaturas()

#! ---- PUNTO M ----!#
print('Barrido por nivel del arbol:')
arbol_criaturas.barrido_por_nivel()
print()


#! ---- PUNTO N ----!#
print('Lista de criaturas capturadas por Heracles:')
arbol_criaturas.criaturas_derrotadas('Heracles')
print()