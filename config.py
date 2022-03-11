import json

email = 'jzdhisjd@gmail.com'
senha = 'email110419'

def get_json(file, path):
    with open(f'{path}/{file}', 'r') as f:
        data = json.load(f)
    return data


class Contato:
    def __init__(self, nome, email, mensagem):
        self.__nome = nome
        self.__email = email
        self.__mensagem = mensagem
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def email(self):
        return self.__email
    
    @property
    def mensagem(self):
        return self.__mensagem

