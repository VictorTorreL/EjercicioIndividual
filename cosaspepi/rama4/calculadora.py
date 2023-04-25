# Definimos las funciones para realizar las operaciones aritméticas
def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "No se puede dividir por cero"
    else:
        return num1 / num2

# Solicitamos al usuario que ingrese los números y la operación que desea realizar
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
operacion = input("Ingresa la operación que deseas realizar (+, -, *, /): ")

# Realizamos la operación seleccionada por el usuario
if operacion == "+":
    resultado = suma(num1, num2)
elif operacion == "-":
    resultado = resta(num1, num2)
elif operacion == "*":
    resultado = multiplicacion(num1, num2)
elif operacion == "/":
    resultado = division(num1, num2)
else:
    resultado = "Operación inválida"

# Imprimimos el resultado
print("El resultado de la operación es:", resultado)
