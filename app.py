from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

#Configuracion de envio de correo
app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = 'bb46ce59e82fc3'
app.config['MAIL_PASSWORD'] = 'b5c16a7e4ca6cd'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

#Configuracion para recibir correos al gmail
"""
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587  # Puerto de Gmail para TLS
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'tu_correo@gmail.com'  # Tu dirección de correo de Gmail
app.config['MAIL_PASSWORD'] = 'tu_contraseña'  # Tu contraseña de Gmail
"""

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mail', methods=['GET', 'POST'])
def send_mail():

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        #Enviar datos a nuestro email   
        msg = Message('Nuevo mensaje de tu sitio web', sender=email, recipients=['alvaroconti05@gmail.com'])
        msg.body = f"Nombre: {name}\nCorreo electrónico: {email}\nMensaje: {message}"
        mail.send(msg)

        return render_template('send_mail.html')
    
    return redirect(url_for('index'))