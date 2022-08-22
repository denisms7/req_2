from app import app
from flask import render_template, request, redirect


@app.route("/")
def index():
    title = 'Menu'
    return render_template('index.html', title=title)

@app.route("/cadastro-cpf", methods=['GET', 'POST'])
def cadastro_cpf():
    title = 'Cadastros CPF'
    tipo = 0
    return render_template('cadastro.html', title=title, tipo=tipo)

@app.route("/cadastro-cnpj", methods=['GET', 'POST'])
def cadastro_cnpj():
    title = 'Cadastros CNPJ'
    tipo = 1
    return render_template('cadastro.html', title=title, tipo=tipo)


@app.route("/busca-pessoa-fisica")
def pessoa_fisica():
    title = 'Pessoa Fisica'
    tipo = 0
    cad = Cadastros.query.all()
    return render_template('cadastro_pesquisa.html', title=title, tipo=tipo,  cad=cad)


@app.route("/busca-pessoa-juridica")
def pessoa_juridica():
    title = 'Pessoa Juridica'
    tipo = 1
    cad = Cadastros.query.all()
    return render_template('cadastro_pesquisa.html', title=title, tipo=tipo,  cad=cad)


@app.route("/requisicao-busca")
def requisicao_pesquisa():
    title = 'Pessoa Juridica'
    tipo = 1
    db_req = Requisicao.query.all()
    return render_template('requisicao_pesquisa.html', title=title, tipo=tipo,  db_req=db_req)


@app.route("/requisicao", methods=['GET', 'POST'])
def requisicao():
    title = 'Requisição'
    if request.method == 'POST':
        data = Requisicao(request.form['req_emissor'],
                          request.form['req_responsavel'],
                          request.form['req_solicitante'],
                          request.form['req_setor'],
                          request.form['req_empresa'],
                          request.form['req_observacao'])
        db.session.add(data)
        db.session.commit()

        return redirect(url_for('requisicao_pesquisa'))
    else:
        return render_template('requisicao.html', title=title)



# Pagina de Erro
@app.route("/<string:variavel>")
def erro_pag(variavel):
    title = '#Erro'
    return render_template('erro.html', variavel=variavel, title=title)