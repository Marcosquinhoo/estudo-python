conta_normal = False
conta_universitaria = False

saldo = 2000
saque = 1500
cheque_especial = 450


if conta_normal:
    if saldo >= saque:
        print("saque realizado com sucesso!")
        
    elif saque <= (saldo + cheque_especial):
         print("saque realizado com cheque especial!")    
         
    else:
        print("Voce não tem saldo suficiente, em todas as contas")
        
elif conta_universitaria:
    if saldo >= saque:
         print("saque realizado com conta universitaria")
         
    else:
        print("saldo insuficiente ")

else:
    print("Sistema não reconheceu o tipo conta, entre em contato com seu banco !!  ")