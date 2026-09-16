import random, time
from carga_de_datos import *
from ascii_frame import *



# MAIN SETUP
DATA = cargar_json("datos/dataset_100.json")# IMPLEMENTAR PATHLIB
LOOP = True
WIDTH = 60
af = AsciiFrame(WIDTH)




# JSON RECORDATORIO
"""
{
"title": "Family Guy",
"genre": "Animation",
"year": 1999,
"popularity_metrics": 79,
"episode_duration_average": 22,
"seasons": 23,
"episodes": 430,
"age_rating": "TV-14",
"is_finished": false
}
"""






# FUNCIONES DE IMPRESION EN PANTALLA
def print_wrapped_text(text, indent="c", separator=" "):
    """ Imprime Texto Dentro De Una Caja ASCII """
    af.print_box("t")
    af.print_text(text, indent, separator)
    af.print_box("b")


def print_wrapped_screen(lst):
    af.print_box("t")
    for i, option in enumerate(lst):
        af.print_text(f"[{i+1}]>" + option)
    af.print_box("b")





# FUNCIONES UTILES PARA EL RESTO DE OPCIONES
def filter_by(user_input:str, option:str):
    """ Filtra series por una opcion de manera lineal:
        title, genre, duration, etc...
    """
    for serie in DATA["series"]:
        if user_input.lower() == serie[option].lower():
            return True
    return False


def select_by(user_input:str, option:str):
    """" Retorna una lista con los nombres de series que tienen una opcion en comun. """
    lst = []
    for serie in DATA["series"]:
        if user_input.lower() == serie[option].lower():
            lst.append(serie)
    return lst
    
    
def get_random_option(option="title"): 
    """ Retorna una serie aleatoria de a la lista
        option es el tipo de dato aleatorio que quermos que retorne
        "title" por default
    """
    return random.choice(DATA["series"])[option]
    
    
def exit():
    global LOOP
    LOOP = False







# IMPRIMIR FUNCIONALIDAD DE LAS OPCIONES DE LA PANTALLA PRINCIPAL
#1
def search_series():
    """ Imprime si la serie ingresada por el usuario esta en la base de datos """
    # HAY QUE DARLE ESTILO A ESTO
    name = ask_user("INGRESE EL NOMBRE DE LA SERIE (en ingles): ")
    
#    print("buscando serie... ")

    if filter_by(name, "title"):
        print_wrapped_text(f'La serie "{name}" SI se encuentra disponible.')
    else:
        print_wrapped_text(f'La serie "{name}" NO se encuentra disponible.')

    exit()



#2
def recommend_related():
    """ Recomienda una serie relacionada a la serie ingresada por el usuario """
    name = ask_user("INGRESE EL NOMBRE UNA SERIE QUE LE GUSTE (en ingles): ")
    print("NO IMPLEMENTADO AUN :(")
    exit()



#3
def recommend_random():
    name = get_random_option()
    print("recomendando serie aleatoria...")
    
    af.print_box("t")
    af.print_text('TE RECOMIENDO QUE MIRES:', "c")
    af.print_text(f'"{name}"', "c")
    af.print_text('¡ESTA MUY BUENA!', "c")
    af.print_box("b")
    exit()
    
    
    
#4
def filter_by_genre():
    """ Imprime las series del genero ingresado por el usuario """
    print('Ejemplo de generos: "Talk", "Horror", "Comedy", "Crime", etc...')
        
    genre = ask_user("INGRESE EL NOMBRE DEL GENERO (en ingles): ")
    lst = select_by(genre, "genre")
    
#    print("filtrando por generos...")
    
    if len(lst) > 0:
        af.print_box("t")
        af.print_text(f'Se encontraron estas series del genero "{genre}"'.upper(), "c",)
        af.print_space("-")
        [af.print_text(f"[{i+1}]>" + serie["title"]) for i, serie in enumerate(lst)]
        af.print_box("b")
    else:
        print_wrapped_text(f'No se encontro el genero "{genre}"'.upper())
    
    exit()



