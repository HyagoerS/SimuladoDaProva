def q1():


    pass

def q2():
    numeros = []

    while True:
        n = int(input("Digite um número: "))
        if n < 0:
            print("Número negativo")
            break
        numeros.append(n)
    for n in numeros:
        if n % 2 == 1:
            print("Primo")
        else:
            print("Não")


def q3():
    pass

def q4():
    pass

def q5():
    pass

if __name__=="__main__":
    q2()