import random

def Criar_CPF():
    numero_9_digitos = str(random.randint(100000000, 999999999))

    # primeiro digito verificador
    soma_ver_1 = 0
    controle =10
    for digit in numero_9_digitos:
        soma_ver_1 += int(digit)*controle
        controle -=1
    resto = soma_ver_1%11

    if resto == 0 or resto == 1:
        digito_verificador_1 = str(0)
    else:
        digito_verificador_1 = str(11-resto)

    # segundo digito verificador
    numero_com_ver1 = numero_9_digitos+digito_verificador_1
    soma_ver_2 = 0
    controle =11
    for digit in numero_com_ver1:
        soma_ver_2 += int(digit)*controle
        controle -=1
    
    resto2 = soma_ver_2%11

    if resto2 == 0 or resto2 == 1:
        digito_verificador_2 = str(0)
    else:
        digito_verificador_2 = str(11-resto2)

    # CPF retornado em forma de string
    Cpf = f"{numero_9_digitos}{digito_verificador_1}{digito_verificador_2}"

    return Cpf

class CPFinvalido(ValueError):
    pass

def Validar_CPF(cpf):
    if len(cpf) > 11:
        raise CPFinvalido("O formato do CPF não está adequado")
    else:
        cpf = str(cpf)

    
    cpf_para_verificar = cpf[:9:]

    # primeiro digito verificador
    soma_ver_1 = 0
    controle =10
    for digit in cpf_para_verificar:
        soma_ver_1 += int(digit)*controle
        controle -=1
    resto = soma_ver_1%11

    if resto == 0 or resto == 1:
        digito_verificador_1 = str(0)
    else:
        digito_verificador_1 = str(11-resto)

    # segundo digito verificador
    numero_com_ver1 = cpf_para_verificar+digito_verificador_1
    soma_ver_2 = 0
    controle =11
    for digit in numero_com_ver1:
        soma_ver_2 += int(digit)*controle
        controle -=1
    
    resto2 = soma_ver_2%11

    if resto2 == 0 or resto2 == 1:
        digito_verificador_2 = str(0)
    else:
        digito_verificador_2 = str(11-resto2)

    cpf_para_verificar = f"{cpf_para_verificar}{digito_verificador_1}{digito_verificador_2}"

    if cpf_para_verificar == cpf:
        return True
    else:
        return False

