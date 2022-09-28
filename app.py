from telnetlib import theNULL
from conexaoBD import Conexao
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_mysqldb import MySQL
from cep import retornarCEP
from datetime import date
import json

app=Flask(__name__)

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'your secret key'

# Enter your database connection details below
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_PORT']=3306
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='Yasmin'
app.config['MYSQL_DB']='cadastro_socioeconomico'

cred = {'HOST':'ec2-34-197-84-74.compute-1.amazonaws.com', 'PORT':5432, 'USER':'piendkrxzduecj', 'PASSWORD':'5af529088848fd2537e0c97f22469dc181a79b2a1cfcc98de6959275e13cab3d', 'DB':'do5a2tog3uf07'}

# Intialize MySQL
mysql = MySQL(app)
banco = Conexao(cred)

def popularCombo(tabela):
    valores = banco.consultar('select * from ' + tabela)

    if len(valores) > 0:
        return valores
    else:
        return [(1, 'Banco está vazio')]

def retornarStringSQL(valor):
    if valor == '':
        return 'null'
    else:
        return "'" + valor + "'"

def retornarIntSQL(valor):
    if valor == '' or valor == '0':
        return 'null'
    else:
        return valor

@app.route('/', methods=['GET', 'POST'])
def login():
    # se tiver logado já vai direto pra home
    if 'loggedin' in session:
        return redirect(url_for('home'))

    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using SQLite
        sql = 'select * from accounts WHERE email like ' + "'" +  username + "' AND senha like MD5('" + password + "')"
        account = banco.consultar(sql)
        print(sql)
        # If account exists in accounts table in out database
        if account:
            print(account)
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account[0][0]
            session['nome'] = account[0][1]
            session['email'] = account[0][3]
            # Redirect to home page
            return redirect(url_for('home'))
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'E-mail/senha incorreto(s)!'
    # Show the login form with message (if any)
    return render_template('index.html', msg=msg)


