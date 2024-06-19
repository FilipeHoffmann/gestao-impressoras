from flask import render_template, request, url_for, redirect
from static.scripts import conector_banco_de_dados

class class_contadores:
    @staticmethod
    def contadores(mes):
        if request.method == "GET":
            if mes == None:
                query = conector_banco_de_dados.conector_banco_de_dados(f'''
                SELECT contadores.id_contadores, contadores.id_impressoras, secretarias.nome, setores.nome_setor, contadores.data_coleta, contadores.paginas_impressas, contadores.mes_referente, contadores.proporcao_mes 
                FROM contadores
                INNER JOIN impressoras ON impressoras.id_impressoras = contadores.id_impressoras
                INNER JOIN setores ON setores.id_setores = impressoras.id_setores
                INNER JOIN secretarias ON secretarias.id_secretarias = setores.id_secretarias''')
            else:
                query = conector_banco_de_dados.conector_banco_de_dados(f'''
                SELECT contadores.id_contadores, contadores.id_impressoras, secretarias.nome, setores.nome_setor, contadores.data_coleta, contadores.paginas_impressas, contadores.mes_referente, contadores.proporcao_mes
                FROM contadores
                INNER JOIN impressoras ON impressoras.id_impressoras = contadores.id_impressoras
                INNER JOIN setores ON setores.id_setores = impressoras.id_setores
                INNER JOIN secretarias ON secretarias.id_secretarias = setores.id_secretarias
                WHERE "{mes}" = mes_referente''')
                
            contadores = query.consultar()
            return render_template("/contadores/contadores.html",
                                mes = mes,
                                contadores=contadores)
            
    def criar_contador():
        if request.method == "POST":
            id_impressoras = request.form["id_impressoras"]
            id_setores = request.form["id_setores"]
            id_produtos = request.form["id_produtos"]
            data_coleta = request.form["data_coleta"]
            paginas_impressas = request.form["paginas_impressas"]
            mes_referente = request.form["mes_referente"]
            proporcao_mes = request.form["proporcao_mes"]
            query = f'''INSERT INTO contadores(id_impressoras,id_setores,id_produtos,data_coleta,paginas_impressas,mes_referente,proporcao_mes)
                    VALUES ('{id_impressoras}','{id_setores}','{id_produtos}','{data_coleta}','{paginas_impressas}','{mes_referente}','{proporcao_mes}')'''
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
        data_coleta = request.form["data_coleta"]
        paginas_impressas = request.form["paginas_impressas"]
        mes_referente = request.form["mes_referente"]
        proporcao_mes= request.form["proporcao_mes"]
        update_query = f"""
            UPDATE contadores
            SET id_impressoras = '{id_impressoras}', data_coleta = '{data_coleta}', paginas_impressas = '{paginas_impressas}', mes_referente = '{mes_referente}', proporcao_mes = '{proporcao_mes}'
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
                    'data_coleta': contador[2],
                    'paginas_impressas': contador[3],
                    'mes_referente': contador[4],
                    'proporcao_mes': contador[5]
                }
                return render_template('contadores/editar_contador.html', contador=contador_dict)
    
    def excluir_contador(id_contador):
        delete_query = f"DELETE FROM contadores WHERE id_contadores = {id_contador}"
        conector_banco_de_dados.conector_banco_de_dados(delete_query).alterar_incluir_excluir()
        return redirect(url_for('contadores'))