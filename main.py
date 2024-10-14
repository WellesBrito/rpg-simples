import random
import os

# Variaveis do jogo
quantidade_espaco = 100

# Variaveis do personagem
vida_maxima = random.randint(100, 200)
vida_atual = vida_maxima
ataque_base = random.randint(30, 50)
estamina_maxima = random.randint(1, 5)
estamina_atual = estamina_maxima

# -------------------------------------------------------------------------

os.system('cls') or None
print('Seja bem vindo ao jogo RPG text')
# nome_personagem = input('Qual o nome do personagem: ')
nome_personagem = 'Kirito'

# -------------------------------------------------------------------------
while True:
    if vida_atual <= 0:
        break
    
    print('=' * quantidade_espaco)
    print(f'{nome_personagem:^{quantidade_espaco}}')
    print('=' * quantidade_espaco)
    print('Barra de vida ({}/{}): '.format(vida_atual, vida_maxima), end='')
    print('♡ ' * (vida_atual // 10))
    print('Ataque base ({}): '.format(ataque_base), end='')
    print('☨ ' * (ataque_base // 5))
    print('Estamina ({}): '.format(estamina_atual), end='')
    print('≋ ' * estamina_atual)
    print('=' * quantidade_espaco)

    # Variaveis do inimigo
    vida_maxima_slime = random.randint(30, 50)
    vida_atual_slime = vida_maxima_slime
    ataque_base_slime = random.randint(10, 20)

    print('\nUm inimigo foi encontrado!\n')
    
    print('=' * quantidade_espaco)
    print(f'{"slime":^{quantidade_espaco}}')
    print('=' * quantidade_espaco)
    print('Barra de vida ({}/{}): '.format(vida_atual_slime, vida_maxima_slime), end='')
    print('♡ ' * (vida_atual_slime // 10))
    print('Ataque base ({}): '.format(ataque_base_slime), end='')
    print('☨ ' * (ataque_base_slime // 5))
    print('=' * quantidade_espaco)

    while True:
        print('\nFaça sua escolha: ')
        print('[1] Atacar')
        print('[2] Fugir')
        escolha = int(input('> '))
        os.system('cls') or None
        
        if escolha == 1:
            if ataque_base >= vida_maxima_slime:
                print('HIT KILL!!!')
                break
        
            vida_atual_slime = vida_atual_slime - ataque_base
        elif escolha == 2:
            if estamina_atual > 0:
                estamina_atual = estamina_atual - 1
                break
            else:
                print('Você não tem estamina!')
        else:
            print('Escolha uma opção válida!')
        
        vida_atual = vida_atual - ataque_base_slime
        print('=' * quantidade_espaco)
        print(f'{nome_personagem:^{quantidade_espaco}}')
        print('=' * quantidade_espaco)
        print('Barra de vida ({}/{}): '.format(vida_atual, vida_maxima), end='')
        print('♡ ' * (vida_atual // 10))
        print('Ataque base ({}): '.format(ataque_base), end='')
        print('☨ ' * (ataque_base // 5))
        print('Estamina ({}): '.format(estamina_atual), end='')
        print('≋ ' * estamina_atual)
        print('=' * quantidade_espaco)

        print('=' * quantidade_espaco)
        print(f'{"slime":^{quantidade_espaco}}')
        print('=' * quantidade_espaco)
        print('Barra de vida ({}/{}): '.format(vida_atual_slime, vida_maxima_slime), end='')
        print('♡ ' * (vida_atual_slime // 10))
        print('Ataque base ({}): '.format(ataque_base_slime), end='')
        print('☨ ' * (ataque_base_slime // 5))
        print('=' * quantidade_espaco)
        if vida_atual_slime <= 0 or vida_atual <= 0:
            break
    print('\nVocê derrotou o inimigo!')
print('\nVocê MORREU!')
