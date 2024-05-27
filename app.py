from flask import Flask, render_template, request, url_for, redirect
from model.contratos_model import contratos_model

app = Flask(__name__)

contratos_model_instance = contratos_model()

@app.route('/',methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('/home/index.html')
    
#Contratos
    
@app.route('/contratos',methods=['GET','POST'])
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
        return redirect(url_for('contratos'))
    
@app.route('/contratos/excluir/<int:id_contrato>', methods=['GET'])
def excluir_contrato(id_contrato):
    delete_query = f"DELETE FROM contracts WHERE contract_id = {id_contrato}"
    contratos_model_instance.excluir_contrato(delete_query)
    return redirect(url_for('contratos'))
        
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
    
#Aditivos
    
@app.route('/contratos/aditivos',methods=['GET','POST'])
def aditivos():
    if request.method == 'GET':
        lista_aditivos = contratos_model_instance.consultar_contratos("SELECT * FROM contractamendments ORDER BY amendment_id DESC")
        return render_template('/contratos/aditivos/aditivos.html',
                            aditivos = lista_aditivos,
                            ids=lista_aditivos)
        
@app.route('/contratos/aditivos/criar', methods=['GET','POST'])
def criar_aditivo():
    if request.method == 'POST':
        id_contrato = request.form['id_contrato']
        data_prorrogada = request.form['data_prorrogada']
        detalhes = request.form['detalhes']
        custo_adicional = request.form['custo_adicional']
        contratos_model_instance.criar_contrato(f'INSERT INTO contractamendments(contract_id,amendment_date,details,additional_cost) VALUES ("{id_contrato}","{data_prorrogada}","{detalhes}","{custo_adicional}")')
        mensagem = "Contrato adicionado!"
        return render_template('/contratos/aditivos/criar_aditivo.html',
                               mensagem = mensagem)
    else:
        return render_template('/contratos/aditivos/criar_aditivo.html')
    
@app.route('/contratos/aditivos/editar/<int:id_aditivo>', methods=['GET', 'POST'])
def editar_aditivo(id_aditivo):
    aditivos = contratos_model_instance.consultar_contratos(f"SELECT * FROM contractamendments WHERE amendment_id = {id_aditivo}")
    
    if request.method == 'GET':
        return render_template('/contratos/aditivos/editar_aditivo.html',  aditivo=aditivos)
    
    if request.method == 'POST':
        id_contrato = request.form['id_contrato']
        data_prorrogada = request.form['data_prorrogada']
        detalhes = request.form['detalhes']
        custo_adicional = request.form['custo_adicional']

        update_query = f"""
            UPDATE contractamendments
            SET contract_id = '{id_contrato}', amendment_date = '{data_prorrogada}', details = '{detalhes}', additional_cost = '{custo_adicional}'
            WHERE amendment_id = '{id_aditivo}'
        """
        contratos_model_instance.atualizar_contrato(update_query)
        return redirect(url_for('aditivos'))
    
@app.route('/contratos/aditivos/excluir/<int:id_aditivo>', methods=['GET'])
def excluir_aditivo(id_aditivo):
    delete_query = f"DELETE FROM contractamendments WHERE amendment_id = {id_aditivo}"
    contratos_model_instance.excluir_contrato(delete_query)
    return redirect(url_for('aditivos'))
            
if __name__ == "__main__":
    app.run(debug=True)