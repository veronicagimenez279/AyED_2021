def __criterio (self, dato, criterio):
    if (criterio == None):
        return dato
    else:
        return dato[criterio]

def quicksort(vector, inicio, fin, criterio):
    primero = inicio
    ultimo = fin -1
    pivote = fin
    while(primero < ultimo):
        while(__criterio(vector[primero], criterio) <= __criterio(vector[pivote], criterio) and primero <= ultimo):
            primero += 1
        while(__criterio(vector[ultimo], criterio) > __criterio(vector[pivote], criterio) and ultimo >= primero):
            ultimo -= 1
        if(primero < ultimo):
            vector[primero], vector[ultimo] = vector[ultimo], vector[primero]
    if(__criterio(vector[pivote], criterio) < __criterio(vector[primero], criterio)):
        vector[primero], vector[pivote] = vector[pivote], vector[primero]

    if(inicio < primero):
        quicksort(vector, inicio, primero -1, criterio)
    if(fin > primero):
        quicksort(vector, primero + 1, fin, criterio)

class Lista (object): 
    """Crea un objeto tipo lista"""

    def __init__(self):
        self.__elementos = []

    def __criterio (self, dato, criterio):
        if (criterio == None):
            return dato
        else:
            return dato[criterio]

    def insertar (self, dato, criterio = None): 
        """Inserta el dado dado en la lista de manera ordenada."""
        if (len(self.__elementos) == 0):
            self.__elementos.append(dato)
        elif (self.__criterio(dato,criterio) < self.__criterio(self.__elementos[0], criterio)): 
            self.__elementos.insert(0, dato)
        else:
            pos = 0
            while (pos < len(self.__elementos) and self.__criterio(dato,criterio) >= self.__criterio(self.__elementos[pos], criterio)):
                pos += 1
            self.__elementos.insert (pos, dato)

    def eliminar(self, dato, criterio=None, clave=None, criterio_clave=None):
        """Elimina un elemento de la lista luego de buscarlo y lo devuelve si lo encuentra.
        eliminar(dato a eliminar, que dato es, dato clave, que dato es el clave)"""
        pos = self.busqueda(dato, criterio, clave, criterio_clave)
        if(pos != -1):
            return self.__elementos.pop(pos)
        else:
            return None

    def modificar_elemento(self, pos, nuevo_valor, criterio = None):
        """Se utiliza cuando se quiere cambiar el campo clave."""
        if (pos < self.tamanio()):
            self.__elementos.pop(pos)
            self.insertar(nuevo_valor, criterio)
    
    def busqueda (self, buscado, criterio = None, clave = None, criterio_clave = None): 
        """Devuelve la posicion del elemento buscado
        lista_personas.busqueda(buscado, que dato es, dato clave buscado, que dato es el clave)"""
        pos = -1
        primero = 0
        ultimo = len(self.__elementos) -1
        while (primero <= ultimo and pos == -1):
            medio = (primero + ultimo) // 2
            if (self.__criterio(self.__elementos[medio], criterio) == buscado):
                pos = medio
            elif (self.__criterio(self.__elementos[medio], criterio) > buscado):
                ultimo = medio - 1
            else:
                primero = medio + 1
        # si pos =! 1 significa que lo encontre
        # si clave is not None pregunta si tiene una clave, si no la tiene es un dato simple y el que encontre es el que quiero eliminar
        # y chequeo que el elemento encontrado sea igual al campo que estoy buscando 
        if (pos != -1 and clave is not None and self.__elementos[pos][criterio_clave] != clave):
            #este while busca el primer elemento de los repetidos
            while (self.__criterio(self.__elementos[pos], criterio) == self.__criterio(self.__elementos[pos-1], criterio)):
                pos -= 1
            while (self.__elementos[pos][criterio_clave] != clave and 
                self.__criterio(self.__elementos[pos], criterio) == self.__criterio(self.__elementos[pos+1], criterio)):
                pos += 1
            if (self.__elementos[pos][criterio_clave] != clave):
                pos = -1
        
        return pos

    def obtener_elemento (self, pos):
        """Devuelve el elemento que se encuentra en una posicion dada."""
        if (pos >= 0):
            return self.__elementos[pos]
        else:
            return None

    def lista_vacia (self):
        """Devuelve true si la lista esta vacia."""
        return len(self.__elementos == 0)

    def tamanio (self):
        """Devuelve el tamaño de la lista."""
        return len(self.__elementos)

    def barrido (self): 
        """Realiza un barrido de los elementos de la lista."""
        for elemento in self.__elementos:
            print (elemento)
    
    def barrido_lista_autos (self): 
        for elemento in self.__elementos:
            print (elemento)
            print ('autos:')
            elementos['autos'].barrido()

    def barrido_alumnos (self):
        for elemento in self.__elementos:
            print (elemento)
            print ('parciales:')
            elemento['Parciales'].barrido()

    def barrido_eliminar (self, datos_eliminar):
        for elemento in self.__elementos:
            if (elemento in datos_eliminar):
                self.__elementos.remove(elemento)

    def ordenar (self, criterio):
        quicksort(self.__elementos, 0, len(self.__elementos)-1, criterio)

