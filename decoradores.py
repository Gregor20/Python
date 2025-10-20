def di_hola(func):          # Decorador
    def funcion_interna():
        print("Estoy diciendo hola!")
        return func()
    return funcion_interna  # Ojo no evaluada! (closure)

def nombre_decorador(func):             # Decorador
    def wrapper(*args, **kwargs):
        print(f"Ejecutando {func.__name__}")          # Lógica del decorador
        resultado = func(*args, **kwargs)           # Ojo, evaluada!
        print(f"Terminó {func.__name__}")
        return resultado
    return wrapper                      # Ojo, no evaluada!

@di_hola
def saludar():
    ...

@nombre_decorador
def saludar(nombre):
    print(f"Hola {nombre}")

saludar("Carlos")