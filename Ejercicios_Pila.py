from pila import Pila
#!-----------------------//EJERCICIO 14//----------------------------!#
# Realizar un algoritmo que permita ingresar elementos en una pila, y que estos queden ordenados
# de forma creciente. Solo puede utilizar una pila auxiliar como estructura extra –no se
# pueden utilizar métodos de ordenamiento–.

pila_numeros = Pila()
pila_aux = Pila()

datos = [7, 20, 3, 5, 10, 4, 70]


for i in range (0, len(datos)):
    numero = datos[i]

    if (pila_numeros.pila_vacia()):
        pila_numeros.apilar(numero)
    else:
        if (numero >= pila_numeros.elemento_cima()):
            pila_numeros.apilar(numero)
        else:
            while (not pila_numeros.pila_vacia() and pila_numeros.elemento_cima() > numero):
                pila_aux.apilar(pila_numeros.desapilar())
            
            pila_numeros.apilar(numero)
            
            while(not pila_aux.pila_vacia()):
                pila_numeros.apilar(pila_aux.desapilar())


# while(not pila_numeros.pila_vacia()):
#     print(pila_numeros.desapilar())

#!-----------------------//EJERCICIO 16//----------------------------!#
# Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empire
# strikes back” y la otra los del episodio VII “The force awakens”. Desarrollar un algoritmo que
# permita obtener la intersección de ambas pilas, es decir los personajes que aparecen en ambos
# episodios.

pila_empire = Pila()
pila_awakens = Pila()
pila_interseccion = Pila()
pila_aux = Pila()

empire = ['Han Solo', 'Luke Skywalker', 'Leia Organa', 'Lando Calrissian', 'Darth Vader', 
          'Chewbacca', 'Yoda', 'Boba Fett','Obi-Wan Kenobi', 'R2-D2', 'C-3PO']
awakens = ['Rey', 'Finn', 'Poe Dameron' ,'Leia Organa', 'Luke Skywalker', 'Han Solo', 'Kylo Ren',
           'Chewbacca', 'R2-D2', 'C-3PO', 'Maz Kanata']

# shuffle (empire)
# shuffle (awakens)

for elemento in empire:
    pila_empire.apilar(elemento)

for elemento in awakens:
    pila_awakens.apilar(elemento)

while not pila_empire.pila_vacia():
    e = pila_empire.desapilar()
    
    while not pila_awakens.pila_vacia():
        a = pila_awakens.desapilar()
        if (e == a):
            pila_interseccion.apilar(e)
        else:
            pila_aux.apilar(a)

    while not pila_aux.pila_vacia():
        pila_awakens.apilar(pila_aux.desapilar())

# print ('Los personajes que aparecen en ambas películas son:')
# while not pila_interseccion.pila_vacia():
#     print ('-', pila_interseccion.desapilar())

#!-----------------------//EJERCICIO 22//----------------------------!#

# Se recuperaron las bitácoras de las naves del cazarrecompensas Boba Fett y Din Djarin (The
# Mandalorian), las cuales se almacenaban en una pila (en su correspondiente nave) en cada
# misión de caza que emprendió, con la siguiente información: planeta visitado, a quien capturó,
# costo de la recompensa. Resolver las siguientes actividades:
# a. mostrar los planetas visitados en el orden que hicieron las misiones cada uno
# de los cazzarrecompensas;
# b. determinar cuántos créditos galácticos recaudo en total cada cazarrecompensas y de estos
# quien obtuvo mayor fortuna;
# c. determinar el número de la misión –es decir su posición desde el fondo de la pila– en la
# que Boba Fett capturo a Han Solo, suponga que dicha misión está cargada;
# d. indicar la cantidad de capturas realizadas por cada cazarrecompensas.

class Mision (object):

    def __init__(self, planeta, prisionero, recompensa):
        self.planeta = planeta
        self.prisionero = prisionero
        self.recompensa = recompensa

    def __str__(self):
        return self.planeta + ' | ' + self.prisionero +' | '+ str(self.recompensa)

pila_din = Pila()
pila_fett = Pila()
pila_aux = Pila()

