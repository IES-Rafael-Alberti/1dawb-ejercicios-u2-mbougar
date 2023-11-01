"""
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
"""
def repeat_Word(word: str, numberTimes: int):
    """Takes a character string and returns a new string with the original string repeated a given number of times"""
    newWord = ""
    for i in range(0, numberTimes):
        newWord += word
        if i != numberTimes-1:
            newWord += "\n"
    return newWord


def main():
    print("Introduce una palabra para mostrar por pantalla 10 veces:", end=" ")
    word = input()
    word = repeat_Word(word, 10)
    print(word)


if __name__ == "__main__":
    main()
