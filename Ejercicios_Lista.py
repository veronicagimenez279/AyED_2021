from lista import Lista

#!-----------------------//EJERCICIO 06//----------------------------!#
# Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
# casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesarias
# para poder realizar las siguientes actividades:
# a. eliminar el nodo que contiene la información de Linterna Verde;
# b. mostrar el año de aparición de Wolverine;
# c. cambiar la casa de Dr. Strange a Marvel;
# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
# “traje” o “armadura”;
# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
# sea anterior a 1963;
# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
# g. mostrar toda la información de Flash y Star-Lord;
# h. listar los superhéroes que comienzan con la letra B, M y S;
# i. determinar cuántos superhéroes hay de cada casa de comic.

datos = [
    {'nombre':'Wolverine','año_aparicion': 1974, 'editorial' : 'Marvel', 'biografia': 'biografia wolverine'},
    {'nombre':'Dr. Strange','año_aparicion': 1963, 'editorial' : 'MRVL', 'biografia': 'biografia dr. strange'},
    {'nombre':'Linterna Verde','año_aparicion': 1940, 'editorial' : 'DC', 'biografia': 'biografia linterna verde'},
    {'nombre':'Mujer Maravilla','año_aparicion': 1941, 'editorial' : 'DC', 'biografia': 'biografia wonder woman'},
    {'nombre':'Capitana Marvel','año_aparicion': 1967, 'editorial' : 'Marvel', 'biografia': 'biografia cap marvel'},
    {'nombre':'Star-Lord','año_aparicion': 1976, 'editorial' : 'Marvel', 'biografia': 'biografia star lord armadura'},
    {'nombre':'Flash','año_aparicion': 1940, 'editorial' : 'DC', 'biografia': 'biografia flash'},
    {'nombre':'Batman','año_aparicion': 1939, 'editorial' : 'DC', 'biografia': 'biografia batman traje'},
    {'nombre':'Scarlet Witch','año_aparicion': 1964, 'editorial' : 'Marvel', 'biografia': 'biografia scarlet witch'},
    {'nombre':'Starfire','año_aparicion': 1980, 'editorial' : 'DC', 'biografia': 'biografia starfire'},
]

def mostrar_datos (lista, pos):
    print ('Nombre:', lista.obtener_elemento(pos)['nombre'])
    print ('Año de aparición:', lista.obtener_elemento(pos)['año_aparicion'])
    print ('Editorial:', lista.obtener_elemento(pos)['editorial'])
    print ('Biografía:', lista.obtener_elemento(pos)['biografia'])
    print ()

lista_personajes = Lista()

for personaje in datos:
    lista_personajes.insertar(personaje, 'nombre')

# lista_personajes.barrido()
# print()

# a. eliminar el nodo que contiene la información de Linterna Verde;
buscado = lista_personajes.busqueda('Linterna Verde', 'nombre')
if (buscado != -1):
    lista_personajes.eliminar(lista_personajes.obtener_elemento(buscado)['nombre'], 'nombre')

# b. mostrar el año de aparición de Wolverine;
buscado = lista_personajes.busqueda('Wolverine', 'nombre')
if (buscado != -1):
    print('El año de aparicion de Wolverine es: ', lista_personajes.obtener_elemento(buscado)['año_aparicion'])

# c. cambiar la casa de Dr. Strange a Marvel;
buscado = lista_personajes.busqueda('Dr. Strange', 'nombre')
if (buscado != -1):
    lista_personajes.obtener_elemento(buscado)['editorial'] = 'Marvel'

# lista_personajes.barrido()
# print()

# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
# “traje” o “armadura”;

print('Superheroes cuya biografia contiene la palabra "traje" o "armadura":')

for i in range(lista_personajes.tamanio()):
    personaje = lista_personajes.obtener_elemento(i)
    if ('traje' in personaje['biografia']
        or 'armadura' in personaje['biografia']):
        print(personaje['nombre'])
print()

# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
# sea anterior a 1963;

print('Superheores cuya fecha de aparicion es anterior a 1963:')

for i in range (lista_personajes.tamanio()):
    personaje = lista_personajes.obtener_elemento(i)
    if personaje['año_aparicion'] < 1963:
        print(personaje['nombre'], '-', personaje['editorial'])
print()

# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;

