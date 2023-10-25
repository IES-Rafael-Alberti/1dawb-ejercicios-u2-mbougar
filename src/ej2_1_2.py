"""Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
"""

def check_Password_Attempt(attempt: str, password: str):
    """Receives 2 character strings and returns "True" if """
    if attempt.lower() == password.lower() or attempt.upper() == password.upper():
        return True
    else:
        return False