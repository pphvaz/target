# 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

def tem_a(texto):
    if 'a' in texto:
        return True
    else:
        return False

def conta_a(texto):
    qtd_a = 0
    for letra in texto:
        if letra == 'a':
            qtd_a += 1
    return qtd_a

def main():
    texto = input("Digite seu texto: ")
    condicao = tem_a(texto.lower())

    if condicao:
        qtd_a = conta_a(texto.lower())
        print(f"O texto ' {texto} ' tem {qtd_a} 'a'.")
main()