#5
def filter_by_seasons():
    """ Imprime las series que tienen menos o igual cantidad de temporadas
        que la ingresada por el usuario
    """
    print("NO IMPLEMENTADO AUN :(")
    exit()



#6
def filter_by_episode_duration():
    """ Imprime las series con menos duracion promedio de episodio
        el usuario debe ingresar la duracion promedio de una lista en pantalla
    """
    print("NO IMPLEMENTADO AUN :(")
    exit()



#7
def filter_by_age_rating():
    """ Imprime las peliculas que son aptas para cierto publico
        el usuario ingresa la opcion de edad de una lista en pantalla
    """
    print("NO IMPLEMENTADO AUN :(")
    exit()






# FUNCIONES DE INPUT Y SELECCION
def ask_user(message="text", type_str=True):
    """ Imprime el mensaje en pantalla para que el usuario vea
        
    """
    if type_str:
        return input(message)
    return int(input(message))


def select_option(user_input:int, method_call_lst:list):
    """ Dependiendo de lo que el usuario ingrese va a llamar a la opcion correcta 
        method_call_lst es una lista con funciones(sin parentesis) que seran ejecutadas aqui
        segun corresponda.
    """    
    # Solo llama a la funcion si el usuario ingresa un nro mayor que 0 y menor/igual al tamaño de la lista
    if 0 < user_input <= len(method_call_lst):
        method_call_lst[user_input-1]()    
    else:  
        print("ESA NO ES UNA OPCION DE LA LISTA")







############################# IMPORTANTE ############################# 

# CUANDO TERMINAMOS DE CONSTRUIR LA FUNCION *MAIN* AL FINAL,
# LA MOVEMOS A UN ARCHIVO *MAIN* EN LA CARPETA PRINCIPAL DEL PROYECTO

############################# IMPORTANTE ############################# 

def main():
    # Estas variables y titulos deberian ir cada una dentro de una funcion
    # Variables de los titulos y opciones de cada pantalla
    MAIN_SCREEN_MESSAGE = "SELECCIONE UNA OPCION DEL MENU: " # mensaje al usuario #1
    MAIN_SCREEN_TITLE = "🎞 SERIESPLAY 🎞"
    # Creamos un diccionario que lo guardamos en una variable con su respectivo NOMBRE_OPTIONS
    # en el cual la "clave" es lo que se imprime en pantalla
    # y el "valor" es la funcion a llamar(sin parentesis, solo el nombre de la funcion)
    MAIN_SCREEN_OPTIONS = {"Buscar Series": search_series,
                           "Recomendar Serie Relacionada": recommend_related, # Implementar mas adelante
                           "Recomendar Serie Aleatoria": recommend_random,
                           "Filtrar Por Genero": filter_by_genre,
                           "Filtrar Por Cantidad De Temporadas": filter_by_seasons,
                           "Filtrar Por Duracion De Capitulo": filter_by_episode_duration,
                           "Filtrar Por Edad": filter_by_age_rating,
                           "Salir":exit,
    }       
    
    # Imprime los titulos y las opciones en pantalla
    print_wrapped_text(MAIN_SCREEN_TITLE) # Imprime el titulo de la pantalla principal 
    print_wrapped_screen(list(MAIN_SCREEN_OPTIONS.keys())) # convierte en "list/lista" las "keys/llaves" del diccionario

    
    # Loop de la funcionalidad basica
    while LOOP:
        # Los mensajes deberian ser dinamicos tambien
        # Si el "user" no es "int" dejar un mensaje y que no se rompa
        user = ask_user(MAIN_SCREEN_MESSAGE, False)
        #Necesita el user_input y los valores de un diccionario con funciones
        select_option(user, list(MAIN_SCREEN_OPTIONS.values()))
        
    
    
    
if __name__ == "__main__":
    main()
    
    


