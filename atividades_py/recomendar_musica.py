def exibir_nome_do_programa():
    print("""
Recomendador de Música
          """)

def exibir_input_pessoal():
    genero_favorito = input("Digite o gênero musical que você prefere: ")
    nome_musica = input("Digite o nome de uma música que você gosta: ")
    genero_musica = input("Digite o gênero da música: ")
    return genero_favorito, nome_musica, genero_musica

def comparador_musical(genero_favorito, genero_musica):
    if genero_favorito.lower() == genero_musica.lower():
        return 'Com base na sua preferência, recomendamos essa música!'
    else:
        return 'Não recomendada.'

def main():
    exibir_nome_do_programa()
    genero_favorito, nome_musica, genero_musica = exibir_input_pessoal()
    resultado = comparador_musical(genero_favorito, genero_musica)
    print(resultado)

if __name__ == "__main__":
    main()
