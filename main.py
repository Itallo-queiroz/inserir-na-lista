# lista de nomes

nomes = []
# Menu
while True:
    print('1 - Insere novo nome. ')
    print('2 - Exibir lista de nomes. ')
    print('3 - exibir em ordem alfabetica. ')
    print('4 - Sair do programa. ')
    
    
    #opção de usuário
    opcao = input('Opção do usuario: ')

    # Verificar a opção escolhida
    match opcao:
        case '1':
            novo_nome = input('Insira o novo nome: ').capitalize()
            nomes.append(novo_nome)
            print(f'{novo_nome} Insirido com suceso. ')
            continue
        case '2':
            print('\nLista de nomes:\n')
            for nome in nomes:
                print(nome)
                continue
        case '3':
            nomes.sort()
            for nome in nomes:
                print(nome)
            print('\nLista ordenada com sucesso.')
            continue
        case '4':
            print('Progama encerrado. ')
            break
        case _:
            print('opcao invalida.')
            

