from flask import Flask, render_template, request
from model.contratos_model import contratos_model

app = Flask(__name__)

contratos_model_instance = contratos_model()

@app.route('/',methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('/home/index.html')
    
@app.route('/contratos',methods=['GET'])
def contratos():
    if request.method == 'GET':
        lista_contratos = contratos_model_instance.consultar_contratos("SELECT * FROM contracts ORDER BY contract_id DESC")
        return render_template('/contratos/contratos.html',
                            contratos = lista_contratos,
                            ids=lista_contratos)
        
@app.route('/contratos/editar/<int:id_contrato>', methods=['GET', 'POST'])
def editar_contrato(id_contrato):
    contrato = contratos_model_instance.consultar_contratos(f"SELECT * FROM contracts WHERE contract_id = {id_contrato}")
    
    if request.method == 'GET':
        return render_template('contratos/editar_contrato.html', contracts_id=id_contrato, contrato=contrato)
    
    if request.method == 'POST':
        descricao = request.form['descricao']
        data_inicio = request.form['data_inicio']
        data_fim = request.form['data_fim']
        contratada = request.form['contratada']
        custo_total = request.form['custo_total']

        update_query = f"""
            UPDATE contracts
            SET description = '{descricao}', start_date = '{data_inicio}', end_date = '{data_fim}', vendor = '{contratada}', total_cost = '{custo_total}'
            WHERE contract_id = '{id_contrato}'
        """
        contratos_model_instance.atualizar_contrato(update_query)
        mensagem = "Contrato editado!"
        return render_template('contratos/editar_contrato.html', mensagem = mensagem, contracts_id=id_contrato, contrato=contrato)
        
@app.route('/contratos/criar', methods=['GET','POST'])
def criar_contrato():
    if request.method == 'POST':
        descricao = request.form['descricao']
        data_inicio = request.form['data_inicio']
        data_fim = request.form['data_fim']
        contratada = request.form['contratada']
        custo_total = request.form['custo_total']
        contratos_model_instance.criar_contrato(f'INSERT INTO contracts(description,end_date,start_date,total_cost,vendor) VALUES ("{descricao}","{data_fim}","{data_inicio}","{custo_total}","{contratada}")')
        mensagem = "Contrato adicionado!"
        return render_template('/contratos/criar_contrato.html',
                               mensagem = mensagem)
    else:
        return render_template('/contratos/criar_contrato.html')   
            
if __name__ == "__main__":
    app.run(debug=True)