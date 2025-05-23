def q1():
    ano = int(input("Digite o ano da primeira dose: "))
    intervalo = 4


    for i in range(1, 5):
        print(ano + i * intervalo,end=" ")
      



def q2():
    numeros = []
    while True:
        n = int(input("Digite um número (ou um valor negativo para encerrar): "))
        if n < 0:
            break
        numeros.append(n)
    for n in numeros:
        if n % 2 == 1:
            print("Primo")
        else:
            print("Não")


def q3():
    total = 0
    contador = 0
    while True:
        doacao = float(input("Digite o valor da doação (ou um valor negativo para encerrar): "))
        if doacao < 0:
            break
        total += doacao
        contador += 1
    print(f"{total:.2f}")
    if contador > 0:
        print(f"{(total / contador):.2f}")
    else:
        print("0.00")

def q4():
    kmRodado = int(input("Digite a quilometragem total rodada: "))
    dias = int(input("Digite a quantidade de dias de aluguel: "))

    if dias <= 0:
        print("Valor inválido")
        return

    diaria = 90
    incluso = 100
    taxa = 12

    total = dias * diaria
    if kmRodado > dias * incluso:
        extra = kmRodado - dias * incluso
        total += extra * taxa

    print(f"{total:.2f}")


def q5():
        graus = float(input("Digite a temperatura: "))
        Temperatura = str(input("C, F, K"))


        if Temperatura == "C":
            print(graus * 9/5 + 32)
            print(graus + 273,15 )
        elif Temperatura == "F":
            print(graus * 5/9)
            print(graus * 1,8 - 459,67)
        elif Temperatura == "K":
            print(graus + 273,15 )
            print(graus *  9/5 + 32)
        else:
            print("Inválido")
            

if __name__=="__main__":
    q5()