"""
Desafio link: https://www.codewars.com/kata/5266876b8f4bf2da9b000362
"""


def likes(names):
    quantidade_de_nomes = 0
    lista_de_nomes = []
    for name in names:
        quantidade_de_nomes += 1
        nome = str(name)
        lista_de_nomes.append(nome)

    if quantidade_de_nomes == 1:
        return f'{lista_de_nomes[0]} likes this'
    elif quantidade_de_nomes == 2:
        return f'{lista_de_nomes[0]} and {lista_de_nomes[1]} like this'
    elif quantidade_de_nomes == 3:
        return f'{lista_de_nomes[0]}, {lista_de_nomes[1]} and {lista_de_nomes[2]} like this'
    elif quantidade_de_nomes > 3:
        return f'{lista_de_nomes[0]}, {lista_de_nomes[1]} and {quantidade_de_nomes - 2} others like this'
    else:
        return 'no one likes this'


print(likes(['Gabriel', 'Carlos', 'João', 'Marcos', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']))
