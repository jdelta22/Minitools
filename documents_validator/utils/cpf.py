"""Geração e validação de CPF (algoritmo dos dígitos verificadores)."""

from __future__ import annotations

import random
import re


class CpfInvalido(ValueError):
    """Entrada de CPF em formato inadequado."""


def limpar_cpf(cpf: str) -> str:
    """Remove máscara e espaços; mantém apenas dígitos."""
    return re.sub(r"\D", "", str(cpf or ""))


def formatar_cpf(cpf: str) -> str:
    """Formata 11 dígitos como 000.000.000-00."""
    digits = limpar_cpf(cpf)
    if len(digits) != 11:
        raise CpfInvalido("CPF deve ter 11 dígitos.")
    return f"{digits[:3]}.{digits[3:6]}.{digits[6:9]}-{digits[9:]}"


def _digito_verificador(base: str, peso_inicial: int) -> str:
    total = sum(int(d) * peso for d, peso in zip(base, range(peso_inicial, 1, -1)))
    resto = total % 11
    return "0" if resto < 2 else str(11 - resto)


def _calcular_digitos(nove_digitos: str) -> str:
    d1 = _digito_verificador(nove_digitos, 10)
    d2 = _digito_verificador(nove_digitos + d1, 11)
    return d1 + d2


def criar_cpf(formatado: bool = True) -> str:
    """Gera um CPF com dígitos verificadores válidos (uso em testes)."""
    while True:
        nove = f"{random.randint(0, 999_999_999):09d}"
        if len(set(nove)) > 1:
            break
    cpf = nove + _calcular_digitos(nove)
    return formatar_cpf(cpf) if formatado else cpf


def validar_cpf(cpf: str) -> bool:
    """
    Retorna True se o CPF for válido.
    Aceita com ou sem máscara. Levanta CpfInvalido se a entrada for vazia
    ou não tiver exatamente 11 dígitos após limpeza.
    """
    digits = limpar_cpf(cpf)
    if not digits:
        raise CpfInvalido("Informe um CPF.")
    if len(digits) != 11:
        raise CpfInvalido("CPF deve ter 11 dígitos.")
    if digits == digits[0] * 11:
        return False
    return digits == digits[:9] + _calcular_digitos(digits[:9])
