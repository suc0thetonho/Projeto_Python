


cadastro = []


#salvar o cadatro em um arquivo
def salvar_cadastro(login, senha):
    with open("user_login.txt", "a") as arquivo:
        arquivo.write(f"{login}:{senha}\n")

#colocar os arquivos numa lista
def load_cadastros():
    try:
        with open('user_logins.txt', 'r') as arquivo:
            for linha in arquivo:
                linha = linha.strip().split(":", 1)
                if len(linha) == 2:
                    login, senha = linha
                    cadastro.append({"login": login.strip(), "senha": senha.strip()})
    except FileNotFoundError:
        pass

def deposito():
    