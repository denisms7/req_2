from app import db


class Usuarios(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_usuario = db.Column(db.String(50), unique=True)
    senha = db.Column(db.String(20))
    nome = db.Column(db.String)
    email = db.Column(db.String, unique=True)

    def __init__(self, nome_usuario, senha, nome, email):
        self.nome_usuario = nome_usuario
        self.senha = senha
        self.nome = nome
        self.email = email





class Cadastros(db.Model):
    __tablename__ = 'cadastros'
    # ID
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # Pessoa Juridica
    razao_social = db.Column(db.String(150))
    nome_fantasia = db.Column(db.String(150))
    cnpj = db.Column(db.String(15))
    ins_estadual = db.Column(db.String(15))
    data_abertura = db.Column(db.Date())
    outros_empresa = db.Column(db.String(255))
    # Pessoa Fisica
    nome = db.Column(db.String(50))
    sobrenome = db.Column(db.String(150))
    cpf = db.Column(db.String(15))
    rg = db.Column(db.String(15))
    emissor = db.Column(db.String(5))
    data_expedicao = db.Column(db.Date())
    data_nascimento = db.Column(db.Date())
    escolaridade = db.Column(db.String(150))
    sexo = db.Column(db.String(15))
    estado_civil = db.Column(db.String(50))
    conjuge_nome = db.Column(db.String(50))
    conjuge_sobrenome = db.Column(db.String(150))
    nome_mae = db.Column(db.String(50))
    sobrenome_mae = db.Column(db.String(150))
    nome_pai = db.Column(db.String(50))
    sobrenome_pai = db.Column(db.String(150))
    outros_pessoais = db.Column(db.String(255))
    # Contato
    email_1 = db.Column(db.String(150))
    email_2 = db.Column(db.String(150))
    telefone = db.Column(db.String(20))
    telefone1 = db.Column(db.String(20))
    telefone2 = db.Column(db.String(20))
    outros_contato = db.Column(db.String(255))
    # Edereco
    cep = db.Column(db.String(10))
    uf = db.Column(db.String(2))
    cidade = db.Column(db.String(150))
    bairro = db.Column(db.String(150))
    rua = db.Column(db.String(150))
    numero = db.Column(db.Integer())
    complemento  = db.Column(db.String(255))
    # Status
    ativo_inativo = db.Column(db.Integer())
    # Sistema
    sistema_att = db.Column(db.Date())
    sistema_att_usuario = db.Column(db.String(150))

class Requisicao(db.Model):
    __tablename__ = 'requisicao'
    # ID
    req_id = db.Column(db.Integer, primary_key=True)
    req_data_cadastro = db.Column(db.DateTime(6))
    req_status = db.Column(db.Integer)

    req_emissor = db.Column(db.String(150))
    req_responsavel = db.Column(db.String(255))
    req_solicitante = db.Column(db.String(255))
    req_setor = db.Column(db.String(255))
    req_empresa = db.Column(db.String(255))
    req_observacao = db.Column(db.Text())

    def __init__(self, req_emissor, req_responsavel, req_solicitante, req_setor, req_empresa, req_observacao):
        self.req_emissor = req_emissor
        self.req_responsavel = req_responsavel
        self.req_solicitante = req_solicitante
        self.req_setor = req_setor
        self.req_empresa = req_empresa
        self.req_observacao = req_observacao