# 1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def fibo(num):
    fibo = [0, 1]
    x = 0
    y = 1
    contador = 0
    while fibo[-1] <= num:
        num_fibo = x + y
        x = y
        y = num_fibo
        fibo.append(num_fibo)
    return fibo
        
def main():
    while True:
        num = input("Digite um numero inteiro: ")
        if num.isdecimal():
            break
    lista = fibo(int(num))
    if int(num) in lista:
        return print(f"O número {num} está na sequência de fibonacci.")
    else:
        return print(f"O número {num} não está na sequência de fibonacci.\n  {lista}")

main()