import os

restaurantes = [{"nome" : "Menu" , "categoria" : "Japonesa", "ativo" :False},
                 {"nome" : "Pizza Suprema", "categoria" : "Pizza", "ativo" : True},
                 {"nome" : "Cantina", "categoria" : "Italiana", "ativo" : False}]



def exibir_nome_do_programa():
    print("""
           ▌║█║▌│║▌│║▌║▌█║Sabor Express ▌│║▌║▌│║║▌█║▌║█
          """)

def exibir_menu_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Alternar status do restaurante")
    print("4. Sair\n")

def opcao_invalida():
    print("Opcao Invalida!\n")
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system("cls")
    linha = "=" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de novos restaurantes")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite o nome da categoria do restaurante {nome_do_restaurante}:")
    dados_do_restaurante = {"nome":nome_do_restaurante, "categoria":categoria, "ativo":False}
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n")
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo("Listando os restaurantes")

    print(f"{"Nome do restaurante".ljust(15)} | {"Categoria".ljust(15)} | Status\n")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "Ativado" if restaurante["ativo"] else "Desativado"
        print(f" - {nome_restaurante.ljust(15)} | {categoria.ljust(15)} | {ativo}\n")

    voltar_ao_menu_principal()

def alternar_estado_do_restaurante():
    exibir_subtitulo("Alternando o status do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja alternar o status: ")
    restaurante_encontrado = False

    #Se o nome do restaurante for encontrado na lista, o status dele sera invertido para o valor oposto
    #Se nao for encontrado, ele vai avisar ao usuario que o restaurante nao foi encontrado!

    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = (f"O restaurante {nome_restaurante} foi ativado com sucesso" if restaurante["ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso")
            print(mensagem)
    if not restaurante_encontrado:
        print("O restaurante nao foi encontrado!")

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
            alternar_estado_do_restaurante()
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