list = list(range(1, 100))

for numero in list:
    if numero%3 == 0 and numero%5 == 0:
        print("fizzbuzz\n")
    elif numero%5 == 0:
        print("buzz\n")
    elif  numero%3 == 0:
        print("fizz\n")
    else:
        print("{}\n".format(numero))