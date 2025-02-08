"""Deposito saque e exibir extrato

deposito = apenas valores positivos, todos os depositos devem ser armazenados em uma variavel e exibidos na operaçao de extrato
saque = permitido apenas 3 sauqes por dia com limite de 500 reais por saque , caso nao tenha saldo em conta, deve informar por mensagem que nao sera possivel sacar por falta de dinheiro, todos os saeus devem ser armazenados em uma variavel e exibidos na operação de extrato
extrato = listar todos os depositos e saques realizados, e no fim apresentar o saldo atual da conta R$ xxx.xx

"""
from datetime import datetime

menu = f"""
        Bem vinda de volta ! 
    Dia: {datetime.now()} 
    
    Escolha uma das opções abaixo:

    1 - Exibir o saldo da sua conta
    2 - Deposito
    3 - Saque
    4 - Exibir extrato
    5 - Sair

"""
saldo = 0
limite = 500
extrato = [] 
limite_saque = 3

def depositar (valor):
    global saldo
    saldo += valor
   


def sacar (valor):
    global saldo
    saldo -= valor


while True:
    print(menu)
    decisao_usuario = int(input('Sua escolha: '))
    
    match decisao_usuario:
        case 1:
            print(f'Seu saldo atual é: R${saldo:.2f}')
        

        case 2: # deposito
            valor_do_deposito = float(input('Valor que você gostaria de depositar:R$ '))

            if valor_do_deposito > 0:
                depositar(valor = valor_do_deposito)
                extrato.append(('deposito', valor_do_deposito))
            
            else:
                print('Não é possível depositar esse valor, tente novamente')


        case 3: # saque
            valor_do_saque = float(input('Valor você gostaria de sacar:R$ '))
            if limite_saque == 0:
                print('Não foi possível realizar seu saue. Limite de saque diário foi atingido')
                continue
            
            if valor_do_saque < saldo and valor_do_saque <= 500:
                sacar(valor = valor_do_saque)
                limite_saque -= 1
                extrato.append(('saque', valor_do_saque))
                print(f'Saque de R${valor_do_saque:.2f} realizado com sucesso')
            elif valor_do_saque > 500:
                print('Não é possível sacar esse valor, tente um valor abaixo de R$500.00')
            elif valor_do_saque > saldo:
                print('Saldo insuficiente')
                
        case 4:
            print('Extrato')
            
            for operacao, valor in extrato:
                print(f'{operacao}: R${valor:.2f}')
            
            
         
        
        
        case 5:
            print('Até mais ;)')
            break