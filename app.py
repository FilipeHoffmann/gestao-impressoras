from flask import Flask, render_template, request
from scripts import banco_de_dados

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('/home/index.html')
    
@app.route('/contratos',methods=['GET'])
def contratos():
    lista = [['teste']]
    return render_template('/contratos/contratos.html',
                           contratos=lista)

if __name__ == "__main__":
    app.run(host="192.168.0.159",port=3000,debug=True)