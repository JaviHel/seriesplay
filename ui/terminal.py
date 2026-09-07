import json, random
from carga_de_datos import *
from ascii_frame import *




# MAIN SETUP
DATA = cargar_json("../datos/dataset_10.json")
LOOP = True
WIDTH = 60
af = AsciiFrame(WIDTH)



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





# FUNCIONES DE INPUT Y SELECCION
def ask_user(message = "text", type_str=True):
    if type_str:
        return input(message)
    return int(input(message))
    

def select_option(user_input):
    # Este menu deberia ser dinamico de entrada y seleccion
    
    # Buscar Serie
    if user_input == 1:
        name = ask_user("INGRESE EL NOMBRE DE LA SERIE (en ingles): ")
        print("buscando serie... ")

        if filter_by(name, "title"):
            print_wrapped_text(f'La serie "{name}" SI se encuentra disponible.')
        else:
            print_wrapped_text(f'La serie "{name}" NO se encuentra disponible.')

        exit()

    # Recomendar serie aleatoria
    elif user_input == 2:
        name = random_recommendation()
        print("recomendando serie aleatoria...")
        print_wrapped_text(f'Te recomiendo que mires "{name}". ¡Esta muy buena!')
        exit()
    

    # Filtrar por genero
    elif user_input == 3:
        genres = ['Horror', 'Comedy', 'Sci-Fi', 'Fantasy', 'Action', 'Thriller', 'Reality',
                  'Crime', 'Drama', 'Talk', 'Animation', 'Mystery', 'Adventure', 'Documentary']
        print('Ejemplo de generos: "Talk", "Horror", "Comedy", "Crime", etc...')
        
        genre = ask_user("INGRESE EL NOMBRE DEL GENERO (en ingles): ")
        lst = select_by(genre, "genre")
        
        print("filtrando por generos...")
        if len(lst) > 0:
            af.print_box("t")
            af.print_text(f'Se encontraron estas series de genero "{genre}"', "c",)
            af.print_space("-")
            [af.print_text(f"[{i+1}]" + serie["title"]) for i, serie in enumerate(lst)]
            af.print_box("b")
        else:
            print_wrapped_text(f'No se encontro el genero "{genre}"')
        
        exit()
    
    # Filtrar por cantidad de temporadas
    elif user_input == 4:
        # filter_by_seasons()
        print("filtrar temporadas")
    
    
    
    # Filtrar por duracion de capitulo
    elif user_input == 5:
        # filter_by_episode_duration()
        print("filtrar capitulo")
        
    
    # Salir
    elif user_input == 6:
        exit()
        print("salir")
        
    else:
        print("): Esa no es una opcion de la lista :(")



# FUNCIONALIDAD DE CADA OPCION


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
    
    
def random_recommendation():
    """ Retorna una serie aleatoria de a la lista """
    return random.choice(DATA["series"])["title"]
 
 
def exit():
    global LOOP
    LOOP = False







def main():
    # Variables de los titulos y opciones de cada pantalla
    MESSAGE_1 = "SELECIONE UNA OPCION DEL MENU: "
    MAIN_SCREEN_TITLE = "🎞 SERIESPLAY 🎞"
    MAIN_SCREEN_OPTIONS = ["Buscar Series",
#                           "Recomendar Serie Relacionada", # Implementar mas adelante
                           "Recomendar Serie Aleatoria",
                           "Filtrar Por Genero",
                           "Filtrar Por Cantidad De Temporadas",
                           "Filtrar Por Duracion De Capitulo",
                           "Salir"]     
    
    # Imprime los titulos y las opciones en pantalla
    print_wrapped_text(MAIN_SCREEN_TITLE)
    print_wrapped_screen(MAIN_SCREEN_OPTIONS)

    
    # Loop de la funcionalidad basica
    while LOOP:
        ui = ask_user(MESSAGE_1, False)
        select_option(ui) # Si "ui" no es "int" dejar un mensaje y que no se rompa
        


if __name__ == "__main__":
    main()


























