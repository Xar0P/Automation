import pyautogui as pygui
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
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

    def get_element_class(self, cl) -> None:
        search = self.driver.find_element_by_class_name(cl)

        search.click()

        time.sleep(10)
        current_url = self.driver.current_url
        self.driver.get(current_url)

        search = self.driver.find_element_by_class_name(cl)
        search.click()

        time.sleep(10)
        search = self.driver.find_element_by_class_name('a-b-rb-c')
        search.click()

        time.sleep(5)
        pygui.press('enter')
        time.sleep(5)

    def quit(self):
        self.driver.quit()


vivaldi = Vivaldi()
vivaldi.site('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
time.sleep(5)
vivaldi.get_element_class('bSmy5')
vivaldi.quit()

time.sleep(10)
df = pd.read_excel(r'C:/Users/pietr/Downloads/Vendas - Dez.xlsx')

faturamento = df['Valor Final'].sum()
qtde_produtos = df['Quantidade'].sum()
print(df)
print(faturamento)
print(qtde_produtos)
