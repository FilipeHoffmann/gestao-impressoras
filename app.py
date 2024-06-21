from flask import Flask, render_template, request
from controller.contratos import class_contratos

app = Flask(__name__)

#Index

@app.route('/',methods=['GET'])
def index():
    return render_template('/home/index.html')
    
#Contratos
    
@app.route('/contratos',methods=['GET'])
def contratos():
    if request.method == "GET":
        return class_contratos.class_contratos.contratos()
    
@app.route('/contratos/editar/<int:id_contrato>', methods=['GET', 'POST'])
def editar_contrato(id_contrato):
    if request.method == "POST":
        return class_contratos.class_contratos.editar_contrato(id_contrato)
    elif request.method =="GET":
        return class_contratos.class_contratos.obter_contrato(id_contrato)
    
@app.route('/contratos/excluir/<int:id_contrato>', methods=['GET'])
def excluir_contrato(id_contrato):
    return class_contratos.class_contratos.excluir_contrato(id_contrato)
        
@app.route('/contratos/criar', methods=['GET','POST'])
def criar_contrato():
    if request.method == "POST":
        return class_contratos.class_contratos.criar_contrato()
    elif request.method == "GET":
        return class_contratos.class_contratos.obter_formulario_contrato()
    
if __name__ == "__main__":
    app.run(debug=True)