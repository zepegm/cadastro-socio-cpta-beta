from conexaoBD import Conexao
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors

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
    if valor == '':
        return 'null'
    else:
        return valor

@app.route('/cadastro-cpta/', methods=['GET', 'POST'])
def login():
    # se tiver logado já vai direto pra home
    if 'loggedin' in session:
        return render_template('home.html')

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

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('select id, nome, rg, cpf from cidadao order by nome')
        #cursor.execute('select * from retirada_cesta')
        listaPessoas = cursor.fetchall()
        ultimasDatas = []
        dadosPessoais = []
        id_selecao = 0
        msg = ''

        if 'selecao' in request.form:
            codigoSQL = "select cidadao.nis, cidadao.sus, cidadao.data_nascimento, cidadao.telefone, cidadao.celular, cidadao.cidade_natal, cidadao.uf_natal, cidadao.profissao, cidadao.renda_familiar_sm, cidadao.numero_filhos, cidadao.participacao_social, cidadao.desc_participacao_social, cidadao.raca, cidadao.observacoes, estado_civil.descricao as 'estado_civil', escolaridade.descricao as 'escolaridade', religiao.religiao from cidadao LEFT JOIN religiao on religiao.id = cidadao.id_religiao LEFT JOIN estado_civil on cidadao.id_estado_civil = estado_civil.id LEFT JOIN escolaridade on cidadao.id_escolaridade = escolaridade.id where cidadao.id = %s" % (request.form['selecao'])
            print(codigoSQL)
            cursor.execute(codigoSQL)
            dadosPessoais = cursor.fetchone()
            id_selecao = request.form['selecao']

        if 'data_nova' in request.form and int(request.form['selecao_update']) > 0:
            id_selecao = request.form['selecao_update']
            nova_data = request.form['data_nova']
            codigoSQL = "INSERT INTO retirada_cesta VALUES(%s, '%s')" % (id_selecao, nova_data)
            print(codigoSQL)
            cursor.execute(codigoSQL)
            mysql.connection.commit()
            msg='Cadastro efetuado com sucesso!'

        for pessoa in listaPessoas:
            codigoSQL = "select id_cidadao, DATE_FORMAT(max(data_retirada), '%d/%m/%Y') as ultimo_dia from retirada_cesta where id_cidadao = " + str(pessoa['id'])
            cursor.execute(codigoSQL)
            ultima_data = cursor.fetchone()
            ultimasDatas.append(ultima_data)

        return render_template('home.html', msg=msg, ultimasDatas=ultimasDatas, id_selecao=id_selecao, dadosPessoais=dadosPessoais, nome=nome, listaPessoas=listaPessoas)
    else:
        return render_template('index.html', msg='')


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
        chefe_familia = request.form['chefe_familia']
        nome = "'" + request.form['nome'] + "'"
        rg = "'" + request.form['rg'] + "'"
        cpf = "'" + request.form['cpf'] + "'"
        nis = retornarIntSQL(request.form['nis'])
        sus = retornarIntSQL(request.form['sus'])
        data_nascimento = "'" + request.form['data_nascimento'] + "'"
        telefone = retornarStringSQL(request.form['telefone'])
        celular = retornarStringSQL(request.form['celular'])
        cidade = "'" + request.form['cidade_natal'] + "'"
        estado = "'" + request.form['uf_natal'] + "'"
        profissao = retornarStringSQL(request.form['profissao'])
        renda_familiar = retornarIntSQL(request.form['renda_familiar_sm'])
        num_filhos = retornarIntSQL(request.form['numero_filhos'])
        participacao_social = request.form['participacao_social']
        desc_part_social = retornarStringSQL(request.form['desc_participacao_social'])
        raca = retornarStringSQL(request.form['raca'])
        estadocivil_sql = retornarIntSQL(request.form['estado_civil'])
        escolaridade_sql = retornarIntSQL(request.form['escolaridade'])
        religiao_sql = retornarIntSQL(request.form['religiao'])
        entrevistador = session['id']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        codigoSQL = 'INSERT INTO cidadao VALUES(null, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, null, null, null, %s, NOW(), NOW(), %s, %s, %s, null, %s)' % \
            (chefe_familia, nome, rg, cpf, nis, sus, data_nascimento, telefone, celular, cidade, estado, profissao, renda_familiar, num_filhos, participacao_social, desc_part_social, raca, \
            estadocivil_sql, escolaridade_sql, religiao_sql, entrevistador)

        cursor.execute(codigoSQL)

        # executar novos cadastros
        ultimo_id = mysql.connection.insert_id()
        
        beneficios_list = request.form.getlist('beneficios')
        for val in beneficios_list:
            cursor.execute('insert into cidadaoxbeneficios values(%s, %s)', (ultimo_id, val))

        servicos_saude_list = request.form.getlist('servicos_saude')
        for val in servicos_saude_list:
            cursor.execute('insert into cidadaoxservico_saude values(%s, %s)', (ultimo_id, val))

        cultura_lazer_list = request.form.getlist('cultura_lazer')
        for val in cultura_lazer_list:
            cursor.execute('insert into cidadaoxcultura_lazer values(%s, %s)', (ultimo_id, val))


        # imovel
        imovel_id = request.form['imovel']
        endereco = "'" + request.form['endereco'] + "'"
        area = "'" + request.form['area'] + "'"

        if 'correio' in request.form:
            correio = retornarIntSQL(request.form['correio'])
        else:
            correio = 'null'

        if 'entregacomercio' in request.form:
            entrega_comercio = retornarIntSQL(request.form['entregacomercio'])
        else:
            entrega_comercio = 'null'

        codigoSQL = 'INSERT INTO situacao_habitacional VALUES(%s, %s, %s, null, null, null, null, %s, %s, %s, null)' % (ultimo_id, imovel_id, endereco, correio, entrega_comercio, area) 
        print(codigoSQL)
        cursor.execute(codigoSQL)

        print(endereco)

        mysql.connection.commit()

        #print(ultimo_id)
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

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)