datos_din = [('PlanetaD1', 'D. A.', 50000), ('PlanetaD2', 'D. B.', 32000), ('PlanetaD3', 'D. C.', 25000), 
            ('PlanetaD4', 'D. D.', 60000)]
datos_fett = [('PlanetaB1', 'B. A.', 80000),('PlanetaB2', 'B. B.', 75000),('PlanetaB3', 'B. C.', 30000),
            ('PlanetaB4', 'B. D.', 150000),('Tatooine', 'Han Solo', 224190),('PlanetaB6', 'B. F.', 90000)]

for (a,b,c) in datos_din:
    mision = Mision(a, b, c)
    pila_din.apilar(mision)

for (a,b,c) in datos_fett:
    mision = Mision(a, b, c)
    pila_fett.apilar(mision)

total_din = 0
while(not pila_din.pila_vacia()):
    x = pila_din.desapilar()
    pila_aux.apilar(x)
    total_din += x.recompensa

print ('Total de capturas de Din Djarin:', pila_aux.tamanio())
print ('Planetas visitados:')
while (not pila_aux.pila_vacia()):
    x = pila_aux.desapilar()
    print (x.planeta) 

print ()

total_fett = 0
while(not pila_fett.pila_vacia()):
    x = pila_fett.desapilar()
    pila_aux.apilar(x)
    total_fett += x.recompensa
    if x.prisionero == 'Han Solo':
        print ('El número de la mision de captura de Han Solo es', pila_fett.tamanio())

print ('Total de capturas de Boba Fett:', pila_aux.tamanio())
print ('Planetas visitados:')

while (not pila_aux.pila_vacia()):
    x = pila_aux.desapilar()
    print (x.planeta) 

print ()

print ('Total creditos galacticos de Din Djarin:', total_din)
print ('Total creditos galacticos de Boba Fett:', total_fett)

if (total_din>total_fett):
    print ('Din Djarin recaudo mas creditos galacticos.')
elif (total_din<total_fett):
    print ('Boba Fett recaudo mas creditos galacticos.')
else:
    print ('Recaudaron lo mismo.')

#!-----------------------//EJERCICIO 24//----------------------------!#
# Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
# su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
# necesarias para resolver las siguientes actividades:
# a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición
# uno la cima de la pila;
# b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar
# la cantidad de películas en la que aparece;
# c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
# d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.

class Personaje (object):

    def __init__(self, nombre, cant_peliculas):
        self.nombre = nombre
        self.cant_peliculas = cant_peliculas

    def __str__(self):
        return self.nombre + ' - ' + str(self.cant_peliculas) + ' peliculas'

pila_MCU = Pila ()
pila_aux = Pila ()
pila_5 = Pila()
pila_CDG = Pila()

personajes = [('Iron Man', 11),('Captain America', 11),('Groot', 4),('Black Widow', 10),('Thor', 8),
            ('Hulk', 8),('Hawkeye', 5),('Bucky Barnes', 7),('Wanda Maximoff', 5),('Captain Marvel', 2),
            ('Star-Lord', 4),('Rocket Raccoon', 4),('Gamora', 4),('Black Panther', 4)]

for (a,b)  in personajes:
    personaje = Personaje(a,b)
    pila_MCU.apilar(personaje)

while not pila_MCU.pila_vacia():
    x = pila_MCU.desapilar()
    pila_aux.apilar(x)
    if x.nombre == 'Rocket Raccoon' or x.nombre == 'Groot':
        print (x.nombre, 'se encuentra en la posicion', pila_aux.tamanio()) 
    if x.cant_peliculas > 5:
        pila_5.apilar(x)
    if x.nombre == 'Black Widow':
        print ('Black Widow aparecio en', x.cant_peliculas, 'peliculas.')
    if x.nombre[0] == 'C' or x.nombre[0] == 'D' or x.nombre[0] == 'G': 
        pila_CDG.apilar(x)

print()
print ('Personajes que aparecieron en mas de 5 películas:')
while not pila_5.pila_vacia():
    print (pila_5.desapilar())

print()
print ('Personajes cuyo nombre empieza con C, D o G:')
while not pila_CDG.pila_vacia():
    print (pila_CDG.desapilar().nombre)