def validate_cpf(cpf):
    """
    Validação de CPF
    """
    cpf = cpf.replace('.', '').replace('-', '')

    if len(cpf) != 11 or cpf.isdigit() == False:
        return False

    # Primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += (10 - i) * int(cpf[i])

    resto = soma % 11

    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto

    # Segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += (11 - i) * int(cpf[i])

    resto = soma % 11

    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto

    if int(cpf[9]) == digito1 and int(cpf[10]) == digito2:
        return True
    else:
        return False

def validate_cnpj(cnpj):
    """
    Validação de CNPJ
    """
    cnpj = cnpj.replace('.', '').replace('-', '').replace('/', '')

    if len(cnpj) != 14 or cnpj.isdigit() == False:
        return False

    # Primeiro dígito verificador
    soma = 0
    peso = 5

    for i in range(12):
        soma += int(cnpj[i]) * peso
        peso -= 1
        if peso == 1:
            peso = 9

    resto = soma % 11

    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto

    # Segundo dígito verificador
    soma = 0
    peso = 6

    for i in range(13):
        soma += int(cnpj[i]) * peso
        peso -= 1
        if peso == 1:
            peso = 9

    resto = soma % 11

    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto

    if int(cnpj[12]) == digito1 and int(cnpj[13]) == digito2:
        return True
    else:
        return False
