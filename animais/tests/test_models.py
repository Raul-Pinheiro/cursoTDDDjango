from django.test import TestCase, RequestFactory
from animais.models import Animais



class AnimaisModelTestCase(TestCase):

    def setUp(self):
        self.animais = Animais.objects.create(
            nome_animal="Papagaio",
            predador = "Verde",
            venenoso="Doméstico",
            domestico = "não"
        )

    def test_anmimal_cadastrado_com_caracteristicas(self):
        self.assertEqual(self.animais.nome_animal, 'Papagaio')