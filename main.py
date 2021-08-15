from time import sleep
import os
from dotenv import load_dotenv
import pandas as pd
import asyncio
from playwright.async_api import async_playwright

# class Vivaldi:

#     def __init__(self) -> None:
#         self._open()
#         self.actions = ActionChains(self.driver)
    
#     def _open(self) -> None:
#         options = Options()
#         options.add_argument('start-maximized')
#         options.binary_location = r"C:\Users\pietr\AppData\Local\Vivaldi\Application\vivaldi.exe"
#         self.driver = webdriver.Chrome(executable_path=r'chromedriver.exe', options=options)

#     def site(self, url) -> None:
#         self.driver.get(url)

#     def download_in_gdrive(self, cl) -> None:
#         """ Recebe classe do elemento html """
#         search = self.driver.find_element_by_class_name(cl)

#         search.click()

#         sleep(10)
#         current_url = self.driver.current_url
#         self.driver.get(current_url)

#         sleep(3)
#         search = self.driver.find_element_by_class_name(cl)
#         search.click()

#         sleep(5)
#         search = self.driver.find_element_by_class_name('a-b-rb-c')
#         search.click()

#         sleep(5)
#         pygui.press('enter')
#         sleep(5)

    
#     def quit(self):
#         self.driver.quit()

class Automation:

    def __init__(self, email, password, destino, assunto, conteudo):
        asyncio.run(self.open(email, password, destino, assunto, conteudo))

    async def open(self, email, password, destino, assunto, conteudo):
        async with async_playwright() as p:
            browser = await p.firefox.launch(headless=False)
            page = await browser.new_page()
            await page.goto('https://protonmail.com')
            print(await page.title())

            # Fazer login
            await page.click('//*[@id="bs-example-navbar-collapse-1"]/ul/li[8]/a')
            await page.fill('//*[@id="username"]',email)
            await page.fill('//*[@id="password"]',password)
            await page.click('//html/body/div[1]/div[2]/div/div/main/div[2]/form/button')

            # Enviar email
            await page.click('//html/body/div[1]/div[2]/div[2]/div/div[1]/div[2]/button')
            await page.fill('//html/body/div[1]/div[3]/div/div/div/div/div/div[2]/div/div/div/div/div/input',destino)
            await page.fill('//html/body/div[1]/div[3]/div/div/div/div/div/div[3]/input', assunto)

            # Entrar no iframe
            iframe = await page.wait_for_selector(".squireIframe")
            iframe = await iframe.content_frame()
            
            # Colocar conteudo dentro do iframe
            await iframe.type('//html/body/div[1]', conteudo)

            # Clicar para enviar
            await page.click('//html/body/div[1]/div[3]/div/div/div/footer/button/span')

            sleep(2)

            await browser.close()

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

Automation(email, password, destino, assunto, conteudo)