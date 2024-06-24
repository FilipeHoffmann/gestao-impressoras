from flask import Flask, render_template, request
from controller.contratos import class_contratos
from controller.secretarias import class_secretarias
from controller.produtos import class_produtos
from controller.itens import class_itens

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
    
#secretarias
    
@app.route('/secretarias',methods=['GET'])
def secretarias():
    if request.method == "GET":
        return class_secretarias.class_secretarias.secretarias()
    
@app.route('/secretarias/editar/<int:id_secretaria>', methods=['GET', 'POST'])
def editar_secretaria(id_secretaria):
    if request.method == "POST":
        return class_secretarias.class_secretarias.editar_secretaria(id_secretaria)
    elif request.method =="GET":
        return class_secretarias.class_secretarias.obter_secretaria(id_secretaria)
    
@app.route('/secretarias/excluir/<int:id_secretaria>', methods=['GET'])
def excluir_secretaria(id_secretaria):
    return class_secretarias.class_secretarias.excluir_secretaria(id_secretaria)
        
@app.route('/secretarias/criar', methods=['GET','POST'])
def criar_secretaria():
    if request.method == "POST":
        return class_secretarias.class_secretarias.criar_secretaria()
    elif request.method == "GET":
        return class_secretarias.class_secretarias.obter_formulario_secretaria()
    
#produtos
    
@app.route('/produtos',methods=['GET'])
def produtos():
    if request.method == "GET":
        return class_produtos.class_produtos.produtos()
    
@app.route('/produtos/editar/<int:id_produto>', methods=['GET', 'POST'])
def editar_produto(id_produto):
    if request.method == "POST":
        return class_produtos.class_produtos.editar_produto(id_produto)
    elif request.method =="GET":
        return class_produtos.class_produtos.obter_produto(id_produto)
    
@app.route('/produtos/excluir/<int:id_produto>', methods=['GET'])
def excluir_produto(id_produto):
    return class_produtos.class_produtos.excluir_produto(id_produto)
        
@app.route('/produtos/criar', methods=['GET','POST'])
def criar_produto():
    if request.method == "POST":
        return class_produtos.class_produtos.criar_produto()
    elif request.method == "GET":
        return class_produtos.class_produtos.obter_formulario_produto()
    
@app.route('/itens', methods=['GET','POST'])
def itens():
    if request.method == "GET":
        return class_itens.class_itens.itens()
    
if __name__ == "__main__":
    app.run(debug=True, host="192.168.0.159")