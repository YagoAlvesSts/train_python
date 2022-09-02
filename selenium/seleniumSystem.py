from selenium import webdriver
from time import sleep
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import chromedriver_autoinstaller


class ChromeAuto():
    def __init__(self):
        # Caminho para a raiz do projeto
        self.__ROOT_FOLDER = Path(__file__).parent.parent.parent
        
        # Caminho para a pasta onde o chromedriver está
        self.__CHROME_DRIVER_PATH = self.__ROOT_FOLDER / 'selenium' / 'bin' / 'chromedriver'
        print(self.__CHROME_DRIVER_PATH)
        self.browser = None
        
    
    def make_chrome_browser(self, *options: str) -> webdriver.Chrome:
        chrome_options = webdriver.ChromeOptions()
        chromedriver_autoinstaller.install()

        # chrome_options.add_argument('--headless')
        if options is not None:
            for option in options:
                chrome_options.add_argument(option)

        # chrome_service = Service(
        #     executable_path= self.__CHROME_DRIVER_PATH,
        # )

        self.browser = webdriver.Chrome(
            options=chrome_options
        )

        return self.browser
    
    def acessa(self, site):
        self.browser.get(site)
        
    def sair(self):
        self.browser.quit()
    
    # TODO: Refactor this functions
    # def clica_sign_in(self):
    #     try:
    #         btn_sign_in = self.chrome.find_element_by_link_text('Sign in')
    #         btn_sign_in.click()
    #     except Exception as e:
    #         print('Erro ao clicar em Sign in:', e)


    

    # def clica_perfil(self):
    #     try:
    #         perfil = self.chrome.find_element_by_css_selector(
    #             'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-lg-flex > details')
    #         perfil.click()
    #     except Exception as e:
    #         print('Erro ao clicar no perfil:', e)

    # def faz_logout(self):
    #     try:
    #         perfil = self.chrome.find_element_by_css_selector(
    #             'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-lg-flex > details > details-menu > form > button')
    #         perfil.click()
    #     except Exception as e:
    #         print('Erro fazer logout:', e)

    # def verifica_usuario(self, usuario):
    #     profile_link = self.chrome.find_element_by_class_name(
    #         'user-profile-link')
    #     profile_link_html = profile_link.get_attribute('innerHTML')
    #     assert usuario in profile_link_html

    # def faz_login(self):
    #     try:
    #         input_login = self.chrome.find_element_by_id('login_field')
    #         input_password = self.chrome.find_element_by_id('password')
    #         btn_login = self.chrome.find_element_by_name('commit')

    #         input_login.send_keys('')
    #         input_password.send_keys('')
    #         sleep(3)
    #         btn_login.click()

    #     except Exception as e:
    #         print('Erro ao fazer login:', e)