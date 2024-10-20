import smtplib
from email.mime.text import MIMEText

correo_origen = 'correo1@gmail.com'
contraseña = '*'
correo_destino = 'correo2@gmail.com'

msg = MIMEText("texto del correo")
msg['Subject'] = 'Envio de correo electronico desde Raspberry PI'
msg['From'] = correo_origen
msg['To'] = correo_destino

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(correo_origen,contraseña)
server.sendmail(correo_origen,correo_destino,msg.as_string())

print("El correo se ha  enviado.")

server.quit()