def mostrar_casa (lista, personaje):
    """Muestra la editorial del personaje dado."""
    pos = lista.busqueda(personaje, 'nombre')
    if pos != -1:
        print ('La editorial de', personaje, 'es', lista.obtener_elemento(pos)['editorial'])

mostrar_casa(lista_personajes, 'Capitana Marvel')
mostrar_casa(lista_personajes, 'Mujer Maravilla')
print()

# g. mostrar toda la información de Flash y Star-Lord;
buscado = lista_personajes.busqueda('Flash', 'nombre')
if buscado != -1:
    mostrar_datos(lista_personajes, buscado)

buscado = lista_personajes.busqueda('Star-Lord', 'nombre')
if buscado != -1:
    mostrar_datos(lista_personajes, buscado)

# h. listar los superhéroes que comienzan con la letra B, M y S;
# i. determinar cuántos superhéroes hay de cada casa de comic.
cont_Marvel = 0
cont_DC = 0
print('Superheroes cuyo nombre comienza con B, M, o S')
for i in range(lista_personajes.tamanio()):
    personaje = lista_personajes.obtener_elemento(i)
    if (personaje['nombre'][0] == 'B' or personaje['nombre'][0] == 'M' or personaje['nombre'][0] == 'S'):
        print(personaje['nombre'])
    if (personaje['editorial'] == 'Marvel'):
        cont_Marvel += 1
    else:
        cont_DC += 1

print('Cantidad de superheroes de DC:', cont_DC)
print('Cantidad de superheroes de Marvel:', cont_Marvel)

#!-----------------------//EJERCICIO 07//----------------------------!#
# Implementar los algoritmos necesarios para resolver las siguientes tareas:
# a. concatenar dos listas, una atrás de la otra;
# b. concatenar dos listas en una sola omitiendo los datos repetidos y manteniendo su orden;
# c. contar cuántos elementos repetidos hay entre dos listas, es decir la intersección de ambas;
# d. eliminar todos los nodos de una lista de a uno a la vez mostrando su contenido.

lista1 = Lista()
lista2 = Lista()
lista_concatenada = Lista()

for i in range (0,10):
    lista1.insertar(i)

for i in range (0,10):
    lista2.insertar(i*2)

# lista1.barrido()
# print()
# lista2.barrido()
# print()

for i in range (lista1.tamanio()):
    lista_concatenada.insertar(lista1.obtener_elemento(i))
for i in range(lista2.tamanio()):
    lista_concatenada.insertar(lista2.obtener_elemento(i))

print('Listas concatenadas:')
lista_concatenada.barrido()
print()

cont_repetido = 0
for i in range(lista2.tamanio()):
    elemento = lista2.obtener_elemento(i)
    pos = lista1.busqueda(elemento)
    if pos == -1:
        lista1.insertar(elemento)
    else:
        cont_repetido += 1

print('Listas concatenadas sin valores repetidos:')
lista1.barrido()
print()

print('Cantidad de valores repetidos en ambas listas:', cont_repetido)

for i in range(lista1.tamanio()):
    while i < lista1.tamanio():
        print(lista1.eliminar(lista1.obtener_elemento(i)))

#!-----------------------//EJERCICIO 15//----------------------------!#

# Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, cantidad
# de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y además
# la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver
# las siguientes actividades utilizando lista de lista implementando las funciones necesarias:
# a. obtener la cantidad de Pokémons de un determinado entrenador;
# b. listar los entrenadores que hayan ganado más de tres torneos;
# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
# d. mostrar todos los datos de un entrenador y sus Pokémos;
# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
# (tipo y subtipo);
# g. el promedio de nivel de los Pokémons de un determinado entrenador;
# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
# i. mostrar los entrenadores que tienen Pokémons repetidos;
# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion
# o Wingull;
# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
# deberán mostrar los datos de ambos;


entrenadores = Lista()
pokemones = Lista()
entrenadores_79 = Lista() #punto e
lista_tipos = Lista() #punto f 

file = open('entrenadores.txt')
file2 = open('pokemones.txt')

lineas = file.readlines()
lineas.pop(0)

for linea in lineas:
    entrenador = linea.split(';')
    entrenador_data = {}
    entrenador_data['Nombre'] = entrenador[0]
    entrenador_data['Torneos'] = int(entrenador[1])
    entrenador_data['Perdidas'] = int(entrenador[2])
    entrenador_data['Ganadas'] = int(entrenador[3])
    entrenador_data['ID'] = int(entrenador[4].split('\n')[0])
    entrenador_data['Pokemones'] = Lista()
    entrenadores.insertar(entrenador_data, 'Nombre')

