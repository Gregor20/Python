import math

def formula_Bernoulli_simple(n: int):                   # Fórumla de Bernoulli para números simples (1 + 2 + 3 + 4 + ...)
    resultado = n * (n + 1) / 2
    return resultado

def formula_Bernoulli_cuadrado(n: int):                 # "" para números al cuadrado (1^2 + 2^2 + 3^2 + 4^2 + ...)
    resultado = n * (n + 1) * (2 * n + 1) / 6
    return resultado

def formula_Bernoulli_cubo(n: int):                     # "" para números al cubo (1^3 + 2^3 + 3^3 + 4^3 + ...)
    resultado = math.pow(n * (n + 1) / 2, 2)
    return resultado



peticion = input("Dime un número: ")            # Petición al usuario

try:
    numero_entero = int(peticion)                                       # Pasa la petición a INT
    formula = formula_Bernoulli_simple(numero_entero)                   # Guarda el resultado en una variable
    print(f"Formula de Bernoulli con números simples: {formula}")       # Imprime
except ValueError:
    print("Error: Debes introducir un número entero válido.")

try:
    numero_entero_2 = int(peticion)
    formula_2 = formula_Bernoulli_cuadrado(numero_entero_2)
    print(f"Formula de Bernoulli con números al cuadrado: {formula_2}")
except ValueError:
   print("Error: Debes introducir un número entero válido.")

try:
    numero_entero_3 = int(peticion)
    formula_3 = formula_Bernoulli_cubo(numero_entero_3)
    print(f"Formula de Bernoulli con números al cubo: {formula_3}")
except ValueError:
   print("Error: Debes introducir un número entero válido.")
