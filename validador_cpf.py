recebe = input('Seu CPF: ')
recebe = recebe.replace('.','').replace('-','')
validacao = False

if len(recebe) != 11:
    print('CPF invalido')
else:
    if recebe.isdigit():
        cpf = []
        validacao = True
        for n in recebe:
            a = int(n)
            cpf.append(a)
    else:
        print('CPF invalido')

d = 10
soma = 0
verifica = False
if validacao:
    for c in range(9):
        calculo = cpf[c]*d
        soma += calculo
        d -= 1
    resto = soma % 11
    if resto >= 2:
        resto = 11 - resto
    else:
        resto = 0
    if resto != cpf[9]:
        print('CPF invalido!')
    else:
        verifica = True
    if verifica:
        soma = 0
        d = 11
        for c in range(10):
            calculo = cpf[c]*d
            soma += calculo
            d -= 1
        resto = soma % 11
        if resto >= 2:
            resto = 11 - resto
        else:
            resto = 0
        if resto != cpf[10]:
            print('CPF invalido!')
        else:
            if cpf.count(cpf[0]) == 11:
                print('CPF invalido!')
            else:
                print('Seu CPF é valido!')