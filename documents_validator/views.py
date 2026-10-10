from django.shortcuts import render

from .utils.cpf import CpfInvalido, criar_cpf, validar_cpf
from .utils.cnpj import CnpjInvalido, criar_cnpj, validar_cnpj


def cpf_validator(request):
    cpf_digitado = ""
    resultado = None
    resultado_ok = None
    cpf_gerado = None

    if request.method == "POST":
        cpf_digitado = request.POST.get("cpf", "").strip()
        try:
            if validar_cpf(cpf_digitado):
                resultado = "CPF válido."
                resultado_ok = True
            else:
                resultado = "CPF inválido."
                resultado_ok = False
        except CpfInvalido as exc:
            resultado = str(exc)
            resultado_ok = False

    if request.GET.get("gerar"):
        cpf_gerado = criar_cpf()

    context = {
        "resultado": resultado,
        "resultado_ok": resultado_ok,
        "cpf_digitado": cpf_digitado,
        "cpf_gerado": cpf_gerado,
    }
    return render(request, "documents_validator/pages/cpf.html", context)

def cnpj_validator(request):
    cnpj_digitado = ""
    resultado = None
    resultado_ok = None
    cnpj_gerado = None

    if request.method == "POST":
        cnpj_digitado = request.POST.get("cnpj", "").strip()
        try:
            if validar_cnpj(cnpj_digitado):
                    resultado = "CNPJ válido."
                    resultado_ok = True
            else:
                resultado = "CNPJ invalido"
                resultado_ok = False
        except CnpjInvalido as e:
            resultado = str(e)
            resultado_ok = False

    if request.GET.get("gerar"): 
        cnpj_gerado = criar_cnpj()

    context = {
            "resultado": resultado,
            "resultado_ok": resultado_ok,
            "cnpj_digitado": cnpj_digitado,
            "cnpj_gerado": cnpj_gerado,
        }
    return render(request, "documents_validator/pages/cnpj.html", context)
