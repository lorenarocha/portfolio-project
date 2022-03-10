from flask import Flask, render_template
import datetime
import os
import json

app = Flask(__name__)

app.config['FILE_PATH'] = os.path.dirname(os.path.realpath(__file__)) + '/static'
file_path = app.config['FILE_PATH']

@app.route('/')
def index():
    birthday = datetime.date(1999, 1, 9)
    aniversario = birthday.strftime('%d/%m')
    idade = str(int(((datetime.date.today() - \
                      birthday).days) / 365))
    data = get_json('project.json', file_path)['projects']
    return render_template('index.html',
                           aniversario=aniversario, 
                           idade=idade,
                           projects=data)
    
    
def get_json(file, path):
    with open(f'{path}/{file}', 'r') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    app.run(debug=True)

