import os

def exibir_nome_do_programa():
    print("""
Este numero é par ou ímpar?
          """)
    
def input_numero():
    numero = int(input("Digite um número inteiro: "))
    return numero

def verificar_par_ou_impar(numero):
    os.system('cls')
    if numero % 2 == 0:
        return "O número é par.\n"
    else:
        return "O número é ímpar.\n" 
    
def main():
    exibir_nome_do_programa()
    numero = input_numero()
    resultado = verificar_par_ou_impar(numero)
    print(resultado)

if __name__ == "__main__":
    main()  
