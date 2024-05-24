from flask import Flask, render_template, request
from model.contratos_model import contratos_model

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('/home/index.html')
    
@app.route('/contratos',methods=['GET'])
def contratos():
    if request.method == 'GET':
        lista_contratos = contratos_model().consultar_contratos("SELECT * FROM contracts")
        return render_template('/contratos/contratos.html',
                            contratos = lista_contratos,
                            ids=lista_contratos)
        
@app.route('/contratos/criar', methods=['GET','POST'])
def criar_contrato():
    if request.method == 'POST':
        descricao = request.form['descricao']
        data_inicio = request.form['data_inicio']
        data_fim = request.form['data_fim']
        contratada = request.form['contratada']
        custo_total = request.form['custo_total']
        contratos_model().criar_contrato(f'INSERT INTO contracts(description,end_date,start_date,total_cost,vendor) VALUES ("{descricao}","{data_fim}","{data_inicio}","{custo_total}","{contratada}")')
        mensagem = "Contrato Adicionado"
        return render_template('/contratos/criar_contrato.html',
                               mensagem = mensagem)
    else:
        return render_template('/contratos/criar_contrato.html')
        
        
            
if __name__ == "__main__":
    app.run(debug=True)