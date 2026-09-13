def validar_cpf(text: str) -> bool:
    recebe = text.replace('.','').replace('-','').strip()
    
    if len(recebe) != 11 or not recebe.isdigit():
        raise ValueError('CPF invalido!')
    cpf = [int(n) for n in recebe]
    if len(set(cpf)) == 1:
        raise ValueError('CPF invalido!')
    
    def CalculoCPF(qntd, mult):
        soma = 0
        for c in range(qntd):
            calculo = cpf[c] * (mult - c)
            soma += calculo
        resto = soma % 11
        resto = 11 - resto if resto >= 2 else 0
        if resto != cpf[qntd]:
            raise ValueError('CPF invalido!')
    
    CalculoCPF(9,10)
    CalculoCPF(10,11)
    return True
