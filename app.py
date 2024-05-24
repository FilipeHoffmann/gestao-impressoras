from flask import Flask, render_template, request
from model.contratos_model import contratos_model

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('/home/index.html')
    
@app.route('/contratos',methods=['GET'])
def contratos():
    lista_contratos = contratos_model().consultar_contratos()
    return render_template('/contratos/contratos.html',
                           contratos = lista_contratos,
                           ids=lista_contratos)

if __name__ == "__main__":
    app.run(host="192.168.0.159",port=3000,debug=True)