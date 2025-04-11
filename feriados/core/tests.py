from django.test import TestCase
from core.models import FeriadoModel
from datetime import datetime
# Create your tests here.

class feriadoTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')
        
    def test_200_response(self):
        self.assertEqual(200,self.resp.status_code)
        
    def test_texto(self):
        self.assertContains(self.resp,"Feriado")
        
    def test_template_feriado(self):
        self.assertTemplateUsed(self.resp,'feriados.html')

class FeriadoModelTest(TestCase):
    def setUp(self):
        self.feriado = "feriado"
        self.mes = 12
        self.dia = 25
        self.cadastro = FeriadoModel(
            nome = self.feriado,
            dia = self.dia,
            mes = self.mes
        )
        
        self.cadastro.save()

    def test_created(self):
        self.assertTrue(FeriadoModel.objects.exists())
        
        
    