import os
from dotenv import load_dotenv
from lib.emails.choose_email import choose_email
from lib.download.downloadgdrive import download as download_drive
from lib.data.analysis import analysis
from lib.data.extract_file import extract_zip

def main():
    
    download_drive('https://drive.google.com/drive/folders/14oLE59U1RqyRqlBbKpsyymW-mitvbtoh')

    extract_zip()

    dados = analysis()

    load_dotenv()
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    destiny = 'pietroricardocres@hotmail.com'
    subject = 'Relatório de vendas de Ontem'
    content = f"""
    Prezado, bom dia

    O faturamento de ontem foi de: R$ {dados.dados[0]}
    A quantidade de produtos foi de: {dados.dados[1]}

    Abs
    Garrafa"""

    choose_email(email,password,destiny,subject,content)
    

if __name__ == "__main__":
    main()