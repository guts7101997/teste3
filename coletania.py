print('Coletânia de jogos')
jogos_do_usuario = []

while True:

    oq_fazr = input('Deseja adicionar jogos a lista ou procurar jogos ja existentes? (N para fechar o programa)')
    oq_fazr = oq_fazr.strip().lower()


    if oq_fazr == 'adicionar':

        quant_de_jogos = int(input('Quantos jogos deseja registrar:'))
        for n in range (0, quant_de_jogos):
            jogo = input('Digite o nome do jogo: ')
            jogo = jogo.strip().lower()
            jogos_do_usuario.append(jogo)

            n += 1
        print('Jogos adicionados a lista!')

    elif oq_fazr == 'n':
        break

    else:
        jogo_existente = input('Qual jogo deseja procurar? ')
        jogo_existente = jogo_existente.strip().lower()
        if jogo_existente in jogos_do_usuario:
            print(f'O jogo {jogo_existente} esta na lista!')
        else:
            print(f'O jogo {jogo_existente} não foi adiconado a lista ainda!')


