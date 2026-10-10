from django.test import SimpleTestCase, Client
from django.urls import reverse

from documents_validator.utils.cpf import (
    CpfInvalido,
    criar_cpf,
    limpar_cpf,
    validar_cpf,
)


class CpfUtilsTests(SimpleTestCase):
    def test_limpar_mascara(self):
        self.assertEqual(limpar_cpf("529.982.247-25"), "52998224725")

    def test_validar_com_mascara(self):
        cpf = criar_cpf(formatado=True)
        self.assertTrue(validar_cpf(cpf))

    def test_validar_sem_mascara(self):
        cpf = criar_cpf(formatado=False)
        self.assertTrue(validar_cpf(cpf))

    def test_rejeita_digitos_iguais(self):
        self.assertFalse(validar_cpf("111.111.111-11"))

    def test_entrada_invalida(self):
        with self.assertRaises(CpfInvalido):
            validar_cpf("123")


class CpfViewTests(SimpleTestCase):
    def setUp(self):
        self.client = Client()

    def test_pagina_cpf(self):
        response = self.client.get(reverse("documents_validator:cpf_validator"))
        self.assertEqual(response.status_code, 200)

    def test_gerar_cpf(self):
        response = self.client.get(
            reverse("documents_validator:cpf_validator"),
            {"gerar": "1"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context["cpf_gerado"])
