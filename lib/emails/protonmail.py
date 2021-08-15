from playwright.async_api import async_playwright
from time import sleep

class ProtonMail:

    async def start(self):
        """ Iniciar o firefox """

        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.firefox.launch()
        self.page = await self.browser.new_page()
        await self.page.goto('https://protonmail.com')
        print(await self.page.title())

    async def login(self, email, password):
        """ Fazer login """

        await self.page.click('//*[@id="bs-example-navbar-collapse-1"]/ul/li[8]/a')
        await self.page.fill('//*[@id="username"]',email)
        print('Inserindo E-Mail')
        await self.page.fill('//*[@id="password"]',password)
        print('Inserindo Senha')
        await self.page.click('//html/body/div[1]/div[2]/div/div/main/div[2]/form/button')
        print('Logado!')

    async def send_mail(self, destino, assunto, conteudo):
        """ Enviar email """

        await self.page.click('//html/body/div[1]/div[2]/div[2]/div/div[1]/div[2]/button')
        print('Inserindo Destino')
        await self.page.fill('//html/body/div[1]/div[3]/div/div/div/div/div/div[2]/div/div/div/div/div/input',destino)
        print('Inserindo Assunto')
        await self.page.fill('//html/body/div[1]/div[3]/div/div/div/div/div/div[3]/input', assunto)

        # Entrar no iframe
        iframe = await self.page.wait_for_selector(".squireIframe")
        iframe = await iframe.content_frame()
        
        # Colocar conteudo dentro do iframe
        print('Inserindo Conteúdo')
        await iframe.type('//html/body/div[1]', conteudo)

        # Clicar para enviar
        await self.page.click('//html/body/div[1]/div[3]/div/div/div/footer/button/span')
        sleep(4)
        print('Enviado!')

    async def exit(self):
        await self.browser.close()
        await self.playwright.stop()