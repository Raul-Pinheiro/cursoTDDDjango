from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from animais.models import Animais

class AnimaisTestCase(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('C:/Users/raulm/Desktop/django_tdd-aula_1/chromedriver.exe')
  
        self.animais = Animais.objects.create(
            nome_animal="Papagaio",
            predador = "Verde",
            venenoso="Doméstico",
            domestico = "não"
        )
        
 
 


    def tearDown(self):
        self.browser.quit()


    def test_buscando_um_novo_animal(self):
        """
            Tëste se um usuário encontra um animal na pesquisa
        """
   

        home_page = self.browser.get(self.live_server_url+'/')
        brand_element = self.browser.find_element(By.CSS_SELECTOR,'.navbar')

        self.assertEqual('Busca Animal', brand_element.text)

        
        buscar_animal_input = self.browser.find_element(By.CSS_SELECTOR,'input')
        
        self.assertEqual(buscar_animal_input.get_attribute('placeholder'), 'Exemplo: leão')
        
        #Busca

        buscar_animal_input.send_keys('leão')

        self.browser.find_element(By.CSS_SELECTOR,'form button').click()

        # Resultados

        resultados = self.browser.find_elements(By.CLASS_NAME, 'results')

        #self.assertGreater(len(resultados),0)
        