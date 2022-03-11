from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
from config import email, senha, get_json, Contato
import datetime
import os

app = Flask(__name__)
app.secret_key = 'lorena'

app.config['FILE_PATH'] = os.path.dirname(os.path.realpath(__file__)) + '/static'
file_path = app.config['FILE_PATH']

mail_settings = {
    'MAIL_SERVER': 'smtp.gmail.com',
    'MAIL_PORT': 405,
    'MAIL_USE_TLS': False,
    'MAIL_USE_SSL': True,
    'MAIL_USERNAME':email,
    'MAIL_PASSWORD': senha
}

app.config.update(mail_settings)
mail = Mail(app)

@app.route('/')
def index():
    birthday = datetime.date(1999, 1, 9)
    aniversario = birthday.strftime('%d/%m')
    idade = int(((datetime.date.today() - \
                      birthday).days) / 365)
    data = get_json('project.json', file_path)['projects']
    return render_template('index.html',
                           aniversario=aniversario, 
                           idade=idade,
                           projects=data)
    

@app.route('/send', methods=['GET','POST'])
def send():
    if request.method == 'POST':
        formContato = Contato(
            request.form['name'],
            request.form['email'],
            request.form['message']
        )

        msg = Message(
            subject = f'{formContato.nome} te enviou uma mensagem no portfólio',
            sender = app.config.get("MAIL_USERNAME"),
            recipients= ['lore.bezerra.r@gmail.com'],
            body = f'''
            
            {formContato.nome} com o e-mail {formContato.email}, te enviou a seguinte mensagem:
            {formContato.mensagem}
            '''
        )
        mail.send(msg)
        flash('Mensagem enviada com sucesso!')
    return redirect('/')
         

if __name__ == '__main__':
    app.run(debug=True)

