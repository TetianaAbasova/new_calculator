number_1 = int(input("Enter a first number: "))
comand = input("Enter a comand: ")
number_2 = int(input("Enter a second number: "))

if comand == "+":
    print(number_1 + number_2)
elif comand == "-":
    print(number_1 - number_2)
elif comand == "*":
    print(number_1 * number_2)
elif comand == "/":
    print(number_1 / number_2)
else:
    print("Invalid command")