import os

restaurantes = ["Pizza", "Sushi"]

def exibir_nome_do_programa():
    print("""
           ▌║█║▌│║▌│║▌║▌█║Sabor Express ▌│║▌║▌│║║▌█║▌║█
          """)

def exibir_menu_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Ativar restaurante")
    print("4. Sair\n")

def opcao_invalida():
    print("Opcao Invalida!\n")
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system("cls")
    print(texto)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de novos restaurantes")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    restaurantes.append(nome_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n")
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo("Listando os restaurantes")
    for restaurante in restaurantes:
        print(f".{restaurante}\n")
    voltar_ao_menu_principal()

def finalizar_app():
    exibir_subtitulo("Finalizar app")

def voltar_ao_menu_principal():
    input(" Digite uma tecla para voltar ao menu ")
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        # opcao_escolhida = int(opcao_escolhida)


        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            print("Ativar Restaurantes")
        elif opcao_escolhida == 4: 
            finalizar_app()
        else:
            opcao_invalida()

        #     opcao_escolhida = int(input('Escolha uma opção: '))
        # match opcao_escolhida:
        #     case 1:
        #         print('Adicionar restaurante')
        #     case 2:
        #         print('Listar restaurantes')
        #     case 3:
        #         print('Ativar restaurante')
        #     case 4:
        #         print('Finalizar app')
        #     case _:
        #         print('Opção inválida!')
    except: 
        opcao_invalida()

def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_menu_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()