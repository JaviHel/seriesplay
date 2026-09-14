class nodoLista():
    """clase nodo lista"""

    info, sig = None, None

class Lista():
    """clase lista enlazada"""

    def __init__(self):
        self.inicio = None
        self.tamanio = 0


def insertar(lista, dato):
    """Insertar el dato pasado en la lista"""
    nodo = nodoLista()
    nodo.info = dato
    if(lista.inicio is None) or (lista.inicio.info>dato):
        nodo.sig = lista.inicio
        lista.inicio = nodo
    else:
        anterior = lista.inicio
        actual = lista.inicio.sig
        while (actual.sig is not None) and (actual.info < dato):
            anterior = anterior.sig
            actual = actual.sig
        nodo.sig = actual
        anterior.sig = nodo
    lista.tamanio += 1

    def lista_vacia(lista):