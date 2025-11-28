import os

print("""
      Definindo Faixa Etária
      """)

def input_faixa_etaria():
    faixa_etaria = int(input("Digite a sua idade: "))
    return faixa_etaria

def definir_faixa_etaria(faixa_etaria):
    if faixa_etaria >= 0 and faixa_etaria <= 12:
        return "Criança"
    elif faixa_etaria >= 13 and faixa_etaria <= 18:
        return "Adolescente"
    else: # faixa_etaria >= 19
        return "Adulto"
    
def main():
    idade = input_faixa_etaria()
    faixa = definir_faixa_etaria(idade)
    print(f"Sua faixa etária é: {faixa}")

if __name__ == "__main__":
    main()