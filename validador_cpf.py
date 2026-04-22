recebe = input('Seu CPF: ');
recebe = recebe.replace('.','').replace('-','');
validacao = False;

# Check if the length of the CPF is 11 digits
if len(recebe) != 11:
    print('CPF invalido');
else:
    # Check if the input contains only digits
    if recebe.isdigit():
        cpf = [];
        validacao = True;
        # Convert each character to an integer and store in the cpf list
        for n in recebe:
            a = int(n);
            cpf.append(a);
    else:
        print('CPF invalido');

# Function to perform CPF validation calculations

def CalculoCPF(qntd, mult):
    soma = 0;
    # Sum the multiplication of each digit by a decreasing multiplier
    for c in range(qntd):
        calculo = cpf[c] * mult;
        soma += calculo;
        mult -= 1;
    resto = soma % 11;
    # Calculate the verification digit
    if resto >= 2:
        resto = 11 - resto;
    else:
        resto = 0;

    # Compare the calculated verification digit with the actual stored digit
    if resto != cpf[qntd]:
        print('CPF invalido!');
    else:
        # Check if all digits in the CPF are the same
        if cpf.count(cpf[0]) == 11:
            print('CPF invalido!');
        else:
            return True;

# First step of validation using the first 9 digits
if validacao:
    passo_1 = CalculoCPF(9, 10);
    # Second step of validation using the first 10 digits
    if passo_1:
        passo_2 = CalculoCPF(10, 11);
        # If both validations pass, the CPF is valid
        if passo_2:
            print('Seu CPF é valido!')