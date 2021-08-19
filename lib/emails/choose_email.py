import re
import asyncio
from .gmail import Gmail
from .protonmail import ProtonMail

def choose_email(email,password,destiny,subject,content):
    host_email = re.search('@[a-zA-Z]*',email)
    host_email = host_email.group()

    if host_email == '@gmail':
        gmail = Gmail()
        gmail.login(email,password)
        gmail.send_mail(destiny,subject,content)
    elif host_email == '@protonmail':
        async def send_mail():
            auto = ProtonMail()
            await auto.start()
            await auto.login(email, password)
            await auto.send_mail(destiny, subject, content)
            await auto.exit()

        asyncio.run(send_mail())