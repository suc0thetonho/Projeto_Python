from cadastro_login import salvar_cadastro, cadastro
from interface_usuario import interface_usuario
from clear import clear_screen
import time

def cadastro_interface():
    clear_screen()
    print("                     CADASTRO")
    print("=============================================")

    while True:
        login = input("Digite aqui o login que você deseja cadastrar: ")
        senha = input("Digite aqui a senha que você deseja usar neste cadastro: ")

        if not login or not senha:
            time.sleep(2)
            print("Erro: login ou senha não podem estar vazios. Tente novamente.")
            continue

        if len(senha) < 8:
            print("Erro: a senha deve ter pelo menos 8 caracteres. Tente novamente.")
            time.sleep(1)
            clear_screen()
            continue

        # Verifica se o login já existe
        for usuario in cadastro:
            if usuario["login"] == login:
                print("Erro: Este login já existe. Tente outro.")
                time.sleep(1)
                clear_screen()
                return

        # Salvar e adicionar ao cadastro
        salvar_cadastro(login, senha)
        print("Cadastro realizado com sucesso!")
        time.sleep(1)
        clear_screen()
        break
    

def login_interface():
    clear_screen()
    print("                     LOGIN")
    print("=============================================")

    while True:
        login = input("Digite seu login: ")
        senha = input("Digite sua senha: ")

        if not login or not senha:
            print("Login e senha não podem estar vazios! Tente novamente.")
            time.sleep(1)
            clear_screen()
            continue

        if len(senha) < 8:
            print("A senha deve ter pelo menos 8 caracteres!")
            time.sleep(1)
            clear_screen()
            continue
        
        # Verificar credenciais no cadastro
        for usuario in cadastro:
            if usuario["login"] == login and usuario["senha"] == senha:
                print("Login realizado com sucesso!")
                time.sleep(1)
                clear_screen()
                interface_usuario(login)
        else:
            print("Login ou senha incorretos! Tente novamente.")
            time.sleep(1)
            clear_screen()
            continue  # Permite nova tentativa no loop interno