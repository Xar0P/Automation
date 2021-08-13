import pyautogui as pygui
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import os
from dotenv import load_dotenv
import pandas as pd


class Vivaldi:

    def __init__(self) -> None:
        self._open()
        self.actions = ActionChains(self.driver)
    
    def _open(self) -> None:
        options = Options()
        options.add_argument('start-maximized')
        options.binary_location = r"C:\Users\pietr\AppData\Local\Vivaldi\Application\vivaldi.exe"
        self.driver = webdriver.Chrome(executable_path=r'chromedriver.exe', options=options)

    def site(self, url) -> None:
        self.driver.get(url)

    def download_in_gdrive(self, cl) -> None:
        """ Recebe classe do elemento html """
        search = self.driver.find_element_by_class_name(cl)

        search.click()

        sleep(10)
        current_url = self.driver.current_url
        self.driver.get(current_url)

        sleep(3)
        search = self.driver.find_element_by_class_name(cl)
        search.click()

        sleep(5)
        search = self.driver.find_element_by_class_name('a-b-rb-c')
        search.click()

        sleep(5)
        pygui.press('enter')
        sleep(5)

    
    def quit(self):
        self.driver.quit()

class Firefox:
    def __init__(self) -> None:
        self._open()
        
    def _open(self) -> None:
        os.environ['MOZ_HEADLESS'] = '1' # Ficar invisivel a janela
        self.driver = webdriver.Firefox(executable_path=r'geckodriver.exe')
    

    def site(self, url) -> None:
        self.driver.get(url)

    def login(self, email, password):
        """ FAZENDO LOGIN """
        self.driver.find_element_by_xpath('//*[@id="bs-example-navbar-collapse-1"]/ul/li[8]/a').click()
        sleep(5)

        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys(email)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/main/div[2]/form/button').click()
        sleep(30)

    def send_email(self, destino, assunto, conteudo):
        """ ENVIANDO EMAIL """
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div[1]/div[2]/button').click()
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div/div/div[2]/div/div/div/div/div/input').send_keys(destino)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div/div/div[3]/input').send_keys(assunto)
        sleep(2)

        # MUDANDO PARA O IFRAME, PARA PEGAR O HTML DENTRO DELE
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div/section/div/div/div[1]/div/iframe'))
        self.driver.find_element_by_xpath('/html/body/div[1]').send_keys(conteudo)
        
        # RETORNANDO PARA O HTML PADRAO
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/footer/button/span').click()
        sleep(12)

    def quit(self):
        self.driver.quit()


# vivaldi = Vivaldi()
# vivaldi.site('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
# sleep(5)
# vivaldi.download_in_gdrive('bSmy5')
# vivaldi.quit()

# sleep(5)
# df = pd.read_excel(r'C:/Users/pietr/Downloads/Vendas - Dez.xlsx')

# faturamento = df['Valor Final'].sum()
# qtde_produtos = df['Quantidade'].sum()

load_dotenv()

email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')

destino = 'pietroricardocres@hotmail.com'
assunto = 'Relatório de vendas de Ontem'
conteudo = f"""
Prezado, bom dia

O faturamento de ontem foi de: R$
A quantidade de produtos foi de: 

Abs
Garrafa"""

firefox = Firefox()
firefox.site('https://protonmail.com')
firefox.login(email=email, password=password)
firefox.send_email(destino=destino, assunto=assunto, conteudo=conteudo)
firefox.quit()
