from flask import Flask, render_template, request, flash, redirect, url_for, send_file
from flask_mail import Mail, Message
from helpers import get_json, Contato
import datetime


app = Flask(__name__)
app.config.from_pyfile('config.py')
mail = Mail(app)


@app.route('/')
def index():
    birthday = datetime.date(1999, 1, 9)
    aniversario = birthday.strftime('%d/%m')
    idade = int(((datetime.date.today() - \
                      birthday).days) / 365)
    data = get_json('projects.json', app.config['PROJECTS_PATH'])['projects']
    return render_template('index.html',
                           aniversario=aniversario, 
                           idade=idade,
                           projects=data)
    

@app.route('/send', methods=['POST',])
def send():
    if request.method == 'POST':
        formContato = Contato(request.form['name'], 
                            request.form['email'], 
                            request.form['message'])
        
        msg = Message(
            subject = f'{formContato.nome} te enviou uma mensagem no portfólio',
            sender = app.config['MAIL_USERNAME'],
            recipients= ['lore.bezerra.r@gmail.com'],
            body = f'''
                
            {formContato.nome} com o e-mail {formContato.email} te enviou a seguinte mensagem:
            {formContato.mensagem}
            ''')
        
        mail.send(msg)
        flash('Mensagem enviada com sucesso!')
        return redirect(url_for('index'))
    
@app.route('/curriculum-vitae')
def get_cv():
    cv = app.config['CV_PATH'] + '/Lorena_CV_DataAnalyst.pdf'
    return send_file(cv)
         

if __name__ == '__main__':
    app.run(debug=True)