@app.route('/cadastro-cpta/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('nome', None)
   # Redirect to login page
   return redirect(url_for('login'))


@app.route('/cadastro-cpta/home', methods=['GET', 'POST'])
def home():
    if 'loggedin' in session:
        nome = session['nome']

        id_selecao = 0
        msg = ''

        if 'data_nova' in request.form and int(request.form['selecao_update']) > 0:
            id_selecao = request.form['selecao_update']
            nova_data = request.form['data_nova']
            codigoSQL = "INSERT INTO retirada_cesta VALUES('%s', %s)" % (nova_data, id_selecao)
            banco.manipular(codigoSQL)
            msg='Cadastro efetuado com sucesso!'

        listaPessoas = banco.consultarDict("select id, nome, rg, substr(lpad(cpf::text, 11, '0'), 1, 3) || '.' || substr(lpad(cpf::text, 11, '0'), 4, 3) || '.' || substr(lpad(cpf::text, 11, '0'), 7, 3) || '-' || substr(lpad(cpf::text, 11, '0'), 10) as cpf, to_char(max(data_retirada), 'DD/MM/YYYY') as ultima_retirada from cidadao LEFT JOIN retirada_cesta ON cidadao.id = retirada_cesta.id_cidadao group by cidadao.id order by nome limit 20 offset 0")

        return render_template('home.html', msg=msg, id_selecao=id_selecao, nome=nome, listaPessoas=listaPessoas, hoje=date.today())
    else:
        return render_template('index.html', msg='')


@app.route('/exibirDetalhes', methods=['GET', 'POST'])
def exibirDetalhes():
    if request.method == 'POST':
        if request.is_json:
            id = request.json
            pessoa = {}
            códigoSQL = "select cidadao.nome, cidadao.rg, substr(lpad(cpf::text, 11, '0'), 1, 3) || '.' || substr(lpad(cpf::text, 11, '0'), 4, 3) || '.' || substr(lpad(cpf::text, 11, '0'), 7, 3) || '-' || substr(lpad(cpf::text, 11, '0'), 10) as cpf, cidadao.chefe_familia, cidadao.endereco, cidadao.nis, cidadao.sus, to_char(cidadao.nascimento, 'DD/MM/YYYY') as nascimento, cidadao.telefone, cidadao.celular, cidadao.email, cidadao.cidade, cidadao.estado, cidadao.profissao, cidadao.renda, cidadao.num_filhos, cidadao.atividades_soc, cidadao.desc_atividades_soc, raca_cor.descricao as raca, estado_civil.descricao as estado_civil, escolaridade.descricao as escolaridade, religiao.descricao as religiao from cidadao LEFT JOIN religiao on religiao.id = cidadao.religiao LEFT JOIN estado_civil on cidadao.estado_civil = estado_civil.id LEFT JOIN escolaridade on cidadao.escolaridade = escolaridade.id LEFT JOIN raca_cor on cidadao.raca = raca_cor.id where cidadao.id = {}".format(id)
            dadosPessoais = banco.consultarDict(códigoSQL)[0]

            for k, v in dadosPessoais.items():
                if dadosPessoais[k] is None:
                    dadosPessoais[k] = '-'

            pessoa['dadosPessoais'] = dadosPessoais
            pessoa['beneficios'] = banco.consultarDict('select beneficio.descricao from cidadao_x_beneficios LEFT JOIN beneficio on cidadao_x_beneficios.id_beneficio = beneficio.id where cidadao_x_beneficios.id_cidadao = {}'.format(id))
            pessoa['servicos_saude'] = banco.consultarDict('select servico_saude.descricao from cidadao_x_saude LEFT JOIN servico_saude on cidadao_x_saude.id_saude = servico_saude.id where cidadao_x_saude.id_cidadao = {}'.format(id))
            pessoa['cultura'] = banco.consultarDict('select cultura_lazer.descricao from cidadao_x_cultura LEFT JOIN cultura_lazer on cidadao_x_cultura.id_cultura = cultura_lazer.id where cidadao_x_cultura.id_cidadao = {}'.format(id))
            pessoa['transporte'] = banco.consultarDict("select transporte.descricao, case when tem = true then 'Sim' else 'Não' end as tem, case when necessita = true then 'Sim' else 'Não' end as necessita from cidadao_x_transporte LEFT JOIN transporte ON cidadao_x_transporte.id_transporte = transporte.id WHERE cidadao_x_transporte.id_cidadao = {} order by cidadao_x_transporte.id_transporte".format(id))
            pessoa['composicao_familiar'] = banco.consultarDict("select COALESCE(nome, '-') as nome, COALESCE(substr(lpad(cpf::text, 11, '0'), 1, 3) || '.' || substr(lpad(cpf::text, 11, '0'), 4, 3) || '.' || substr(lpad(cpf::text, 11, '0'), 7, 3) || '-' || substr(lpad(cpf::text, 11, '0'), 10), '-') as cpf, COALESCE(estado_civil.descricao, '-') as estado_civil, COALESCE(vinculo, '-') as vinculo, COALESCE(to_char(nascimento, 'DD/MM/YYYY'), '-') as nascimento, COALESCE(escolaridade.descricao, '-') as escolaridade, COALESCE(profissao, '-') as profissao, case when formal = true then 'Sim' else 'Não' end as formal, COALESCE(situacao_saude.descricao, '-') as situacao_saude from composicao_familiar LEFT JOIN estado_civil ON estado_civil.id = composicao_familiar.estado_civil LEFT JOIN escolaridade ON escolaridade.id = composicao_familiar.escolaridade LEFT JOIN situacao_saude ON situacao_saude.id = composicao_familiar.situacao_saude where id_cidadao = {}".format(id))
            if len(pessoa['beneficios']) > 0 or len(pessoa['servicos_saude']) > 0 or len(pessoa['cultura']) > 0 or len(pessoa['transporte']) > 0: 
                pessoa['rel'] = True
            else:
                pessoa['rel'] = False

            return jsonify(pessoa)


@app.route('/cadastro-cpta/cadastro_cidadao', methods=['GET', 'POST'])
def cadastro_cidadao():

    escolaridade = popularCombo('escolaridade')
    estadocivil = popularCombo('estado_civil')
    religiao = popularCombo('religiao')
    beneficios = popularCombo('beneficio')
    servicos_saude = popularCombo('servico_saude')
    cultura_lazer = popularCombo('cultura_lazer')
    imovel = popularCombo('tipo_imovel')
    transporte = popularCombo('transporte')
    situacao_saude = popularCombo('situacao_saude')
    raca_cor = popularCombo('raca_cor')

    msg = ''

    # agora é hora de receber os dados
    if request.method=='POST' and 'nome' in request.form:
        #print(request.form)
        chefe_familia = request.form['chefe_familia']
        nome = "'" + request.form['nome'] + "'"

        # montar endereço
        endereco = "'" + request.form['rua'] + ', ' + request.form['num_casa'] + ', ' + request.form['bairro'] + ', ' + request.form['cidade'] + ', ' + request.form['estado_casa'] + "'"
        #endereco = "'" + request.form['endereco'] + "'"
        
        rg = "'" + request.form['rg'] + "'"
        cpf = request.form['cpf'].replace('.', '').replace('-', '').zfill(11)
        nis = retornarIntSQL(request.form['nis'])
        sus = retornarIntSQL(request.form['sus'])
        data_nascimento = "'" + request.form['data_nascimento'] + "'"
        telefone = retornarStringSQL(request.form['telefone']) 
        celular = retornarStringSQL(request.form['celular'])
        email = retornarStringSQL(request.form['email'])
        cidade = "'" + request.form['cidade_natal'] + "'"
        estado = "'" + request.form['uf_natal'] + "'"
        profissao = retornarStringSQL(request.form['profissao'])
        renda_familiar = retornarIntSQL(request.form['renda_familiar_sm'])
        num_filhos = retornarIntSQL(request.form['numero_filhos'])
        participacao_social = request.form['participacao_social']
        desc_part_social = retornarStringSQL(request.form['desc_participacao_social'])
        raca = retornarIntSQL(request.form['raca'])
        estadocivil_sql = retornarIntSQL(request.form['estado_civil'])
        escolaridade_sql = retornarIntSQL(request.form['escolaridade'])
        religiao_sql = retornarIntSQL(request.form['religiao'])
        # situação habitacional
        imovel_id = request.form['imovel']
        area = "'" + request.form['area'] + "'"
        if 'correio' in request.form:
            correio = request.form['correio']
        else:
            correio = 'null'
        if 'entregacomercio' in request.form:
            entrega_comercio = request.form['entregacomercio']
        else:
            entrega_comercio = 'null'

        #entrevistador = session['id']

        #cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        codigoSQL = 'INSERT INTO cidadao(nome, nascimento, telefone, celular, email, endereco, rg, cpf, nis, sus, chefe_familia, cidade, estado, escolaridade, raca, profissao, renda, num_filhos, estado_civil, religiao, atividades_soc, desc_atividades_soc, tipo_imovel, area, correio, entrega) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id' % \
            (nome, data_nascimento, telefone, celular, email, endereco, rg, cpf, nis, sus, chefe_familia, cidade, estado, escolaridade_sql, raca, profissao, renda_familiar, num_filhos, estadocivil_sql, religiao_sql, participacao_social, desc_part_social, imovel_id, area, correio, entrega_comercio)


        print(codigoSQL)
        
        # executar novos cadastros
        ultimo_id = banco.inserir(codigoSQL)[0]
        #print(ultimo_id)

        # gravar benefícios
        beneficios_list = request.form.getlist('beneficios')
        for val in beneficios_list:
            banco.manipular('insert into cidadao_x_beneficios values({}, {})'.format(ultimo_id, val))

        # gravar serviços de saúde
        servicos_saude_list = request.form.getlist('servicos_saude')
        for val in servicos_saude_list:
            banco.manipular('insert into cidadao_x_saude values({}, {})'.format(ultimo_id, val))

        # gravar lista de cultura e lazer
        cultura_lazer_list = request.form.getlist('cultura_lazer')
        for val in cultura_lazer_list:
            banco.manipular('insert into cidadao_x_cultura values({}, {})'.format(ultimo_id, val))

        # transporte
        transporte_tem = request.form.getlist('transporte_tem')
        for val in transporte_tem:
            banco.manipular('insert into cidadao_x_transporte values({}, {}, {}, {})'.format(ultimo_id, val, 'true', 'false'))
            print('insert into cidadao_x_transporte values({}, {}, {}, {})'.format(ultimo_id, val, 'true', 'false'))

        transporte_necessita = request.form.getlist('transporte_necessita')
        for val in transporte_necessita:
            banco.manipular('insert into cidadao_x_transporte values ({}, {}, false, true) on conflict (id_cidadao, id_transporte) Do update set necessita = true'.format(ultimo_id, val))


        # gravar composição familiar        
        composicao_familiar = json.loads(request.form['composicao_familiar'])
        for membro in composicao_familiar:
            sql = "insert into composicao_familiar values({}, {}, {}, {}, {}, {}, {}, {}, {}, {})".format(ultimo_id, retornarIntSQL(membro['cpf']), retornarIntSQL(membro['estado_civil']), retornarStringSQL(membro['vinculo']), retornarStringSQL(membro['nascimento']), retornarIntSQL(membro['escolaridade']), retornarStringSQL(membro['profissao']), membro['formal'], retornarIntSQL(membro['saude']), retornarStringSQL(membro['nome']))
            print(sql)
            banco.manipular(sql)

        msg = 'Gravado com sucesso!'

    if 'loggedin' in session:
        return render_template('formulario-cidadao (completo).jinja', msg=msg, escolaridade=escolaridade, estadocivil=estadocivil, religiao=religiao, beneficios=beneficios, servicos_saude=servicos_saude, cultura_lazer=cultura_lazer, imovel=imovel, transporte=transporte, situacao_saude=situacao_saude, raca = raca_cor)
    else:
        return render_template('index.html', msg='')

@app.route('/cadastro-cpta/registro', methods=['GET', 'POST'])
def registro():
    if 'loggedin' in session:
        if request.method=='POST' and 'nome' in request.form and 'email' in request.form and 'senha' in request.form:
            nome = request.form['nome']
            email = request.form['email']
            senha = request.form['senha']
            
            try:
                if banco.manipular("INSERT INTO accounts(nome, senha, email) VALUES('{}', MD5('{}'), '{}')".format(nome, senha, email)):
                    msg = 'Registro efetuado com suesso!'
                else:
                    msg = 'Erro fatal ao tentar registrar um usuário.'    
            except:
                msg = 'Erro fatal ao tentar registrar um usuário.'
            return render_template('registro.html', msg=msg)

        return render_template('registro.html', msg='')

    return render_template('index.html', msg='')    


@app.route('/buscarCEP', methods=['GET', 'POST'])
def buscarCEP():

    cep = '0'

    if request.method == 'POST':
        #print('got a post request!')

        if request.is_json: # application/json
            # handle your ajax request here!
            cep = request.json

    
    endereco = retornarCEP(cep)

    return jsonify(endereco)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)