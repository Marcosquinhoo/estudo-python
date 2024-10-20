opcao = -1

while opcao != 0:
      opcao = int(input("[1] sacar \n[2] extrato \n[0] sair \n: "))
      
      if opcao == 1:
          print('sacando...')
          
      elif opcao == 2:
            print('Exibindo o extrato...')
            
      elif opcao == 0:
            print('fim do prgrama...')
            
      else:
           print("Comando invalido")