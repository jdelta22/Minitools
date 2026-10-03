from django.shortcuts import render
from .utils.cpf import Criar_CPF, Validar_CPF

# Create your views here.
def Cpf(request):
    cpf_enviado = ""
    resultado_validação = None

    if request.method == 'POST':
        cpf_enviado = request.POST.get("cpf", "")
        if Validar_CPF(cpf_enviado):
            resultado_validação = "CPF Valido! ✅"
        else:
            resultado_validação = "CPF Invalido! ❌"

    cpf_gerado = None
    if "gerar" in request.GET:
        cpf_gerado = Criar_CPF()

    context = {
        "resultado": resultado_validação,
        "cpf_digitado": cpf_enviado,
        "cpf_gerado": cpf_gerado
    }

    return render(request, "DocumentsValidator/pages/CPF.html", context)