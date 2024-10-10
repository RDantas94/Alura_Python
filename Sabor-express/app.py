import os

restaurantes = []


def limpar_tela():
    os.system('cls')


def exibir_nome_do_programa():
    print('''
    S̲a̲b̲o̲r̲ E̲x̲p̲r̲e̲s̲s̲
      ''')


def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')


def opcao_invalida():
    print('Opção inválida!\n')
    input('Digite uma tecla para voltar ao menu principal')
    main()


def cadastrar_novo_restaurante():
    limpar_tela()
    print('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input(
        'Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O Restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    input('Digite uma tecla para voltar ao menu principal')
    main()


def listar_restaurantes():
    pass


def finalizar_app():
    limpar_tela()
    print('Finalizando o app')


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                print('Ativar restaurante')
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()


def main():
    limpar_tela()
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
