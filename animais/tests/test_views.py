from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet
from animais.models import Animais


class IndexViewTestCase(TestCase):
    def setUp(self):

        self.factory = RequestFactory()
        self.animais = Animais.objects.create(
            nome_animal="Papagaio",
            predador = "Verde",
            venenoso="Doméstico",
            domestico = "não"
        )
    
    def test_index_view_retorna_caracteristicas_do_animal(self):
        response = self.client.get('/',{
            'caracteristicas':self.animais
        })

        caracteristica_animal_pesquisado  = response.context['caracteristicas']

        self.assertIs(type(response.context['caracteristicas']), QuerySet)

        self.assertEqual(caracteristica_animal_pesquisado[0].nome_animal, 'Papagaio')
        