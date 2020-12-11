"""
Desafio link: https://www.codewars.com/kata/5412509bd436bd33920011bc
"""


def maskify(cc):

    numeros_finais_da_conta = cc[-4:]
    numeros_iniciais = cc[:len(cc) - 4]
    numeros_iniciais.replace(numeros_iniciais, "#")

    if len(cc) == 3:
        return cc
    else:
        return numeros_iniciais.replace(numeros_iniciais, ("#" * len(numeros_iniciais))) + numeros_finais_da_conta


print(maskify('12313213213212321'))
print(maskify('Gabriel Ramos dos Santos'))
print(maskify('132165'))
print(maskify('fefewfe'))
print(maskify('1231321ffwefwefwefw3213212321'))
print(maskify('12313213213212fwefwfw321'))
print(maskify('ccccccccccccccccc1609'))


