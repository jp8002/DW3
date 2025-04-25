from django.test import TestCase
from core.models import FeriadoModel
from datetime import datetime
from django.urls import reverse

class ModificarFeriadoViewTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(reverse("mod_feriado", args=[1]))

    def test_200_response(self):
        self.assertEqual(self.resp.status_code, 200)
    
    def test_template(self):
        self.assertTemplateUsed(self.resp, 'modificar_feriado.html')

class SemFeriadoTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_200_response(self):
        self.assertEqual(self.resp.status_code, 200)
    
    def test_texto(self):
        self.assertContains(self.resp, 'Não é feriado')
    
    def test_template(self):
        self.assertTemplateUsed(self.resp, 'feriado.html')
        self.assertTemplateNotUsed(self.resp, 'natal2.html')


class Feriado_TDD_Test(TestCase):
    def setUp(self):
        hoje = datetime.today()
        FeriadoModel.objects.create(nome='Dia do TDD',dia=hoje.day, mes=hoje.month)
        self.resp = self.client.get('/')

    def test_200_response(self):
        self.assertEqual(self.resp.status_code, 200)
    
    def test_texto(self):
        self.assertContains(self.resp, 'Dia do TDD')
    
    def test_template(self):
        self.assertTemplateUsed(self.resp, 'feriado.html')

class FeriadoModelTest(TestCase):
    def setUp(self):
        self.cadastro = FeriadoModel.objects.create(nome="Natal",dia=25,mes=12)
    
    def test_create(self):
        self.assertTrue(FeriadoModel.objects.exists())
    
    def test_name(self):
        feriado_no_banco = FeriadoModel.objects.first()
        self.assertEqual(feriado_no_banco.nome, 'Natal')


from django.urls import reverse
class ListarFeriadosViewTest(TestCase):

    def test_listar_feriados_vazio(self):
        response = self.client.get(reverse('listar_feriados'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listar_feriados.html')
        self.assertContains(response, 'Lista de Feriados')

    def test_listar_feriados_com_dados(self):
        FeriadoModel.objects.create(nome="Natal", dia=25, mes=12)
        FeriadoModel.objects.create(nome="Ano Novo", dia=1, mes=1)

        response = self.client.get(reverse('listar_feriados'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Natal")
        self.assertContains(response, "Ano Novo")


class AdicionarFeriadoViewTest(TestCase):

    def test_get_formulario_adicionar_feriado(self):
        response = self.client.get(reverse('add_feriado'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'adicionar_feriado.html')

    def test_post_dados_validos_cria_feriado(self):
        data = {'nome': 'Independência', 'dia': '7', 'mes': '9'}
        response = self.client.post(reverse('add_feriado'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(FeriadoModel.objects.filter(nome='INDEPENDÊNCIA').exists())

    def test_post_faltando_dados_retorna_200(self):
        response = self.client.post(reverse('add_feriado'), {'nome': '', 'dia': '', 'mes': ''})
        self.assertEqual(response.status_code, 200)

    def test_post_dia_ou_mes_fora_do_intervalo(self):
        response = self.client.post(reverse('add_feriado'), {'nome': 'Feriado', 'dia': '32', 'mes': '13'})
        self.assertEqual(response.status_code, 200)

    def test_post_dia_mes_nao_numerico(self):
        response = self.client.post(reverse('add_feriado'), {'nome': 'Teste', 'dia': 'dez', 'mes': 'jan'})
        self.assertEqual(response.status_code, 200)





