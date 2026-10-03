import ast
import math
import operator as op

OPERADORES = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.USub: op.neg,
    ast.UAdd: op.pos,
}

MAX_FATORIAL= 500

def fatorial(n):
    if not isinstance(n, int):
        if isinstance(n, float) and n.is_integer():
            n = int(n)
        else:
            raise ExpressaoInvalida("Fatorial exige um inteiro.")
    if n < 0:
        raise ExpressaoInvalida("Fatorial de número negativo não existe.")
    if n > MAX_FATORIAL:
        raise ExpressaoInvalida(f"Fatorial limitado a {MAX_FATORIAL}.")
    return math.factorial(n)

FUNCOES = {
    "sqrt": math.sqrt,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "log": math.log,
    "abs": abs,
    "round": round,
    "fat": fatorial,
}

CONSTANTES = {"pi": math.pi, "e": math.e,}

MAX_EXPOENTE = 1000


class ExpressaoInvalida(ValueError):
    pass


def avaliar(expressao: str):
    if len(expressao) > 200:
        raise ExpressaoInvalida("Expressão muito longa.")
    try:
        arvore = ast.parse(expressao.replace("^", "**"), mode="eval")
    except SyntaxError:
        raise ExpressaoInvalida("Sintaxe inválida.")
    return _eval(arvore.body)


def _eval(no):
    if isinstance(no, ast.Constant) and isinstance(no.value, (int, float)):
        return no.value

    if isinstance(no, ast.Name) and no.id in CONSTANTES:
        return CONSTANTES[no.id]

    if isinstance(no, ast.BinOp) and type(no.op) in OPERADORES:
        esq, dir_ = _eval(no.left), _eval(no.right)
        if isinstance(no.op, ast.Pow) and abs(dir_) > MAX_EXPOENTE:
            raise ExpressaoInvalida("Expoente muito grande.")
        return OPERADORES[type(no.op)](esq, dir_)

    if isinstance(no, ast.UnaryOp) and type(no.op) in OPERADORES:
        return OPERADORES[type(no.op)](_eval(no.operand))

    if (
        isinstance(no, ast.Call)
        and isinstance(no.func, ast.Name)
        and no.func.id in FUNCOES
        and not no.keywords
    ):
        return FUNCOES[no.func.id](*[_eval(a) for a in no.args])

    raise ExpressaoInvalida("Elemento não permitido na expressão.")