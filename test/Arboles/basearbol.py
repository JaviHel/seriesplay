from clasenodo import Nodo

class nodoArbol(object):
    #Clase nodo árbol"""

    def __init__(self, dato):
    #Crear un nodo con la información cargada"""
        self.raiz=Nodo(dato)
    
    def __agregar_recursivo(self,nodo,dato):
        if dato < nodo.dato:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.izquierdo, dato)
        else:
            if nodo.derecho is None:
                nodo.derecho = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.derecho, dato)

    def __inorden_recursivo(self,nodo,resultado):
        if nodo is not None:
            self.__inorden_recursivo(nodo.izquierdo,resultado)
            resultado.append(nodo.dato)
            self.__inorden_recursivo(nodo.derecho,resultado)

    def __preorden_recursivo(self,nodo, resultado):
        if nodo is not None:
            resultado.append(nodo.dato)
            self.__preorden_recursivo(nodo.izquierdo, resultado)
            self.__preorden_recursivo(nodo.derecho, resultado)
    
    def __postorden_recursivo(self,nodo,resultado):
        if nodo is not None:
            self.__postorden_recursivo(nodo.izquierdo, resultado)
            self.__postorden_recursivo(nodo.derecho, resultado)
            resultado.append(nodo.dato)

    def __buscar(self,nodo, busqueda):
        if nodo is None:
            return None
        if busqueda == nodo.dato:
            return nodo
        elif busqueda < nodo.dato:
            return self.__buscar(nodo.izquierdo, busqueda)
        else:
            return self.__buscar(nodo.derecho, busqueda)

    def insertar(self, dato):
        self.__agregar_recursivo(self.raiz, dato)


    def inorden(self):
        print("Imprimiendo árbol en orden")
        resultado = []
        self.__inorden_recursivo(self.raiz,resultado)
        print(resultado)
        return len(resultado)

    def preorden(self):
        print("Imprimiendo árbol en preorden")
        resultado = []
        self.__preorden_recursivo(self.raiz,resultado)
        print(resultado)
        return len(resultado)

    def postorden(self):
        print("Imprimiendo árbol en postorden")
        resultado = []
        self.__postorden_recursivo(self.raiz,resultado)
        print(resultado)
        return len(resultado)

    def buscar(self, busqueda):
        return self.__buscar(self.raiz, busqueda)