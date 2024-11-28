import os

def clear_screen():
    # Detecta o sistema operacional e limpa a tela
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Linux, macOS, etc.
        os.system('clear')