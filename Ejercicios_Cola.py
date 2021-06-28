from cola import Cola

#!-----------------------//EJERCICIO 11//----------------------------!#

class Personaje (object):

    def __init__(self, nombre, planeta):
        self.nombre = nombre
        self.planeta = planeta

    def __str__(self):
        return self.nombre + ' - ' + self.planeta

cola_personajes = Cola()
cola_aux = Cola()

personajes = [('Leia Organa', 'Alderaan'),('Luke Skywalker', 'Tatooine'),('Han Solo', 'Cordellia'),
            ('Padmé Amidala', 'Naboo'),('Yoda', 'Desconocido'),('Darth Vader', 'Tatooine'),
            ('Jar Jar Binks', 'Naboo'),('Cara Dune', 'Alderaan'),('Ewoks', 'Endor')]

for (a,b) in personajes:
    personaje = Personaje(a, b)
    cola_personajes.arribo(personaje)
    #print (personaje)


def mostrar_personajes (cola, planeta):
    """Muestra la lista de personajes de un planeta dado."""
    print ('Lista de personajes de', planeta)
    cola_aux = Cola()
    while (not cola.cola_vacia()):
        x = cola.atencion()
        cola_aux.arribo(x)
        if (x.planeta == planeta):
            print (x.nombre)
    while (not cola_aux.cola_vacia()):
        cola.arribo(cola_aux.atencion())

def planeta_natal (cola, personaje):
    """Determina el planeta de origen del personaje dado."""
    cola_aux = Cola()
    while (not cola.cola_vacia()):
        x = cola.atencion()
        cola_aux.arribo(x)
        if (x.nombre == personaje):
            print ('El planeta natal de', personaje, 'es', x.planeta)
    while (not cola_aux.cola_vacia()):
        cola.arribo(cola_aux.atencion())

def insertar_personaje_antes (cola, personaje1, personaje2):
    """Inserta el personaje2 en la posicion anterior al personaje1 en la cola."""
    cola_aux = Cola()
    while (not cola.cola_vacia()):
        x = cola.atencion()
        if (x.nombre==personaje1):
            cola_aux.arribo(personaje2)
        cola_aux.arribo(x)
    
    while (not cola.cola_vacia()):
        cola_aux.arribo(cola.atencion())
    while (not cola_aux.cola_vacia()):
        cola.arribo(cola_aux.atencion())

def eliminar_personaje_despues (cola, personaje):
    """Elimina al personaje en la posicion posterior al ingresado."""
    cola_aux = Cola()
    while (not cola.cola_vacia()):
        x = cola.atencion()
        cola_aux.arribo(x)
        if (x.nombre==personaje):
            break
    cola.atencion()
    while (not cola.cola_vacia()):
        cola_aux.arribo(cola.atencion())
    while (not cola_aux.cola_vacia()):
        cola.arribo(cola_aux.atencion())

# a. mostrar los personajes del planeta Alderaan, Endor y Tatooine

mostrar_personajes(cola_personajes, 'Alderaan')
print ()
mostrar_personajes(cola_personajes, 'Endor')
print ()
mostrar_personajes(cola_personajes, 'Tatooine')
print ()

# b. indicar el planeta natal de Luke Skywalker y Han Solo

planeta_natal(cola_personajes, 'Luke Skywalker')
planeta_natal(cola_personajes, 'Han Solo')
print ()

# c. insertar un nuevo personaje antes del maestro Yoda

personaje2 = Personaje ('Rey', 'Jakku')
insertar_personaje_antes(cola_personajes, 'Yoda', personaje2)


# d. eliminar el personaje ubicado después de Jar Jar Binks

eliminar_personaje_despues(cola_personajes, 'Jar Jar Binks')


while not cola_personajes.cola_vacia():
    print (cola_personajes.atencion())

#!-----------------------//EJERCICIO 12//----------------------------!#
# Dada dos colas con valores ordenadas, realizar un algoritmo que permita combinarlas en una
# nueva cola. Se deben mantener ordenados los valores sin utilizar ninguna estructura auxiliar,
# ni métodos de ordenamiento.

cola1 = Cola()
cola2 = Cola()
cola3 = Cola()

datos1 = [2, 3, 9, 12, 40, 45, 46, 47, 48, 50]
datos2 = [1, 4, 5, 6, 7, 11, 35, 36, 37, 38, 50, 51, 89, 90]


for elemento in datos1:
    cola1.arribo(elemento)
    
for elemento in datos2:
    cola2.arribo(elemento)

while not cola1.cola_vacia():
    x = cola1.atencion()
    while not cola2.cola_vacia():
        if cola2.en_frente() <= x:
            cola3.arribo(cola2.atencion())
        else:
            break
    cola3.arribo(x)

while not cola2.cola_vacia(): #para cuando la segunda cola tiene mas elementos que la primera
    cola3.arribo(cola2.atencion())

while not cola3.cola_vacia():
    print (cola3.atencion())


#!-----------------------//EJERCICIO 22//----------------------------!#
# 22. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce
# el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino
# F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff,
# Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:
# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
# b. mostrar los nombre de los superhéroes femeninos;
# c. mostrar los nombres de los personajes masculinos;
# d. determinar el nombre del superhéroe del personaje Scott Lang;
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
# con la letra S;
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
# de superhéroes.

class Personaje (object):

    def __init__(self, nombre, alter_ego, genero):
        self.nombre = nombre
        self.alter_ego = alter_ego
        self.genero = genero

    def __str__(self):
        return self.nombre + ' - ' + self.alter_ego + ' - ' + self.genero

cola_personajes = Cola()
cola_F = Cola()
cola_M = Cola()
cola_S = Cola()

personajes = [ ('Tony Stark','Iron Man','M'),('Steve Rogers','Captain America','M'),('Natasha Romanoff','Black Widow','F'),
            ('Wanda Maximoff','Scarlet Witch','F'),('Clint Barton','Hawkeye','M'),('Bruce Banner','Hulk','M'),
            ('Carol Danvers','Captain Marvel','F'),('Hope Van Dyne','The Wasp','F'),('Scott Lang','Ant-Man','M'),
            ('Thor Odinson','Thor','M'),("T'challa",'Black Panther','M'),('Pepper Potts','Rescue','F'),
            ('Peter Parker','Spider-Man','M'),('Gamora','Gamora','F')]


for (a,b,c) in personajes:
    personaje = Personaje(a, b, c)
    cola_personajes.arribo(personaje)

while not cola_personajes.cola_vacia():
    x = cola_personajes.atencion()
    if (x.alter_ego == 'Captain Marvel'):
        print ('El nombre de', x.alter_ego, 'es', x.nombre)
    if (x.nombre == 'Scott Lang'):
        print ('El nombre de superhéroe de', x.nombre, 'es', x.alter_ego)
    if (x.nombre == 'Carol Danvers'):
        print (x.nombre, 'se encuentra en la cola y su nombre de superhéroe es', x.alter_ego)
    if (x.nombre[0]=='S' or x.alter_ego[0]=='S'):
        cola_S.arribo(x)
    if (x.genero == 'F'):
        cola_F.arribo(x)
    else:
        cola_M.arribo(x) 

print()
print ('Nombres de los superhéroes femeninos:')
while (not cola_F.cola_vacia()):
    print (cola_F.atencion().alter_ego)

print()

print ('Nombres de los personajes masculinos:')
while (not cola_M.cola_vacia()):
    print (cola_M.atencion().nombre)

print()

print ('Personajes cuyos nombres empiezan con S:')
while (not cola_S.cola_vacia()):
    print (cola_S.atencion())