import os


def exibir_nome_do_programa():
    print("""
            Soma de todos os elementos!
          """)

def user_values():
    while True:
        try:
            tamanho = int(input("Digite o tamanho da sua lista: "))
            if tamanho < 0:
                print("O tamanho deve ser maior ou igual a 0.")
                continue
            return tamanho
        except:
            print("Digite um número válido!")


def gerar_lista(tamanho):
    lista = []
    print("\nAgora insira os valores da lista:\n")

    for i in range(tamanho):
        while True:
            try:
                valor = int(input(f"Digite o valor {i+1}: "))
                lista.append(valor)
                break
            except:
                print("Valor inválido! Digite um número inteiro.")
    
    return lista


def soma_lista(lista):
    soma = sum(lista)
    print("\nLista gerada:", lista)
    print("Soma dos valores:", soma)


def main():
    os.system("cls" if os.name == "nt" else "clear")
    exibir_nome_do_programa()

    tamanho = user_values()
    lista = gerar_lista(tamanho)
    soma_lista(lista)


if __name__ == "__main__":
    main()


#Funcao gerar lista aleatoria
# def gerar_lista_aleatoria(tamanho, minimo, maximo):
    # lista = []
    # for _ in range(tamanho):
    #     numero = random.randint(minimo, maximo)
    #     lista.append(numero)
    # return lista

# soma da lista aleatoria

# lista = gerar_lista_aleatoria(5, 1, 1000)
# print("Lista gerada:", lista)

# soma = sum(lista)
# print("Soma dos valores:", soma)
    


