def validate_cpf(cpf):
    """
    Validate a Brazilian CPF number.

    A CPF is a national identification number used in Brazil, composed of 11 digits.
    The last two digits are check digits, which are calculated using the first nine digits.
    """
    # Remove non-digit characters from the input
    cpf = ''.join(filter(str.isdigit, str(cpf)))

    # Check for length
    if len(cpf) != 11:
        return False

    # Check for repeated digits
    if cpf in ("00000000000", "11111111111", "22222222222", "33333333333", "44444444444", "55555555555", "66666666666", "77777777777", "88888888888", "99999999999"):
        return False

    # Calculate the first check digit
    sum1 = sum(int(cpf[i]) * ((10 - i) for i in range(9)) )
    digit1 = (sum1 * 10) % 11
    digit1 = 0 if digit1 == 10 else digit1

    # Calculate the second check digit
    sum2 = sum(int(cpf[i]) * ((11 - i) for i in range(10)))
    digit2 = (sum2 * 10) % 11
    digit2 = 0 if digit2 == 10 else digit2

    # Compare check digits with the last two digits of the CPF
    return cpf[-2:] == '{}{}'.format(digit1, digit2)

# Example usage
if __name__ == '__main__':
    test_cpfs = ['12345678909', '11144477735']
    for cpf in test_cpfs:
        print(f'CPF {cpf} is valid: {validate_cpf(cpf)})