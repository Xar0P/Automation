from playwright.async_api import async_playwright
from time import sleep

class DownloadGDrive:
    async def start(self, url):
        """ Iniciar o firefox """

        self.playwright = await async_playwright().start()
        # headless=False para ficar visivel
        self.browser = await self.playwright.firefox.launch()
        self.page = await self.browser.new_page(accept_downloads=True)
        await self.page.goto(url)
        print(await self.page.title())

    async def download(self, xpath: str = '#content'):
        """ Baixar arquivo """

        await self.page.dblclick(xpath)
        sleep(3)

        async def download():
            print('Baixando')
            async with self.page.expect_download() as download_info:
                await self.page.click('//html/body/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]')
                download = await download_info.value
                await download.save_as(download.suggested_filename)

        await download()

        print('Finalizado!')

    async def exit(self):
        await self.browser.close()
        await self.playwright.stop()