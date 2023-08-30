userInput = input("Anna numero: ")

numbers = []

while userInput != "":
    numbers.append(float(userInput))
    userInput = input("Anna numero: ")


def list_sum(array):
    sum = 0
    for number in array:
        sum += number

    return print(sum)


list_sum(numbers)
