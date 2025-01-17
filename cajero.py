# cajero automatico

def retirar_dinero():
    print("cuanto dinero desea retirar")
    usuario = int(input(""))
    resultado = saldo - usuario
    print(f"retirando {resultado}")
    print(f"tu saldo sobrante es {saldo}")

def depositar_dinero():
    print("cuanto dinero desea depositar")
    usuario = int(input(""))
    resultado = saldo + usuario
    print(f"se deposito: {usuario} tu total es: {resultado}")

def consultar_saldo():
    print(f"tu saldo es: {saldo}")

clave = 2053
saldo = 500000
def main():
    intentos = 0
    while True:
        usuario = int(input("ingresa tu clave: "))
        if usuario != clave:
            intentos += 1
            print("clave incorrecta, vuelve a intentarlo")
            if intentos == 3:
                return print("Muchos intentos, vuelve más tarde")
        if usuario == clave:
            break

    while usuario != 4:
        print("\n Bienvenido al banco que desea consultar")
        print("1) retirar dinero")
        print("2) depositar dinero")
        print("3) consultar saldo")
        print("4) salir")

        usuario = int(input("que desea: "))
        if usuario == 1:
            retirar_dinero()
        elif usuario == 2:
            depositar_dinero()
        elif usuario == 3:
            consultar_saldo()
        elif usuario == 4:
            print("hasta luego")
        else:
            print("opcion invalida")

if __name__ == "__main__":
    main()
