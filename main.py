from defs import salvar_cadastro, cadastro, load_cadastros

log_sucess = False

while not log_sucess:
    interface = int(input("==========================\n"
                      "DIGITE 1 PARA CADASTRAR O USUARIO\n"
                      "DIGITE 2 PARA FAZER LOGIN NO USUARIO\n"
                      "SELECIONE AQUI: "))

    if (interface == 1):
        while(True):
            login = input("Digite aqui o login que você deseja cadastrar: ")
            senha = input("Digite aqui a senha que que você deseja usar neste cadastro: ")
            if (not login) or (not senha):
                print("senha ou login não adicionado\n"
                    "tente novamente")
                login = input("Digite aqui o login que você deseja cadastrar: ")
                senha = input("Digite aqui a senha que que você deseja usar neste cadastro: ")
            if(len(senha) < 8):
                print("Senha não está no tamanho correto\n"
                "Tente novamente")
                senha = input("Digite aqui a senha que que você deseja usar neste cadastro: ")

            salvar_cadastro(login, senha)
            cadastro.append({"login": login, "senha": senha})
            print(f"Cadastro realizado com sucesso!")
            break

    elif interface == 2:
        while True:
            login = input(f"Digite seu login: ")
            senha = input(f"Digite sua senha: ")

            if not login or not senha:
                print(f"Login e senha não podem estar vazios! Tente novamente.")
                continue 

            if len(senha) < 8:
                print(f"A senha deve ter pelo menos 8 caracteres!")
                continue

            for usuario in cadastro:
                if usuario["login"] == login and usuario["senha"] == senha:
                    print(f"Login realizado com sucesso!")
                    log_sucess = True
                    break
            else:
                print(f"Login ou senha incorretos!")
            break

    load_cadastros()