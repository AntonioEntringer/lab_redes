from flask import Flask, request
import os

app = Flask(__name__)

def salvar_arquivo(nome_arquivo, dados):
    with open(nome_arquivo, 'wb') as arquivo:
        arquivo.write(dados)

@app.route('/upload', methods=['POST'])
def receber_arquivo():
    arquivo = request.files['arquivo']
    nome_arquivo = arquivo.filename

    dados = arquivo.read()
    
    # Criar o diretório /root/receber se ele não existir
    diretorio_salvar = '/root/receber'
    if not os.path.exists(diretorio_salvar):
        os.makedirs(diretorio_salvar)

    salvar_arquivo('/root/receber/' + nome_arquivo, dados)
    return "Arquivo {} recebido e salvo com sucesso.".format(nome_arquivo)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
