import os
import time


cadastro = []


#salvar o cadatro em um arquivo
def salvar_cadastro(login, senha):
    with open("user_login.txt", "a") as arquivo:
        arquivo.write(f"{login}:{senha}\n")
        
    cadastro.append({"login": login, "senha": senha})

#colocar os arquivos numa lista
def load_cadastros():
    global cadastro
    cadastro.clear()  # Limpa a lista antes de carregar os cadastros

    file_path = os.path.join(os.getcwd(), 'user_login.txt')
    retries = 0

    while retries < 3:  # Tenta 3 vezes carregar o arquivo
        try:
            with open(file_path, 'r') as arquivo:
                for linha in arquivo:
                    linha = linha.strip().split(":", 1)
                    if len(linha) == 2:
                        login, senha = linha
                        cadastro.append({"login": login.strip(), "senha": senha.strip()})
            break  # Se carregado com sucesso, sai do loop
        except FileNotFoundError:
            time.sleep(1)  # Aguarda 1 segundo antes de tentar novamente
            retries += 1
    

#def deposito():



    