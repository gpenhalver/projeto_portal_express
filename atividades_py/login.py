print("""
      Checking Login
      """)

login = "Usuario"
senha = "senha123"


def login_user():
    login_name = input(print("Insira o nome de usuario, por favor: \n"))
    login_senha = input(print("Insira a senha, por favor: \n"))
    return login_name, login_senha

def login_check():
    login_name, login_senha = login_user()
    if login_name == login and login_senha == senha:
        return("Login realizado com sucesso!")
    elif login_name != login and login_senha == senha:
        return("Nome de usuário incorreto.")
    elif login_name == login and login_senha != senha:
        return("Senha incorreta.")
    else:
        return("Login ou senha incorretos. Tente novamente.")
    
def main():
    resultado = login_check()
    print(resultado)            

if __name__ == "__main__":
    main()  