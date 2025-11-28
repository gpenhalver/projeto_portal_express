import os

nomes = ["Gabriel","Julia","Alfredo","Maria"]
ano = ["2001","2025"]

def exibir_nome_do_programa():
    print("""
            Lista de Numeros de 1 a 10 / Nomes / Ano de Nascimento
          """)

def inserir_numero_na_lista(numeros):
    try:
        numero_inserido = int(input("Insira um número de 1 a 10: "))
        if 1 <= numero_inserido <= 10:
            if numero_inserido in numeros:
                print(f"O número {numero_inserido} já está na lista! Não será adicionado novamente.\n")
                return voltar_menu(numeros)

            numeros.append(numero_inserido)
            numeros.sort()

            print(f"O número {numero_inserido} foi inserido com sucesso!\n")

            print("Aqui está a lista atualizada:")
            for numero in numeros:
                print(f". {numero}")
            print(f". {nomes}")
            print(f". {ano}")
            voltar_menu(numeros)
        else:
            print("Número inválido, tente novamente.")
            voltar_menu(numeros)
    except:
        print("Número inválido, tente novamente.")
        voltar_menu(numeros)

def voltar_menu(numeros):
    input("\nDigite ENTER para voltar ao menu ")
    main(numeros)

def main(numeros=None):
    os.system("cls")

    # Se a lista não existe ainda, cria uma nova
    if numeros is None:
        numeros = []

    exibir_nome_do_programa()
    inserir_numero_na_lista(numeros)

if __name__ == "__main__":
    main()
