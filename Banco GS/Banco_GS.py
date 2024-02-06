Slogan = "= Banco GS ="
menu = '''
Bem vindo ao banco GS
Digite:
[d] Deposito
[s] Sacar
[e] Extrato
[q] Sair

Informe a operacao desejada: '''

saldo = 100
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)
    if  opcao == 'd':
        print(Slogan)
        valor = float(input("Informe o valor do deposito: "))
        if valor>0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
            print("Operacao falhou o valor informado e invalido.")
    elif opcao == 's':
        print(Slogan)
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saque = numero_saque > LIMITE_SAQUE
        
        if excedeu_saldo:
            print("Operacao falhou! Voce nao tem saldo suficiente.")
        if excedeu_limite:
            print("Operacao falhou! O valor e maior que R$500.")
        if excedeu_saque:
            print("Operacao falhou! Numero de saques excedido.")
            
        elif valor >0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saque += 1
        else:
            print("Operacao falhou! Valor informado e invalido.")
    elif opcao == "e":
        print(Slogan)
        print("\n===== EXTRATO =====")
        print("Nenhum movimentacao realizada." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("=====================")
    elif opcao == 'q':
        break
    else:
        print("Operacao invalida! Tente novamente.")
