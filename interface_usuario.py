import time
from saque_deposito import saque, deposito
from clear import clear_screen

saldo = 0
def interface_usuario(login):
      global saldo
      while True:
      
            print("TELA USUARIO\n"
          "=================================\n\n"
          f"Seja bem vindo(a) {login}\n"
          F"Saldo na conta: R$ {saldo}\n")
            user_options = int(input("O que deseja fazer?\n"
                             "1 - Saque\n"
                             "2 - Deposito\n"
                             "3 - Pix\n"
                             "4 - Transferencia\n"
                             "5 - Voltar para o menu\n"
                             "Selecione aqui a opção que você deseja -------> "))
            clear_screen()
            
            #opção para sacar
            if(user_options == 1 and saldo <= 0):
                  print(f"Não é possivel realizar o saque devido ao usuario {login}, não possuir nenhum saldo na conta\n"
              "para realizar um saque, realize um deposito antes")
                  time.sleep(1.5)
                  clear_screen()
                  interface_usuario(login)
            elif(user_options == 1 and saldo > 0):
                  saldo_antigo = saldo
                  saldo = saque(saldo)
                  if (saldo < 0):
                        print("o valor que você deseja sacar é muito alto, comparado ao valor que você possui na conta\n")
                        saldo = saldo_antigo
                        time.sleep(1)
                        clear_screen()
                        interface_usuario(login)
                  else:
                        print("Dinheiro sacado com sucesso")
                        time.sleep(1)
                        interface_usuario(login)

            #opção para depositar
            elif(user_options == 2):
                  saldo = deposito(saldo)
                  print("Dinheiro depositado com sucesso")
                  time.sleep(1)
                  clear_screen()
                  interface_usuario(login)
    

    