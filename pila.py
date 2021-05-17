class Pila (object): 

    def __init__(self):
        """Crea una pila vacía."""              
        self.__elementos = []        

    def apilar(self, dato):
        """Apila el dato sobre la cima de la pila."""               
        self.__elementos.append(dato)
    
    def desapilar(self):
        """Desapila el elemento en la cima y lo devuelve."""  
        return self.__elementos.pop() 
    
    def pila_vacia(self):
        """Devuelve True si la pila esta vacía."""  
        return len(self.__elementos)==0

    def tamanio(self):
        """Devuelve el número de elementos en la pila."""
        return len(self.__elementos)
    
    def elemento_cima(self):
        """Devuelve el valor almacenado en la cima de la pila."""
        return self.__elementos[-1] #si fuera 0 seria el elemento del fondo por eso es -1