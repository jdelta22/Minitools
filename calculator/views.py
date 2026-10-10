from django.shortcuts import render

from .utils.calc import ExpressaoInvalida, avaliar


def calculator_view(request):
    ctx = {}

    if request.method == "POST":
        expr = request.POST.get("expressao", "")
        ctx["expressao"] = expr
        try:
            ctx["resultado"] = avaliar(expr)
        except ZeroDivisionError:
            ctx["erro"] = "Divisão por zero."
        except (ExpressaoInvalida, ValueError, OverflowError, TypeError) as e:
            ctx["erro"] = str(e) or "Expressão inválida."

    return render(request, "calculator/pages/calculator.html", ctx)
