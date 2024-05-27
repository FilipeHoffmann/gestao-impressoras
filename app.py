from flask import Flask, render_template, request, url_for, redirect
from static.scripts import conector_banco_de_dados

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('/home/index.html')
    
#Contratos
    
@app.route('/contratos',methods=['GET','POST'])
def contratos():
    if request.method == 'GET':
        query = conector_banco_de_dados.conector_banco_de_dados("SELECT * FROM contratos ORDER BY id_contratos DESC")
        lista_contratos = query.consultar()
        return render_template('/contratos/contratos.html',
                            contratos = lista_contratos,
                            ids=lista_contratos)
    
@app.route('/contratos/editar/<int:id_contrato>', methods=['GET', 'POST'])
def editar_contrato(id_contrato):
    query = conector_banco_de_dados.conector_banco_de_dados(f"SELECT * FROM contratos WHERE id_contratos = {id_contrato}")
    contrato = query.consultar()
    if request.method == 'GET':
        return render_template('contratos/editar_contrato.html', contracts_id=id_contrato, contrato=contrato)
    
    if request.method == 'POST':
        descricao = request.form['descricao']
        data_inicio = request.form['data_inicio']
        data_fim = request.form['data_fim']
        contratada = request.form['contratada']
        custo_total = request.form['custo_total']

        update_query = f"""
            UPDATE contratos
            SET descricao = '{descricao}', data_inicial = '{data_inicio}', data_final = '{data_fim}', contratada = '{contratada}', custo_total = '{custo_total}'
            WHERE id_contratos = '{id_contrato}'
        """
        conector_banco_de_dados.conector_banco_de_dados(update_query).alterar_incluir_excluir()
        return redirect(url_for('contratos'))
    
@app.route('/contratos/excluir/<int:id_contrato>', methods=['GET'])
def excluir_contrato(id_contrato):
    delete_query = f"DELETE FROM contratos WHERE id_contratos = {id_contrato}"
    conector_banco_de_dados.conector_banco_de_dados(delete_query).alterar_incluir_excluir()
    return redirect(url_for('contratos'))
        
@app.route('/contratos/criar', methods=['GET','POST'])
def criar_contrato():
    if request.method == 'POST':
        descricao = request.form['descricao']
        data_inicio = request.form['data_inicio']
        data_fim = request.form['data_fim']
        contratada = request.form['contratada']
        custo_total = request.form['custo_total']
        conector_banco_de_dados.conector_banco_de_dados(f'INSERT INTO contratos(descricao,data_final,data_inicial,custo_total,contratada) VALUES ("{descricao}","{data_fim}","{data_inicio}","{custo_total}","{contratada}")').alterar_incluir_excluir()
        mensagem = "Contrato adicionado!"
        return render_template('/contratos/criar_contrato.html',
                               mensagem = mensagem)
    else:
        return render_template('/contratos/criar_contrato.html')
    
#Aditivos
    
@app.route('/contratos/aditivos',methods=['GET','POST'])
def aditivos():
    if request.method == 'GET':
        lista_aditivos = conector_banco_de_dados.conector_banco_de_dados("SELECT * FROM aditivos ORDER BY id_aditivos DESC").consultar()
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
        conector_banco_de_dados.conector_banco_de_dados(f'INSERT INTO aditivos(id_contratos,data_aditivo,detalhes,custo_adicional) VALUES ("{id_contrato}","{data_prorrogada}","{detalhes}","{custo_adicional}")').alterar_incluir_excluir()
        mensagem = "Contrato adicionado!"
        return render_template('/contratos/aditivos/criar_aditivo.html',
                               mensagem = mensagem)
    else:
        return render_template('/contratos/aditivos/criar_aditivo.html')
    
@app.route('/contratos/aditivos/editar/<int:id_aditivo>', methods=['GET', 'POST'])
def editar_aditivo(id_aditivo):
    aditivos = conector_banco_de_dados.conector_banco_de_dados(f"SELECT * FROM aditivos WHERE id_aditivos = {id_aditivo}").consultar()
    
    if request.method == 'GET':
        return render_template('/contratos/aditivos/editar_aditivo.html',  aditivo=aditivos)
    
    if request.method == 'POST':
        id_contrato = request.form['id_contrato']
        data_prorrogada = request.form['data_prorrogada']
        detalhes = request.form['detalhes']
        custo_adicional = request.form['custo_adicional']

        update_query = f"""
            UPDATE aditivos
            SET id_contratos = '{id_contrato}', data_aditivo = '{data_prorrogada}', detalhes = '{detalhes}', custo_adicional = '{custo_adicional}'
            WHERE id_aditivos = '{id_aditivo}'
        """
        conector_banco_de_dados.conector_banco_de_dados(update_query).alterar_incluir_excluir()
        return redirect(url_for('aditivos'))
    
@app.route('/contratos/aditivos/excluir/<int:id_aditivo>', methods=['GET'])
def excluir_aditivo(id_aditivo):
    delete_query = f"DELETE FROM aditivos WHERE id_aditivos = {id_aditivo}"
    conector_banco_de_dados.conector_banco_de_dados(delete_query).alterar_incluir_excluir()
    return redirect(url_for('aditivos'))

if __name__ == "__main__":
    app.run(debug=True)