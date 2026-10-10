"""Geração e validação de CNPJ (algoritmo dos dígitos verificadores)."""

import re
import random
import string


class CnpjInvalido(ValueError):
    """Entrada de CNPJ em formato inadequado""" 


def limpar_cnpj(cnpj: str) -> str:
    """Remove máscara e espaços; mantém apenas dígitos."""
    return re.sub(r"[^a-zA-Z0-9]", "", str(cnpj or "")).upper()

def formatar_cnpj(cnpj: str) -> str:
    digits = limpar_cnpj(cnpj)
    if len(digits) != 14:
        raise CnpjInvalido("CNPJ deve ter 14 digitos") 
    return f"{digits[:2]}.{digits[2:5]}.{digits[5:8]}/{digits[8:12]}-{digits[12:14]}"

def calcular_valores_alfanumericos(cnpj: str) -> list:
    return [ord(char) - 48 if char.isalpha() else int(char) for char in limpar_cnpj(cnpj)]

def _digito_verificador(base: list) -> str:
    if len(base) == 12:
        pesos = [5,4,3,2,9,8,7,6,5,4,3,2]
    elif len(base) == 13:
        pesos = [6,5,4,3,2,9,8,7,6,5,4,3,2]
    else:
        raise ValueError("A lista de valores parciais deve conter 12 ou 13 elementos")

    total = sum([d * p for d,p in zip(base, pesos)])
    resto = total % 11
    return "0" if resto < 2 else str(11 - resto)

def calcular_digitos(doze_digitos: list) -> list:
    dv1 = _digito_verificador(doze_digitos)
    dv2 = _digito_verificador(doze_digitos+[int(dv1)])

    return [dv1, dv2]

def validar_cnpj(cnpj:str) -> bool:
    cnpj_limpo = (limpar_cnpj(cnpj))
    if not cnpj_limpo:
        raise CnpjInvalido("Informe um CNPJ")

    if len(cnpj_limpo) != 14:
        raise CnpjInvalido("O CNPJ deve conter 14 digitos")

    base_calculo = calcular_valores_alfanumericos(cnpj_limpo[:12])

    digitos_calculados = calcular_digitos(base_calculo)

    dvs_str = "".join(digitos_calculados)

    cnpj_esperado = cnpj_limpo[:12] + dvs_str
    return cnpj_limpo == cnpj_esperado

def criar_cnpj(formatado: bool = True) -> str:
    caracteres = string.ascii_letters + string.digits
    resultado = list(random.choices(caracteres, k=12))

    digitos_no_ascii = calcular_valores_alfanumericos(resultado)
    digitos = calcular_digitos(digitos_no_ascii)
    cnpj = "".join(resultado+digitos)
    print(len(cnpj))
    return formatar_cnpj(cnpj) if formatado == True else cnpj


if __name__ == "__main__":
    cnpj_original = "EN.S9A.OGM/Q4BJ-40"
    
    # 1. Formata para exibição na tela
    cnpj_formatado = formatar_cnpj(cnpj_original)
    print("CNPJ Formatado:", cnpj_formatado)

    # 2. Transforma o CNPJ inteiro (14 dígitos) em lista de inteiros
    cnpj_calculado = calcular_valores_alfanumericos(cnpj_original)
    print("Lista de inteiros (14):", cnpj_calculado)

    # 3. EXTRAÇÃO CORRETA: Pega os 12 primeiros números direto da lista calculada!
    base = cnpj_calculado[:12]
    print("Tamanho da base:", len(base))  # Agora vai dar 12 com certeza!
    print("Lista da Base (12):", base)

    # 4. Calcula o primeiro dígito verificador
    dv1 = _digito_verificador(base)
    print("Primeiro DV calculado:", dv1)
    
    # 5. Calcula o segundo dígito verificador (passando a base + dv1 convertido em int)
    base_com_dv1 = base + [int(dv1)]
    dv2 = _digito_verificador(base_com_dv1)
    print("Segundo DV calculado:", dv2)

    print("cnpj valido" if validar_cnpj(cnpj_original) else "cnpj invalido")

    print("Cnpj gerado =" + criar_cnpj())