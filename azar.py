import random

# opcion 1 la más sencilla sin funcion y pocas variables

intentos = 0
while True:
    usuario = int(input("ingresa un numero entre el [0 y 10]: "))
    bot = random.randint(0,10)
    if usuario == bot:
        print(f"Ganaste tu numero era: {usuario} y el del bot era: {bot}")
        break
    if usuario < bot:
        print("el numero es mayor")
    if usuario > bot:
        print("el numero es menor")
    if usuario != bot:
        intentos += 1
        print("intento fallido, prueba otra vez")
        if intentos == 3:
            print("intentos maximos")
            break

    print("Perdiste")

# opcion 2 ya con funciones y más variables

def adivinar_numero(usuario, bot):
    usuario = str(input("nivel de dificultad [facil], [normal], [dificil]: ").lower())
    intentos = 0
    if usuario == "facil":
        while True:
            usuario = int(input("ingresa un número entre el [0, 10]: "))
            bot = random.randint(0,10)
            if usuario == bot:
                return print(f"ganaste tu eleccion fue el: {usuario} y el del bot era: {bot}")
            if usuario < bot:
                print("el numero es mayor")
            if usuario > bot:
                print("el numero es menor")
            if usuario != bot:
                intentos += 1
                print("incorrecto")
                if intentos == 3:
                    print("intentos maximos")
                    return print("perdiste")
                
    if usuario == "normal":
        while True:
            usuario = int(input("ingresa un número entre el [0, 50]: "))
            bot = random.randint(0,50)
            if usuario == bot:
                return print(f"ganaste tu eleccion fue el: {usuario} y el del bot era: {bot}")
            if usuario < bot:
                print("el numero es mayor")
            if usuario > bot:
                print("el numero es menor")
            if usuario != bot:
                intentos += 1
                print("incorrecto")
                if intentos == 5:
                    print("intentos maximos")
                    return print("perdiste")
                
    if usuario == "dificil":
        while True:
            usuario = int(input("ingresa un número entre el [0, 100]: "))
            bot = random.randint(0,100)
            if usuario == bot:
                return print(f"ganaste tu eleccion fue el: {usuario} y el del bot era: {bot}")
            if usuario < bot:
                print("el numero es mayor")
            if usuario > bot:
                print("el numero es menor")
            if usuario != bot:
                intentos += 1
                print("incorrecto")
                if intentos == 10:
                    print("intentos maximos")
                    return print("perdiste")

adivinar_numero(usuario="", bot="")

    