lineas = file2.readlines()
lineas.pop(0)

for linea in lineas:
    pokemon = linea.split(';')
    pokemon_data = {}
    pokemon_data['Nombre'] = pokemon[0]
    pokemon_data['Nivel'] = int(pokemon[1])
    pokemon_data['Tipo'] = pokemon[2]
    pokemon_data['Subtipo'] = pokemon[3]
    pokemon_data['ID'] = int(pokemon[4].split('\n')[0])
    pokemones.insertar(pokemon_data, 'ID')

for i in range (entrenadores.tamanio()):
    id_entrenador = entrenadores.obtener_elemento(i)['ID']
    for j in range (pokemones.tamanio()):
        id_pokemon = pokemones.obtener_elemento(j)['ID']
        if (id_entrenador ==  id_pokemon):
            entrenadores.obtener_elemento(i)['Pokemones'].insertar(pokemones.obtener_elemento(j), 'Nombre')

def mostrar_datos (lista, pos):
    """Muestra los datos de los entrenadores y los datos de cada pokemon del entrenador."""
    entrenador = lista.obtener_elemento(pos)
    print('•',entrenador['Nombre'])
    print ('Torneos Ganados:', entrenador['Torneos'], '| Batallas perdidas:', entrenador['Perdidas'], '| Batallas ganadas:', entrenador['Ganadas'] )
    print ('Pokemones:')
    for j in range(0, entrenador['Pokemones'].tamanio()):
        pokemones = lista.obtener_elemento(pos)['Pokemones']
        print(pokemones.obtener_elemento(j)['Nombre'], '| Nivel:', pokemones.obtener_elemento(j)['Nivel'], '| Tipo:', 
        pokemones.obtener_elemento(j)['Tipo'], '| Subtipo:', pokemones.obtener_elemento(j)['Subtipo'])

for i in range (entrenadores.tamanio()):
    mostrar_datos(entrenadores, i)
    print()

# a. obtener la cantidad de Pokémons de un determinado entrenador;
entr = input('Ingrese el nombre del entrenador para saber su cantidad de Pokemon: ').capitalize()
pos = entrenadores.busqueda(entr, 'Nombre')
if pos != -1:
    print ('La cantidad de Pokemon de', entr, 'es:', entrenadores.obtener_elemento(pos)['Pokemones'].tamanio())
print()

