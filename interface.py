from cadastro_login import cadastro, load_cadastros
from clear import clear_screen
from interface_options import cadastro_interface, login_interface


def interface():
    clear_screen()
    global cadastro  
    load_cadastros()  
    log_sucess = False
    

    while not log_sucess:
        
        print("             TELA DE MENU")
        interface_option = int(input("=============================================\n"
                                  "DIGITE 1 PARA CADASTRAR O USUÁRIO\n"
                                  "DIGITE 2 PARA FAZER LOGIN NO USUÁRIO\n"
                                  "DIGITE 3 PARA SAIR\n"
                                  "SELECIONE AQUI: "))

        if interface_option == 1:
            clear_screen()
            cadastro_interface()

        elif interface_option == 2:
            clear_screen()
            login_interface()
            
        elif interface_option == 3:
            break
