from datetime import date

'''FUNÇÃO DE CRIAÇÃO DO USUÁRIO
    Parâmetros: 
    nome, 
    data de nascimento
    CPF, 
    logradouro,
    bairro,
    cidade, 
    sigla do estado
'''
def criar_usuario(nome, data_nascimento, cpf, logradouro, bairro, cidade, sigla_estado):
    global usuarios
    
    if not cpf.isdigit() or len(cpf) != 11:
        raise ValueError("O campo CPF deve conter apenas números e ter 11 dígitos.")
        #Para a função caso o CPF não seja válido
    
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            raise ValueError('Usuário já cadastrado')
    
    if not len(sigla_estado) == 2:
        raise ValueError('A sigla do estado só pode conter 2 letras')
    
    endereco = f'{logradouro} - {bairro} - {cidade}/{sigla_estado}' 
            
    novo_usuario ={
            "nome": nome, 
            "data_nascimento": data_nascimento, 
            "cpf": cpf, 
            "endereco": endereco
        }
    
    usuarios.append(novo_usuario)   
    print(f'Usuário {nome} cadastrado com sucesso!')   
    return novo_usuario
 
'''FUNÇÃO DE CRIAÇÃO DA CONTA CORRENTE
    Parâmetros: 
    nome, 
    data de nascimento
    CPF, 
    logradouro,
    bairro,
    cidade, 
    sigla do estado
'''           
            
def criar_conta_corrente(cpf, usuarios, contas_correntes):
    AGENCIA = "0001"
    cliente = {}
    
    numero_conta = 0
    
    #Pega o primeiro usuário que corresponde ao cpf, caso não corresponda constará None
    cliente = next((usuario for usuario in usuarios if usuario['cpf'] == cpf), None)
    
    if not cliente:
        raise ValueError("Usuário não encontrado. Crie o usuário antes de criar a conta.")
    
    conta_corrente ={
        "agencia": AGENCIA,
        "numero_conta": numero_conta,
        "usuario": cliente,
        "saldo": 0.0,
        "transacoes_diarias": []
    }
    
    numero_conta += 1
    
    contas_correntes.append(conta_corrente)
    print(f"Conta do usuário {cliente['nome']} cadastrado com sucesso!")
    return conta_corrente



def deposito(valor, numero_conta, contas_correntes, /):
    if not isinstance(numero_conta, int):
        raise TypeError("⚠️ O número da conta deve ser um inteiro.")   
    
    if valor <= 0:
        raise ValueError("O valor inserido não pode ser igual ou menor que zero")
    
    
    #APAGAR QUANDO FOR POSTAR
    '''conta_encontrada é o mesmo dicionário que está dentro de contas_correntes.

    Logo, se você alterar algo dentro de conta_encontrada, está automaticamente alterando o mesmo objeto dentro da lista.'''
    
      
    conta_encontrada = next((conta for conta in contas_correntes if conta['numero_conta'] == conta), None)
    
    if conta_encontrada is None:
        raise ValueError("Conta não localizada. Verifique o número informado.")
            
    conta_encontrada['saldo'] += valor
    
    print(f"Deposito de R$ {valor:.2f} efetuado com sucesso na conta {numero_conta}!")
    print(f"O seu saldo atual é {'saldo'}:.2f")
    
    return conta_encontrada['saldo']
    

    
def saque(*, numero_conta, valor, contas_correntes):
    if not isinstance(numero_conta, int):
        raise TypeError("⚠️ O número da conta deve ser um inteiro.")
    
    if valor <= 0:
        raise ValueError("O valor inserido não pode ser igual ou menor que zero")

    conta_encontrada = next((conta for conta in contas_correntes if conta['numero_conta'] == numero_conta), None)
    
    if conta_encontrada is None:
        raise ValueError("Conta não localizada. Verifique o número informado.")
    
    if conta_encontrada['saldo'] < valor:
        raise ValueError("Você não tem saldo suficiente.")
    
    #retorna uma lista com as datas de saque do dia da operação
    saques_hoje = [saq for saq in conta_encontrada.get('transacoes_diarias',[]) if saq['data'] == date.today().isoformat()] #[] retorna uma lista vazia caso não encontre o valor de transacoes_diarias
    
    quantidade_saques = len(saques_hoje)
    
    if quantidade_saques < 5:
        conta_encontrada['saldo'] -= valor
        conta_encontrada.setdefault('transacoes_diarias', []).append({
            "valor": valor,
            "data": date.today().isoformat()
        })
        print(f"Saque de R$ {valor:.2f} realizado com sucesso. Saldo atual: R$ {conta_encontrada['saldo']:.2f}")

    else:
        print("Quantidade de saques de hoje excedidos")
        

def extrato(nome, /, *, numero_conta, contas_correntes):
    if not isinstance(numero_conta, int):
        raise TypeError("⚠️ O número da conta deve ser um inteiro.")
    
    conta_encontrada = next((conta for conta in contas_correntes if conta['numero_conta'] == numero_conta), None)
    
    
    
    

''' elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")    '''
    
usuarios = []
contas_correntes = []
numero_conta = 1                 

criar_usuario("Aline","22/06/1993", "05827254503", "Humberto", "Rafael", "Salvador", "BA")

criar_usuario("Lucas","22/06/1993", "05527254508", "Humberto", "Rafael", "Salvador", "BA")

print(usuarios) 

criar_conta_corrente('05827254503')

criar_conta_corrente('05527254508')

print(contas_correntes)