may_torneos = entrenadores.obtener_elemento(0)
# b. listar los entrenadores que hayan ganado más de tres torneos;
print('Entrenadores que han ganado mas de 3 torneos:')
for i in range (entrenadores.tamanio()):
    entrenador = entrenadores.obtener_elemento(i)
    poke_lista = entrenador['Pokemones']
    if (entrenador['Torneos']>3):
        print(entrenador['Nombre'],'ha ganado', entrenador['Torneos'], 'torneos.')
    if entrenador['Torneos']>may_torneos['Torneos']:
        may_torneos = entrenador
    if (entrenador['Ganadas']*100//(entrenador['Perdidas']+entrenador['Ganadas']) > 79):
        entrenadores_79.insertar(entrenador, 'Nombre')
    for j in range (poke_lista.tamanio()):
        pokemon = poke_lista.obtener_elemento(j)
        if ((pokemon['Tipo'] == 'Fuego' and pokemon['Subtipo']== 'Planta') or (pokemon['Tipo'] == 'Agua' and pokemon['Subtipo']== 'Volador')):
            lista_tipos.insertar(entrenador, 'Nombre')


print()

# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
poke_lista = may_torneos['Pokemones']
may_nivel = poke_lista.obtener_elemento(0)
for i in range(poke_lista.tamanio()):
    if (poke_lista.obtener_elemento(i)['Nivel'] > may_nivel['Nivel']):
        may_nivel = poke_lista.obtener_elemento(i)

print('El pokemon de mayor nivel de', may_torneos['Nombre'], 'es', may_nivel['Nombre'])
print()

# d. mostrar todos los datos de un entrenador y sus Pokémos;
entr = input('Ingrese el nombre del entrenador para mostrar sus datos y Pokemon: ').capitalize()
pos = entrenadores.busqueda(entr, 'Nombre')
if (pos != -1):
    mostrar_datos(entrenadores, pos)
print()

# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
print('Entrenadores cuyo porcentaje de batallas ganadas es mayor al 79%:')
for i in range(entrenadores_79.tamanio()):
    print(entrenadores_79.obtener_elemento(i)['Nombre'])
print()

# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
# (tipo y subtipo);
print('Entrenadores que tienen Pokemon de tipo fuego/planta o agua/volador:')
for i in range(lista_tipos.tamanio()):
    print(lista_tipos.obtener_elemento(i)['Nombre'])
print()

# g. el promedio de nivel de los Pokémons de un determinado entrenador;
def promedio_nivel (lista_pokemon):
    """Calcula el promedio de nivel de los pokemones en una lista de pokemones dada."""
    total_niveles = 0
    for i in range (lista_pokemon.tamanio()):
        total_niveles += lista_pokemon.obtener_elemento(i)['Nivel']
    return total_niveles/lista_pokemon.tamanio()

entr = input('Ingrese el nombre del entrenador para calcular el promedio de nivel de sus Pokemon: ').capitalize()
pos = entrenadores.busqueda(entr, 'Nombre')
if (pos != -1):
    promedio = round(promedio_nivel(entrenadores.obtener_elemento(pos)['Pokemones']),2)
    print('El promedio de nivel de los Pokemon de', entr, 'es:', promedio)
print()

# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
def entrenadores_pokemon (pokemon, lista):
    """Determina cuantos entrenadores tienen a un determinado pokemon."""
    cantidad_entrenadores = 0
    for i in range (lista.tamanio()):
        pos = lista.obtener_elemento(i)['Pokemones'].busqueda(pokemon, 'Nombre')
        if (pos != -1):
            cantidad_entrenadores += 1
    return cantidad_entrenadores

poke = input('Ingrese el nombre del Pokemon para determinar cuantos entrenadores lo tienen: ').capitalize()
print (entrenadores_pokemon(poke, entrenadores), 'entrenador(es) tiene(n) a', poke)
print()

# i. mostrar los entrenadores que tienen Pokémons repetidos;



# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
print('Los entrenadores que tienen un Tyrantrum, Terrakion o Wingull son:')
for i in range(entrenadores.tamanio()):
    entrenador =  entrenadores.obtener_elemento(i)
    lista_pokemones = entrenador['Pokemones']
    for j in range(lista_pokemones.tamanio()):
        if (lista_pokemones.obtener_elemento(j)['Nombre'] == 'Tyrantrum' or 
            lista_pokemones.obtener_elemento(j)['Nombre'] == 'Terrakion' or 
            lista_pokemones.obtener_elemento(j)['Nombre'] == 'Wingull'):
            print(entrenador['Nombre'])
print()
        
# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
# deberán mostrar los datos de ambos;
ent = input('Ingrese el nombre del entrenador para saber si tiene a un Pokemon: ').capitalize()
pos = entrenadores.busqueda(ent, 'Nombre')
if pos != -1:
    poke = input('Ingrese el nombre del pokemon: ').capitalize()
    pos2 = entrenadores.obtener_elemento(pos)['Pokemones'].busqueda(poke, 'Nombre')
    if pos2 != -1:
        print(ent, 'tiene a', poke)
        entrenador = entrenadores.obtener_elemento(pos)
        print(ent, '| Torneos Ganados:', entrenador['Torneos'], '| Batallas perdidas:', entrenador['Perdidas'], '| Batallas ganadas:', entrenador['Ganadas'])
        pokemon = entrenadores.obtener_elemento(pos)['Pokemones'].obtener_elemento(pos2)
        print (poke, '| Nivel:', pokemon['Nivel'], '| Tipo:', pokemon['Tipo'], '| Subtipo:', pokemon['Subtipo'])
    else:
        print(ent, 'no tiene a', poke)
else:
    print ('No existe entrenador con ese nombre.')

#!-----------------------//EJERCICIO 22//----------------------------!#
# Se dispone de una lista de todos los Jedi, de cada uno de estos se conoce su nombre, maestros,
# colores de sable de luz usados y especie. implementar las funciones necesarias para resolver las
# actividades enumeradas a continuación:
# a. listado ordenado por nombre y por especie;
# b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
# c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
# d. mostrar los Jedi de especie humana y twi'lek;
# e. listar todos los Jedi que comienzan con A;
# f. mostrar los Jedi que usaron sable de luz de más de un color;
# g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
# h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.

lista_jedis = Lista()
lista_especie = Lista()

file = open('jedis.txt', encoding="utf8")
lineas = file.readlines()
lineas.pop(0)
for linea in lineas:
    jedi = linea.split(';')
    jedi_data = {}
    jedi_data['name'] = jedi[0].title()
    jedi_data['rank'] = jedi[1].title()
    jedi_data['species'] = jedi[2]
    jedi_data['master'] = jedi[3].title().split('/')
    jedi_data['lightsaber_color'] = jedi[4].split('/')
    jedi_data['homeworld'] = jedi[5].title()
    jedi_data['birth_year'] = jedi[6]
    jedi_data['height'] = float(jedi[7].split('\n')[0])
    if len(jedi) > 8:
        jedi_data['to_darkside'] = jedi[8]
        jedi_data['come_lightside'] =jedi[9]
    lista_jedis.insertar(jedi_data, 'name')
    lista_especie.insertar(jedi_data, 'species')


# lista_jedis.barrido()

def mostrar_elemento (lista, pos):
    jedi = lista.obtener_elemento(pos)
    print('• Nombre:', jedi['name'], ' | Rango:', jedi['rank'], ' | Especie:', jedi['species'], ' | Maestro(s):', jedi['master'])
    print ('  Color de sable de luz:', jedi['lightsaber_color'], ' | Planeta natal:', jedi['homeworld'], ' | Año de nacimiento:', jedi['birth_year'], ' | Altura:', jedi['height'])


print() 

# a. listado ordenado por nombre y por especie;
# print('Listado ordenado por nombre:')
# for i in range(lista_jedis.tamanio()):
#     mostrar_elemento(lista_jedis, i)

# print()

# print('Listado ordenado por especie:')
# for i in range(lista_especie.tamanio()):
#     mostrar_elemento(lista_especie, i)

# b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
print('Información de Ahsoka Tano y Kit Fisto')
pos = lista_jedis.busqueda('Ahsoka Tano', 'name')
if pos != -1:
    mostrar_elemento(lista_jedis, pos)

pos = lista_jedis.busqueda('Kit Fisto', 'name')
if pos != -1:
    mostrar_elemento(lista_jedis, pos)

# c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
print('Padawans de Luke Skywalker y Yoda:')
for i in range (lista_jedis.tamanio()):
    jedi = lista_jedis.obtener_elemento(i)
    if ('Luke Skywalker' in jedi['master'] or 'Yoda' in jedi['master']):
        print(jedi['name'], '- Master(s):', jedi['master'])
print()

# d. mostrar los Jedi de especie humana y twi'lek;
print("Jedi de especie humana y twi'lek")
for i in range(lista_especie.tamanio()):
    jedi = lista_especie.obtener_elemento(i)
    if (jedi['species']=='human' or jedi['species'] == "twi'lek"):
        mostrar_elemento(lista_especie, i)

print()

# e. listar todos los Jedi que comienzan con A;
print('Jedi que comienzan con A:')
for i in range (lista_jedis.tamanio()):
    jedi = lista_jedis.obtener_elemento(i)
    if jedi['name'][0]=='A':
        print(jedi['name'])
print()

# f. mostrar los Jedi que usaron sable de luz de más de un color;
print('Jedi que usaron sable de mas de un color:')
for i in range (lista_jedis.tamanio()):
    jedi = lista_jedis.obtener_elemento(i)
    if len(jedi['lightsaber_color'])>1:
        print(jedi['name'], ' - Colores:', jedi['lightsaber_color'])
print()

# g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
print('Jedis que usaron un sable de luz amarillo o violeta:')
for i in range (lista_jedis.tamanio()):
    jedi = lista_jedis.obtener_elemento(i)
    if 'yellow' in jedi['lightsaber_color'] or 'purple' in jedi['lightsaber_color']:
        print(jedi['name'])

print()

# h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.
print('Padawans de Qui-Gon Jin y Mace Windu:')
for i in range (lista_jedis.tamanio()):
    jedi = lista_jedis.obtener_elemento(i)
    if ('Qui-Gon Jin' in jedi['master'] or 'Mace Windu' in jedi['master']):
        print(jedi['name'], '- Master(s):', jedi['master'])
print()