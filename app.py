from flask import Flask, render_template
from controller.contratos import class_contratos
from controller.aditivos import class_aditivos

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template('/home/index.html')
    
#Contratos
    
@app.route('/contratos',methods=['GET','POST'])
def contratos():
    return class_contratos.class_contratos.contratos()
    
@app.route('/contratos/editar/<int:id_contrato>', methods=['GET', 'POST'])
def editar_contrato(id_contrato):
    return class_contratos.class_contratos.editar_contrato(id_contrato)
    
@app.route('/contratos/excluir/<int:id_contrato>', methods=['GET'])
def excluir_contrato(id_contrato):
    return class_contratos.class_contratos.excluir_contrato(id_contrato)
        
@app.route('/contratos/criar', methods=['GET','POST'])
def criar_contrato():
    return class_contratos.class_contratos.criar_contrato()
    
#Aditivos
    
@app.route('/contratos/aditivos',methods=['GET','POST'])
def aditivos():
    return class_aditivos.class_aditivos.aditivos()
        
@app.route('/contratos/aditivos/criar', methods=['GET','POST'])
def criar_aditivo():
    return class_aditivos.class_aditivos.criar_aditivo()
    
@app.route('/contratos/aditivos/editar/<int:id_aditivo>', methods=['GET', 'POST'])
def editar_aditivo(id_aditivo):
    return class_aditivos.class_aditivos.editar_aditivo(id_aditivo)
    
@app.route('/contratos/aditivos/excluir/<int:id_aditivo>', methods=['GET'])
def excluir_aditivo(id_aditivo):
    return class_aditivos.class_aditivos.excluir_contrato(id_aditivo)

if __name__ == "__main__":
    app.run(debug=True)