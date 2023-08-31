userInput = input("Anna numero: ")

numbers = []

while userInput != "":
    numbers.append(float(userInput))
    userInput = input("Anna numero: ")


def list_even(array):
    print(array)
    print("\n")

    for oddNumber in array:
        if oddNumber % 2 != 0:
            array.remove(oddNumber)
    return print(array)


list_even(numbers)
