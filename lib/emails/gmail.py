import smtplib
from email.message import EmailMessage

class Gmail:
    
    def __init__(self) -> None:
        """ IMPORTANT - Para enviar email pelo gmail, permitir dispositivos menos seguros! """

        self.message = EmailMessage()

    def login(self, email: str = 'example@example.com', password: str = '12345') -> None:
        """ Stores login data """

        self.email = email
        self.password = password
        print('Login feito!')

    def send_mail(self, destiny: str = 'destiny@example.com', subject: str = 'Automatic email', content: str = 'Content'):
        """ Send the email """

        self.message['From'] = self.email
        self.message['To'] = destiny
        self.message['Subject'] = subject

        self.message.add_header('Content-Type', 'text/html')
        self.message.set_payload(content)

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()

        s.login(self.email, self.password)
        s.sendmail(self.email,destiny,self.message.as_string().encode('utf-8'))
        s.quit()
        print('E-mail enviado!')