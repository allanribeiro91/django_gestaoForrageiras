def valida_cpf(cpf):
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Verifica se o CPF tem todos os dígitos iguais, o que o torna inválido
    if cpf == cpf[0] * 11:
        return False

    # Cálculo do primeiro dígito verificador
    soma = sum(int(a) * b for a, b in zip(cpf[:-2], range(10, 1, -1)))
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto

    # Cálculo do segundo dígito verificador
    soma = sum(int(a) * b for a, b in zip(cpf[:-1], range(11, 1, -1)))
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto

    return cpf[-2:] == f"{digito1}{digito2}"


