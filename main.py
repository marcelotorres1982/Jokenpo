'''
Para nos auxiliar neste pequeno projeto, vamos contar com a ajuda da função choice() da biblioteca random,
ela será responsável por emular uma escolha pseudo-aleatória da máquina, entre as três opções disponíveis
(Pedra, Papel e Tesoura).

Também iremos utilizar um While Loop para manter o jogo executando até que o usuário deseje sair.

Coletaremos o input do usuário através da função input() e testaremos uma série de if, elif e else para sabermos quem
é o vitorioso.
'''

from random import choice

opcoes = ['pedra', 'papel', 'tesoura']
maquina = choice(opcoes)
jogando = True

while jogando:
    print('# pedra\n# papel\n# tesoura\n# sair')
    player = input('Escolha entre uma das opcoes :')
    if maquina == player.lower():
        print(f'Ocorreu um empate')
    elif player.lower() == 'pedra':
        if maquina == 'papel':
            print(f'Você perdeu! {maquina} cobre {player.lower()}!')
        else:
            print(f'Parabéns, voce venceu! {player.lower()} quebra {maquina}!')
    elif player.lower() == 'papel':
        if maquina == 'tesoura':
            print(f'Você perdeu! {maquina} corta {player.lower()}!')
        else:
            print(f'Parabéns, voce venceu! {player.lower()} cobre {maquina}!')
    elif player.lower() == 'tesoura':
        if maquina == 'pedra':
            print(f'Você perdeu" {maquina} esmaga {player.lower()}!')
        else:
            print(f'Você venceu! {player.lower()} corta {maquina}!')
    elif player.lower() == 'sair':
        jogando = False
    else:
        print('Jogada inválida, verifique se digitou a opção corretamente!')
        print('-'*45)
    maquina = choice(opcoes)
