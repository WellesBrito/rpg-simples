import random

# Variaveis do jogo
quantidade_espaco = 100

# Variaveis do personagem
vida_maxima = random.randint(100, 200)
vida_atual = vida_maxima
ataque_base = random.randint(30, 50)
estamina_maxima = random.randint(1, 5)
estamina_atual = estamina_maxima

# -------------------------------------------------------------------------

print('Seja bem vindo ao jogo RPG text')
nome_personagem = input('Qual o nome do personagem: ')
# nome_personagem = 'Kirito'

print('=' * quantidade_espaco)
print('{:^100}'.format(nome_personagem))
print('=' * quantidade_espaco)
print('Barra de vida ({}/{}): '.format(vida_atual, vida_maxima), end='')
print('♡ ' * (vida_atual // 10))
print('Ataque base: {}'.format(ataque_base))
print('Estamina: {}'.format(estamina_atual))
print('=' * quantidade_espaco)
