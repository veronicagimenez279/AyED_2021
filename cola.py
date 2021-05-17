
class Cola (object):

    def __init__ (self):
        """Crea una cola vacía."""  
        self.__elementos = []

    def arribo (self, dato):
        """Agrega el dato al final de la cola."""
        self.__elementos.append(dato)
    
    def atencion(self):
        """Elimina el elemento en el frente de la cola y lo devuelve."""
        return self.__elementos.pop(0)

    def cola_vacia (self):
        """Devuelve True si la cola esta vacía."""
        return len(self.__elementos) == 0 

    def en_frente (self):
        """Devuelve el valor almacenado en el frente de la cola."""
        return self.__elementos[0]

    def mover_final (self): 
        """Mueve el elemento al frente de la cola al final y devuelve su valor."""
        dato = self.atencion()
        self.arribo(dato)
        return dato
    
    def tamanio (self):
        """Devuelve el número de elementos de la cola."""
        return len (self.__elementos)
    
