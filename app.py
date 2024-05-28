from flask import Flask, render_template, request
from controller.contratos import class_contratos
from controller.aditivos import class_aditivos
from controller.produtos import class_produtos
from controller.impressoras import class_impressoras

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
    
#Aditivos
    
@app.route('/contratos/aditivos',methods=['GET'])
def aditivos():
    if request.method == "GET":
        return class_aditivos.class_aditivos.aditivos()
        
@app.route('/contratos/aditivos/criar', methods=['GET','POST'])
def criar_aditivo():
    if request.method == "POST":  
        return class_aditivos.class_aditivos.criar_aditivo()
    elif request.method == "GET":
        return class_aditivos.class_aditivos.obter_formulario_aditivo()

    
@app.route('/contratos/aditivos/editar/<int:id_aditivo>', methods=['GET', 'POST'])
def editar_aditivo(id_aditivo):
    if request.method == "POST":
        return class_aditivos.class_aditivos.editar_aditivo(id_aditivo)
    elif request.method == "GET":
        return class_aditivos.class_aditivos.obter_aditivo(id_aditivo)

@app.route('/contratos/aditivos/excluir/<int:id_aditivo>', methods=['GET'])
def excluir_aditivo(id_aditivo):
    if request.method == "GET":
        return class_aditivos.class_aditivos.excluir_contrato(id_aditivo)
    
#Produtos

@app.route('/produtos',methods=['GET'])
def produtos():
    if request.method == "GET":
        return class_produtos.class_produtos.produtos()
    
@app.route("/produtos/criar", methods=['GET','POST'])
def criar_produto():
    if request.method == "GET":
        return class_produtos.class_produtos.obter_formulario_produto()
    elif request.method == "POST":
        return class_produtos.class_produtos.criar_produto()
    
#Impressoras
@app.route('/impressoras', methods=['GET'])
def impressoras():
    if request.method == "GET":
        return class_impressoras.class_impressoras.impressoras()
    elif request.method == "POST":
        return class_impressoras.class_impressoras.criar_impressora()
    
if __name__ == "__main__":
    app.run(debug=True)