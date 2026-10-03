from django.shortcuts import render
from .utils.calc import avaliar, ExpressaoInvalida

# Create your views here.
def Calculator(request):
    ctx ={}

    if request.method == 'POST':
        expr = request.POST.get("expressao", "")
        ctx["expressao"] = expr
        try:
            ctx["resultado"] = avaliar(expr)
        except ZeroDivisionError:
            ctx["erro"] = "divisão por zero"
        except (ExpressaoInvalida, ValueError, OverflowError, TypeError) as e:
            ctx["erro"] = str(e) or "Expressão invalida"

    return render(request, 'calculator/pages/calculator.html', ctx)