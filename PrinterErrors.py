"""
https://www.codewars.com/kata/56541980fa08ab47a0000040
"""


def printer_error(s):
    letras_A_ate_M = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    contagem_acertos = 0
    tamanho = len(s)
    for letra in s:
        if letra not in letras_A_ate_M:
            contagem_acertos += 1
    else:
        pass

    return f"{contagem_acertos}/{tamanho}"


print(printer_error('aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz'))
