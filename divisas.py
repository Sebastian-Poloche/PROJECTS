def USD():
    usuario = str(input("Bienvenido que divisa tienes para convertir de USD a [COP o EUR]: ").upper())
    if usuario == "COP":
        valor = int(input("que valor deseas convertir: "))
        resultado = valor*(4335.10/1)
        print(f"tus {valor} dolares en pesos colombianos son: {resultado}")
    elif usuario == "EUR":
        valor = int(input("que valor deseas convertir: "))
        resultado = valor*(0.9734/1)
        print(f"tus {valor} dolares en euros son: {resultado}")
    else:
        print("valor incorrecto")

def EUR():
    usuario = str(input("Bienvenido que divisa tienes para convertir de EUR a [COP o USD]: ").upper())
    if usuario == "COP":
        valor = int(input("que valor deseas convertir: "))
        resultado = valor*(4453.45/1)
        print(f"tus {valor} euros en pesos colombianos son: {resultado}")
    elif usuario == "USD":
        valor = int(input("que valor deseas convertir: "))
        resultado = valor*(1.03/1)
        print(f"tus {valor} euros en dolares son: {resultado}")
    else:
        print("valor incorrecto")
        
def COP():
    usuario = str(input("Bienvenido que divisa tienes para convertir de COP a [USD o EUR]: ").upper())
    if usuario == "USD":
        valor = int(input("que valor deseas convertir: "))
        resultado = valor*(0.000230321/1)
        print(f"tus {valor} pesos colombianos en dolares son: {resultado}")
    elif usuario == "EUR":
        valor = int(input("que valor deseas convertir: "))
        resultado = valor*(0.000224337/1)
        print(f"tus {valor} pesos colombianos en euros son: {resultado}")
    else:
        print("valor incorrecto")

def main():
    print("conversor de divisas")
    usuario = str(input("ingresa la divisa que deseas [USD, EUR o COP]: ").upper())
    if usuario == "USD":
        USD()
    elif usuario == "EUR":
        EUR()
    elif usuario == "COP":
        COP()
    else:
        print("valor incorrecto")

if __name__ == "__main__":
    main()