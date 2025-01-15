import random
import string

# opcion 1 forma sencilla

maximo = int(input("ingrese un valor: "))
caracteres = string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation
resultado = "".join((random.choice(caracteres)) for i in range(maximo))
print(f"la contraseña generada es: {resultado}")

# opcion 2 forma con funcion y más variables
# se necesita letras mayusculas y minusculas, numeros y caracteres especiales

def generar_contraseña(longitud, incluir_mayus, incluir_nums, incluir_esp):
    caracteres = string.ascii_lowercase
    if incluir_mayus:
        caracteres += string.ascii_uppercase
    if incluir_nums:
        caracteres += string.digits
    if incluir_esp:
        caracteres += string.punctuation
    contraseña = "".join(random.choice(caracteres) for i in range(longitud))
    return contraseña

longitud = int(input("ingresa la longitud de tu contraseña: "))
incluir_mayus = input("ingresar mayusculas (s/n): ").lower() == "s"
incluir_nums = input("ingresar numeros (s/n): ").lower() == "s"
incluir_esp = input("ingresar caracteres especiales (s/n): ").lower() == "s"

contraseña = generar_contraseña(longitud, incluir_mayus, incluir_nums, incluir_esp)
print(f"contraseña generada: {contraseña}")
    
