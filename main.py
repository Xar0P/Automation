import os
from dotenv import load_dotenv
import asyncio
from lib.emails.protonmail import ProtonMail
from lib.download.downloadgdrive import DownloadGDrive
from lib.data.analysis import analysis
from lib.data.extract_file import extract_zip

def main():
    async def get_file():
        download = DownloadGDrive()
        await download.start('https://drive.google.com/drive/folders/14oLE59U1RqyRqlBbKpsyymW-mitvbtoh')
        await download.download()
        await download.exit()

    try:
        asyncio.run(get_file())
    except Exception:
        asyncio.run(get_file())
    except Exception as e:
        print(f'Erro: {e}')

    extract_zip()

    dados = analysis()

    load_dotenv()
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    destino = 'pietroricardocres@hotmail.com'
    assunto = 'Relatório de vendas de Ontem'
    conteudo = f"""
    Prezado, bom dia

    O faturamento de ontem foi de: R$ {dados.dados[0]}
    A quantidade de produtos foi de: {dados.dados[1]}

    Abs
    Garrafa"""

    async def send_mail():
        auto = ProtonMail()
        await auto.start()
        await auto.login(email, password)
        await auto.send_mail(destino, assunto, conteudo)
        await auto.exit()

    asyncio.run(send_mail())

if __name__ == "__main__":
    main()