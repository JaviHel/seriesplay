import random, time
from carga_de_datos import *
from ascii_frame import *



# MAIN SETUP
DATA = cargar_json("../datos/dataset_100.json")
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
    """
    Imprime la lista de cadena de caracteres dentro de una caja ASCII
    lst debe ser una lista con strings
    """
    af.print_box("t")
    for i, option in enumerate(lst):
        af.print_text(f"[{i+1}]>" + option)
    af.print_box("b")





# FUNCIONES UTILES PARA EL RESTO DE OPCIONES
def filter_by(user_input, option):
    """ Filtra series por una opcion de manera lineal:
        title, genre, duration, etc...
    """
    for serie in DATA["series"]:
        if user_input.lower() == serie[option].lower():
            return True
    return False


def select_by(user_input, option):
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
    print("buscando serie... ")
    time.sleep(2) # Simula que esta buscando

    if filter_by(name, "title"):
        print_wrapped_text(f'La serie "{name}" SI se encuentra disponible.')
    else:
        print_wrapped_text(f'La serie "{name}" NO se encuentra disponible.')

    exit()



#2
def recommend_related():
    """ Recomienda una serie relacionada a la serie ingresada por el usuario """
    name = ask_user("INGRESE EL NOMBRE UNA SERIE QUE LE GUSTE (en ingles): ")
    exit()
    pass



#3
def recommend_random(): # pasamos opciones que no usamos, SÍ 
    name = get_random_option()
    print("recomendando serie aleatoria...")
    time.sleep(2) # Simula que esta buscando
    
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
    
    print("filtrando por generos...")
    time.sleep(2) # Simula que esta buscando
    
    if len(lst) > 0:
        af.print_box("t")
        af.print_text(f'Se encontraron estas series de genero "{genre}"', "c",)
        af.print_space("-")
        [af.print_text(f"[{i+1}]>" + serie["title"]) for i, serie in enumerate(lst)]
        af.print_box("b")
    else:
        print_wrapped_text(f'No se encontro el genero "{genre}"')
    
    exit()



#5
def filter_by_seasons():
    """ Imprime las series que tienen menos o igual cantidad de temporadas
        que la ingresada por el usuario
    """
    pass



#6
def filter_by_episode_duration():
    """ Imprime las series con menos duracion promedio de episodio
        el usuario debe ingresar la duracion promedio de una lista en pantalla
    """
    pass



#7
def filter_by_age_rating():
    """ Imprime las peliculas que son aptas para cierto publico
        el usuario ingresa la opcion de edad de una lista en pantalla
    """
    pass






# FUNCIONES DE INPUT Y SELECCION
def ask_user(message = "text", type_str=True):
    if type_str:
        return input(message)
    return int(input(message))


def select_option(user_input, method_call_lst):
    """ Dependiendo de lo que el usuario ingrese va a llamar a la opcion correcta 
    """
    # Solo llama a la funcion si el usuario ingresa un nro mayor que 0 y menor que el tamaño de la lista
    if user_input > 0 and user_input < len(method_call_lst)+1:
        method_call_lst[user_input-1]()
    else:
        print("ESA NO ES UNA OPCION DE LA LISTA")





def main():
    # Variables de los titulos y opciones de cada pantalla
    MESSAGE_1 = "SELECCIONE UNA OPCION DEL MENU: "    
    # MAIN_SCREEN_OPTIONS y MAIN_SCREEN_METHODS trabajan en conjunto
    # MAIN_SCREEN_OPTIONS guarda las opciones para imprimir en pantalla
    # MAIN_SCREEN_METHODS guarda la funcionalidad
    # cada pantalla a mostrar tendra que tener estas tres variables name_title, name_options, name_methods
    # entonces solo pasamos cada variable como parametro de una funcion que se encargara 
    # de imprimir todo automaticamente en el orden de cada opcion
    # IMPORTANTE: options y methods deben tener exactamente el mismo orden para funcionar
    # Ej: si la primera opcion es "buscar series" entonces el primer metodo sera "buscar_serie()"
    MAIN_SCREEN_TITLE = "🎞 SERIESPLAY 🎞"
    MAIN_SCREEN_OPTIONS = ["Buscar Series",
                           "Recomendar Serie Relacionada", # Implementar mas adelante
                           "Recomendar Serie Aleatoria",
                           "Filtrar Por Genero",
                           "Filtrar Por Cantidad De Temporadas",
                           "Filtrar Por Duracion De Capitulo",
                           "Filtrar Por Edad",
                           "Salir"]
    MAIN_SCREEN_METHODS = [search_series, 
                           recommend_related,
                           recommend_random,
                           filter_by_genre,
                           filter_by_seasons,
                           filter_by_episode_duration,
                           filter_by_age_rating,
                           exit]
    
    # Imprime los titulos y las opciones en pantalla
    print_wrapped_text(MAIN_SCREEN_TITLE)
    print_wrapped_screen(MAIN_SCREEN_OPTIONS)

    
    # Loop de la funcionalidad basica
    while LOOP:
        # Los mensajes deberian ser dinamicos tambien
        # Si el "user" no es "int" dejar un mensaje y que no se rompa
        user = ask_user(MESSAGE_1, False)
        # Necesita el user_input y la lista de funciones
        select_option(user, MAIN_SCREEN_METHODS)


if __name__ == "__main__":
    main()


























