from pyswip import Prolog
from pyswip import Functor
import random
from image import DrawImage
import os
import time

lista_conocimiento = []


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# Iniciar el intérprete de Prolog
prolog = Prolog()
prolog.consult("rpg_combate.pl")

# Función para obtener un enemigo aleatorio
def obtener_tropa_aleatoria():
    # Realizar la consulta en Prolog
    query_result = list(prolog.query("obtener_tropa_aleatoria(Enemigo)"))
    
    # Obtener el resultado (si hay alguno)
    if query_result:
        return query_result[0]['Enemigo']
    else:
        return None
        
def enfrentar_usuario():
    clear()
    print("Clases disponibles: mago | orco | elfo | enano | vampiro | dragon | guerrero | troll | bruja") 
    print("Tu conocimiento es: ")
    global lista_conocimiento
    for element in lista_conocimiento:
        print("-> ",element.args[0].decode('utf-8'), "gana", element.args[1].decode('utf-8'))

    tropa = obtener_tropa_aleatoria()

    image = DrawImage.from_file("enemies/" + tropa + ".png",(18,9))
    image.draw_image()
    
    print(f"¡Te enfrentas a un {tropa}!")

    usuario = input("Elige tu invocación:" )
    time.sleep(1)

    resultado_query = list(prolog.query(f"ganador_combate({usuario}, {tropa})"))
    if resultado_query:
        print("¡Has ganado el combate!")
        
        lista_diccionarios = list(prolog.query("obtener_enemigos_derrotados(Lista)."))

        lista_conocimiento = lista_diccionarios[0]['Lista']
            
        time.sleep(2)
        return True
        
    else:
        print("¡Has perdido el combate!")
        resultado_query = list(prolog.query(f"ganador_combate('{usuario}', '{tropa}')"))
        time.sleep(1)
        return False
    

# Programa principal
if __name__ == "__main__":
    print("¡Bienvenido a la invocacion de conocimiento!")
    print("----------------------------------------")
    counter = 0
    while True:
        
        if enfrentar_usuario() == False:
            print("Has perdido!\nCombates ganados: ", counter)

            seleccion = input("Volverlo a intentar? (s/n): ")
            if seleccion == "s":
                counter = 0
                continue
            else:
                break
        counter += 1
        
