import os

restaurantes = [{"nome" : "Menu" , "categoria" : "Japonesa", "ativo" :False},
                 {"nome" : "Pizza Suprema", "categoria" : "Pizza", "ativo" : True},
                 {"nome" : "Cantina", "categoria" : "Italiana", "ativo" : False}]



def exibir_nome_do_programa():
    """ Essa funcao exibe o nome do programa"""

    print("""
           ▌║█║▌│║▌│║▌║▌█║Sabor Express ▌│║▌║▌│║║▌█║▌║█
          """)

def exibir_menu_opcoes():
    """ Essa funcao exibe o menu opcoes
    
    Outputs:
    - Lista as opcoes disponiveis ao usuario
    
    """
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Alternar status do restaurante")
    print("4. Sair\n")

def opcao_invalida():
    """ Essa funcao exibe se a opcao eh invalida e volta ao menu principal"""
    print("Opcao Invalida!\n")
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    """ Essa funcao exibe o subtitulo"""
    os.system("cls")
    linha = "=" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    """ Essa funcao e responsavel por cadastrar um novo restaurante
    
    Inputs:
    - Nome do Restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes

    """
    exibir_subtitulo("Cadastro de novos restaurantes")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite o nome da categoria do restaurante {nome_do_restaurante}:")
    dados_do_restaurante = {"nome":nome_do_restaurante, "categoria":categoria, "ativo":False}
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n")
    voltar_ao_menu_principal()

def listar_restaurantes():
    """ Essa funcao e responsavel por listar os restaurantes
    
    Operador logico:
    - for para buscar dentro da lista os nomes, categoria e status do restaurante

    Outputs:
    - Lista os restaurantes cadastrados
    
    """


    exibir_subtitulo("Listando os restaurantes")

    print(f"{"Nome do restaurante".ljust(15)} | {"Categoria".ljust(15)} | Status\n")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "Ativado" if restaurante["ativo"] else "Desativado"
        print(f" - {nome_restaurante.ljust(15)} | {categoria.ljust(15)} | {ativo}\n")

    voltar_ao_menu_principal()

def alternar_estado_do_restaurante():
    """ Essa funcao e responsavel por alternar o estado de um restaurante
    
    Inputs:
    - Nome do Restaurante que deseja buscar na lista

    Operador logico:
    - for para buscar dentro da lista o nome do restaurante e verificar se ele existe ou nao

    Outputs:
    - Informa que o restaurante foi ativado ou desativado com sucesso
    
    """

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
    """ Essa funcao e responsavel por finalizar o app"""

    exibir_subtitulo("Finalizar app")

def voltar_ao_menu_principal():
    """ Essa funcao e responsavel por voltar ao menu principal
    
    Input:
    - Usuario insere uma tecla qualquer para retornar ao menu principal
    
    """

    input(" Digite uma tecla para voltar ao menu ")
    main()

def escolher_opcao():
    """ Essa funcao e responsavel por escolher e verificar a opcao
    
        Operador logico:
        - Try para que o usuario escolha uma opcao
        - If/elif/else para verificar qual opcao o usuario escolheu e assim executar a funcao respectiva
        - Except para caso a opcao inserida seja invalida

        Inputs:
        - Opcao escolhida

    """

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
    """ Essa funcao eh a main def"""

    os.system("cls")
    exibir_nome_do_programa()
    exibir_menu_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()