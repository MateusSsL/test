# Interpolação básica de strings com %%%%%%%%%%%%%%%%%%%%%%%%
# s - string
# d e i - int
# f - float
# x e X - Hexadecimal (ABCDEF0123456789)
# """
# nome = 'Luiz'
# preco = 1000.95897643
# variavel = '%s, o preço é R$%.2f' % (nome, preco)
# print(variavel)
# print('O hexadecimal de %d é %08X' % (1500, 1500))

# Interpolação básica de strings com f-string
"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')