from flask import render_template, request, url_for, redirect
from static.scripts import conector_banco_de_dados

class class_contadores:
    @staticmethod
    def contadores():
        if request.method == "GET":
            query = conector_banco_de_dados.conector_banco_de_dados('''
            SELECT c.id_contadores, i.modelo, s.nome_setor, p.codigo,c.data_coleta,c.paginas_impressas,c.mes_referente
            FROM contadores as c
            inner join impressoras as i on c.id_impressoras = i.id_impressoras
            inner join setores as s on c.id_setores = s.id_setores
            inner join produtos as p on c.id_produtos = p.id_produtos 
            ORDER BY c.id_contadores DESC''')
            contadores = query.consultar()
            return render_template("/contadores/contadores.html",
                                ids = contadores,
                                contadores=contadores)
            
    def criar_contador():
        if request.method == "POST":
            id_impressoras = request.form["id_impressoras"]
            id_setores = request.form["id_setores"]
            id_produtos = request.form["id_produtos"]
            data_coleta = request.form["data_coleta"]
            paginas_impressas = request.form["paginas_impressas"]
            mes_referente = request.form["mes_referente"]
            query = f'''INSERT INTO contadores(id_impressoras,id_setores,id_produtos,data_coleta,paginas_impressas,mes_referente)
                    VALUES ('{id_impressoras}','{id_setores}','{id_produtos}','{data_coleta}','{paginas_impressas}','{mes_referente}')'''
            conector_banco_de_dados.conector_banco_de_dados(query).alterar_incluir_excluir()
            mensagem = "Contador adicionado!"
            return render_template("/contadores/criar_contador.html",
                                   mensagem = mensagem)

    def obter_formulario_contador():
        if request.method == "GET":
            impressoras_query = 'SELECT id_impressoras, modelo FROM impressoras'
            impressoras = conector_banco_de_dados.conector_banco_de_dados(impressoras_query).consultar()
            setores_query = "SELECT id_setores, nome_setor FROM setores"
            setores = conector_banco_de_dados.conector_banco_de_dados(setores_query).consultar()
            produtos_query = "SELECT id_produtos, descricao FROM produtos"
            produtos = conector_banco_de_dados.conector_banco_de_dados(produtos_query).consultar()
            return render_template("/contadores/criar_contador.html",
                                   impressoras=impressoras,
                                   setores=setores,
                                   produtos=produtos)
        
    def editar_contador(id_contador):
        id_impressoras = request.form["id_impressoras"]
        id_setores = request.form["id_setores"]
        id_produtos = request.form["id_produtos"]
        data_coleta = request.form["data_coleta"]
        paginas_impressas = request.form["paginas_impressas"]
        mes_referente = request.form["mes_referente"]
        update_query = f"""
            UPDATE contadores
            SET id_impressoras = '{id_impressoras}', id_setores = '{id_setores}', id_produtos = '{id_produtos}', data_coleta = '{data_coleta}', paginas_impressas = '{paginas_impressas}', mes_referente = '{mes_referente}'
            WHERE id_contadores = '{id_contador}'
        """
        conector_banco_de_dados.conector_banco_de_dados(update_query).alterar_incluir_excluir()
        return redirect(url_for('contadores'))
    
    def obter_contador(id_contador):
        if request.method == 'GET':
            contador = conector_banco_de_dados.conector_banco_de_dados(f"SELECT * FROM contadores WHERE id_contadores = {id_contador}").consultar()
            if contador:
                contador = contador[0]
                contador_dict = {
                    'id_impressoras': contador[1],
                    'id_setores': contador[2],
                    'id_produtos': contador[3],
                    'data_coleta': contador[4],
                    'paginas_impressas': contador[5],
                    'mes_referente': contador[6]
                }
                return render_template('contadores/editar_contador.html', contador=contador_dict)
    
    def excluir_contador(id_contador):
        delete_query = f"DELETE FROM contadores WHERE id_contadores = {id_contador}"
        conector_banco_de_dados.conector_banco_de_dados(delete_query).alterar_incluir_excluir()
        return redirect(url_for('contadores'))