from flask import render_template, request, url_for, redirect
from static.scripts import conector_banco_de_dados

class class_impressoras:
    @staticmethod
    def impressoras():
        query = conector_banco_de_dados.conector_banco_de_dados('''SELECT `impressoras`.`id_impressoras`,
        `impressoras`.`modelo`,
        `impressoras`.`marca`,
        `impressoras`.`ip`,
        `impressoras`.`localizacao`,
        `impressoras`.`status`,
        `impressoras`.`tipo_impressora`,
        `impressoras`.`cotas`,
        `impressoras`.`contador_inicial`,
        `impressoras`.`data_instalacao`,
        `setores`.`nome_setor`,
        `produtos`.`descricao`
        FROM `controleimpressora`.`impressoras`
        INNER JOIN setores ON setores.id_setores = impressoras.id_setores
        INNER JOIN produtos ON produtos.id_produtos = impressoras.id_produtos;
        ''')
        lista_impressoras = query.consultar()
        return render_template('/impressoras/impressoras.html',
                            impressoras = lista_impressoras,
                            ids=lista_impressoras)

    def obter_impressora(id_impressora):
        query = conector_banco_de_dados.conector_banco_de_dados(f'''SELECT `impressoras`.`id_impressoras`,
        `impressoras`.`modelo`,
        `impressoras`.`marca`,
        `impressoras`.`ip`,
        `impressoras`.`localizacao`,
        `impressoras`.`status`,
        `impressoras`.`tipo_impressora`,
        `impressoras`.`cotas`,
        `impressoras`.`contador_inicial`,
        `impressoras`.`data_instalacao`,
        `setores`.`nome_setor`,
        `produtos`.`descricao`
        FROM `controleimpressora`.`impressoras`
        INNER JOIN setores ON setores.id_setores = impressoras.id_setores
        INNER JOIN produtos ON produtos.id_produtos = impressoras.id_produtos
        WHERE id_impressoras = {id_impressora}''')
        impressoras = query.consultar()
        impressoras = impressoras[0]
        produtos_query = "SELECT id_produtos, descricao FROM produtos"
        produtos = conector_banco_de_dados.conector_banco_de_dados(produtos_query).consultar()
        setores_query = "SELECT id_setores, nome_setor FROM setores"
        setores = conector_banco_de_dados.conector_banco_de_dados(setores_query).consultar()
        impressoras_dict = {
            'modelo': impressoras[1],
            'marca': impressoras[2],
            'ip': impressoras[3],
            'localizacao': impressoras[4],
            'status': impressoras[5],
            'tipo_impressora': impressoras[6],
            'cotas': impressoras[7],
            'contador_inicial': impressoras[8],
            'data_instalacao': impressoras[9],
            'id_setores': impressoras[10],
            'id_produtos': impressoras[11]
        }
        return render_template('impressoras/editar_impressora.html', id_impressora=id_impressora, impressora=impressoras_dict, produtos=produtos, setores=setores)
    
    def editar_impressora(id_impressora):
        modelo = request.form['modelo']
        marca = request.form['marca']
        ip = request.form['ip']
        localizacao = request.form['localizacao']
        status = request.form['status']
        tipo_impressora = request.form['tipo_impressora']
        id_setores = request.form['id_setores']
        cotas = request.form['cotas']
        contador_inicial = request.form['contador_inicial']
        data_instalacao = request.form['data_instalacao']
        id_produtos = request.form['id_produtos']
        update_query = f"""
        UPDATE impressoras
        SET modelo = '{modelo}', marca = '{marca}', ip = '{ip}', localizacao = '{localizacao}', status = '{status}', tipo_impressora = '{tipo_impressora}', id_setores = '{id_setores}', cotas = '{cotas}', contador_inicial = '{contador_inicial}', data_instalacao = '{data_instalacao}', id_produtos = '{id_produtos}'
        WHERE id_impressoras = '{id_impressora}'
        """
        conector_banco_de_dados.conector_banco_de_dados(update_query).alterar_incluir_excluir()
        return redirect(url_for('impressoras'))
            
    def excluir_impressora(id_impressora):
        delete_query = f"DELETE FROM impressoras WHERE id_impressoras = {id_impressora}"
        conector_banco_de_dados.conector_banco_de_dados(delete_query).alterar_incluir_excluir()
        return redirect(url_for('impressoras'))
    
    def criar_impressora():
        id_impressora = request.form['id_impressora']
        modelo = request.form['modelo']
        marca = request.form['marca']
        ip = request.form['ip']
        localizacao = request.form['localizacao']
        status = request.form['status']
        tipo_impressora = request.form['tipo_impressora']
        id_setores = request.form['id_setores']
        cotas = request.form['cotas']
        contador_inicial = request.form['contador_inicial']
        data_instalacao = request.form['data_instalacao']
        id_produtos = request.form['id_produtos']
        
        conector_banco_de_dados.conector_banco_de_dados(f'INSERT INTO impressoras(id_impressoras, modelo, marca, ip, localizacao, status, tipo_impressora, id_setores, cotas, contador_inicial, data_instalacao, id_produtos) VALUES ("{id_impressora}","{modelo}","{marca}","{ip}","{localizacao}","{status}", "{tipo_impressora}","{id_setores}", "{cotas}", "{contador_inicial}","{data_instalacao}","{id_produtos}")').alterar_incluir_excluir()
        #Criar o contador vazio
        meses = ["JANEIRO","FEVEREIRO","MARÇO","ABRIL","MAIO","JUNHO","JULHO","AGOSTO","SETEMBRO","OUTUBRO","NOVEMBRO","DEZEMBRO"]
        for i in range(len(meses)):
            conector_banco_de_dados.conector_banco_de_dados(f'INSERT INTO contadores(id_impressoras, mes_referente) VALUES ("{id_impressora}", "{meses[i]}")').alterar_incluir_excluir()
        mensagem = "Impressora adicionada!"
        return render_template('/impressoras/criar_impressora.html',
                            mensagem = mensagem)
    
    def obter_formulario_impressora():
        setores_query = "SELECT id_setores, nome_setor FROM setores"
        setores = conector_banco_de_dados.conector_banco_de_dados(setores_query).consultar()
        produtos_query = "SELECT id_produtos, descricao FROM produtos"
        produtos = conector_banco_de_dados.conector_banco_de_dados(produtos_query).consultar()
        return render_template('/impressoras/criar_impressora.html',
                               setores=setores,
                               produtos = produtos)