from basearbol import nodoArbol

# Creamos la raíz del árbol
raiz = nodoArbol(10)

# Insertamos nuevos dataes
raiz.insertar(5)
raiz.insertar(15)
raiz.insertar(2)

# Mostramos los elementos ordenados (recorrido inorden)
print("Elementos ordenados:", raiz.inorden())
print("Elementos en preorden:", raiz.preorden())
print("Elementos en postorden:", raiz.postorden())