# cajero automatico

def cajero(clave):
    clave = "2053"
    saldo = 500000
    intentos = 0
    while True:
        print("Ingresa tu clave")
        usuario = input("")
        if usuario != clave:
            intentos += 1
            print("clave incorrecto, vuelve a intentarlo")
            if intentos == 3:
                return print("Muchos intentos, vuelve más tarde")
        if usuario == clave:
            break
    print("Bienvenido al banco que desea consultar")
    print("1) retirar dinero")
    print("2) depositar dinero")
    print("3) consultar saldo")
    opcion = float(input(""))
    if opcion == 1:
        print(f"Tu saldo es de {saldo} pesos colombianos")
        print("cuanto dinero desea retirar")
        usuario = float(input(""))
        resultado = saldo - usuario
        print(f"retirando {usuario} pesos colombianos")
        print(f"tu saldo sobrante es de {resultado} pesos colombianos")
    if opcion == 2:
        print(f"Tu saldo es de {saldo} pesos colombianos")
        print("cuanto dinero desea depositar")
        usuario = float(input(""))
        resultado = saldo + usuario
        print(f"depositando {usuario} pesos colombianos")
        print(f"tu saldo total es de {resultado} pesos colombianos")        
    if opcion == 3:
        print("consultar saldo")
        print(f"tu saldo total es de {saldo} pesos colombianos")

cajero(clave="")
