import os   

print("""
      Coordenadas de um ponto no plano cartesiano   
    """)

def ObterCoordenas():
    coordenada_x = float(input("Insira as coordenas X de um ponto qualquer: "))
    coordenada_y = float(input("Insira as coordenas Y de um ponto qualquer: "))
    return coordenada_x, coordenada_y

def QuadranteCoordenas(coordenada_x, coordenada_y):
    if coordenada_x > 0 and coordenada_y > 0:
        print("Os pontos fornecidos se encontram no primeiro quadrante!")
    elif coordenada_x < 0 and coordenada_y > 0:
        print("Os pontos fornecidos se encontram no segundo quadrante!")
    elif coordenada_x < 0 and coordenada_y < 0:
        print("Os pontos fornecidos se encontram no terceiro quadrante!")
    elif coordenada_x > 0 and coordenada_y < 0:
        print("Os pontos fornecidos se encontram no quarto quadrante!")
    else: 
        print("o ponto está localizado no eixo ou origem.")

def main():
    x,y = ObterCoordenas()
    QuadranteCoordenas(x, y)

if __name__ == "__main__":
    main()