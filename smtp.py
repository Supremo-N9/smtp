import smtplib
import os.path
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE
from email import encoders

# Configuración del servidor SMTP de Gmail
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'email'
smtp_password = 'password'

# Configuración del correo electrónico
sender = 'emailxd'
receiver = ['DESTINATARIO_1@gmail.com', 'DESTINATARIO_2@hotmail.com']
subject = 'Correo con archivo adjunto'
body = 'Hola,\n\nAdjunto te envío un archivo PDF.\n\nSaludos.'

# Configuración del archivo adjunto
filename = 'documento.pdf'
attachment = open(filename, 'rb')

# Creación del mensaje
msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = COMMASPACE.join(receiver)
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

part = MIMEBase('application', "octet-stream")
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment', filename=filename)
msg.attach(part)

# Envío del mensaje
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(sender, receiver, msg.as_string())
    server.close()
    print('Correo enviado correctamente')
except Exception as e:
    print('Error al enviar el correo: ', str(e))
