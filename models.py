# coding: utf-8
from flask_sqlalchemy import SQLAlchemy
from wtforms_sqlalchemy.orm import model_form


db = SQLAlchemy()


t_situacao_habitacionalxtransporte = db.Table(
    'situacao_habitacionalxtransporte',
    db.Column('situacao_habitacional_id', db.ForeignKey('situacao_habitacional.id'), primary_key=True, nullable=False, index=True),
    db.Column('transporte_id', db.ForeignKey('transporte.id'), primary_key=True, nullable=False, index=True)
)


t_cidadaoxbeneficios = db.Table(
    'cidadaoxbeneficios',
    db.Column('id_cidadao', db.ForeignKey('cidadao.id'), primary_key=True, nullable=False, index=True),
    db.Column('id_beneficio', db.ForeignKey('beneficio.id'), primary_key=True, nullable=False, index=True)
)


t_cidadaoxinformacoes_adicionais = db.Table(
    'cidadaoxinformacoes_adicionais',
    db.Column('id_cidadao', db.ForeignKey('cidadao.id'), primary_key=True, nullable=False, index=True),
    db.Column('id_informacoes_adicionais', db.ForeignKey('informacoes_adicionais.id'), primary_key=True, nullable=False, index=True)
)



t_cidadaoxsaude = db.Table(
    'cidadaoxsaude',
    db.Column('cidadao_id', db.ForeignKey('cidadao.id'), primary_key=True, nullable=False, index=True),
    db.Column('saude_id', db.ForeignKey('saude.id'), primary_key=True, nullable=False, index=True)
)



t_cidadaoxservico_saude = db.Table(
    'cidadaoxservico_saude',
    db.Column('id_cidadao', db.ForeignKey('cidadao.id'), primary_key=True, nullable=False, index=True),
    db.Column('id_servico_saude', db.ForeignKey('servico_saude.id'), primary_key=True, nullable=False, index=True)
)



class Account(db.Model):
    __tablename__ = 'accounts'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    senha = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(255), nullable=False)


AccountForm = model_form(Account)



class Beneficio(db.Model):
    __tablename__ = 'beneficio'

    id = db.Column(db.Integer, primary_key=True)
    beneficio = db.Column(db.String(255), nullable=False)

    cidadao = db.relationship('Cidadao', secondary='cidadaoxbeneficios', backref='beneficios')



class CidadaoxculturaLazer(db.Model):
    __tablename__ = 'cidadaoxcultura_lazer'

    cidadao_id = db.Column(db.ForeignKey('cidadao.id'), primary_key=True, nullable=False, index=True)
    cultura_lazer_id = db.Column(db.ForeignKey('cultura_lazer.id'), primary_key=True, nullable=False, index=True)
    descricao = db.Column(db.String(255))

    cidadao = db.relationship('Cidadao', primaryjoin='CidadaoxculturaLazer.cidadao_id == Cidadao.id', backref='cidadaoxcultura_lazers')
    cultura_lazer = db.relationship('CulturaLazer', primaryjoin='CidadaoxculturaLazer.cultura_lazer_id == CulturaLazer.id', backref='cidadaoxcultura_lazers')



class Covid(db.Model):
    __tablename__ = 'covid'

    id = db.Column(db.Integer, primary_key=True)
    infeccao_familia = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    quantidade_pessoas = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    familia_afetada = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    afetacao = db.Column(db.String(255))



class CulturaLazer(db.Model):
    __tablename__ = 'cultura_lazer'

    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(255))



class Escolaridade(db.Model):
    __tablename__ = 'escolaridade'

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(45), nullable=False)



class EstadoCivil(db.Model):
    __tablename__ = 'estado_civil'

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(45), nullable=False)



class InformacoesAdicionai(db.Model):
    __tablename__ = 'informacoes_adicionais'

    id = db.Column(db.Integer, primary_key=True)
    luto_recente = db.Column(db.Integer)
    falecido = db.Column(db.String(45))
    motivo_falecimento = db.Column(db.String(255))
    amse_psc_la = db.Column(db.Integer)
    qtde_amse_psc_la = db.Column(db.Integer)
    amse_fc = db.Column(db.Integer)
    qtde_amse_fc = db.Column(db.Integer)
    sistema_prisional = db.Column(db.Integer)
    quem_sistema_prisional = db.Column(db.String(255))
    sistema_acolhimento = db.Column(db.Integer)
    sistema_acolhimento_c_i = db.Column(db.Enum('C', 'I'))
    onde_sistema_acolhimento = db.Column(db.String(255))
    situacao_violencia = db.Column(db.Integer)
    violencia_domestica = db.Column(db.Integer)
    violencia_trabalho = db.Column(db.Integer)
    violencia_rua = db.Column(db.Integer)
    violencia_escola = db.Column(db.Integer)
    violencia_fisica = db.Column(db.Integer)
    violencia_verbal = db.Column(db.Integer)



class Religiao(db.Model):
    __tablename__ = 'religiao'

    id = db.Column(db.Integer, primary_key=True)
    religiao = db.Column(db.String(255), nullable=False)



class RetiradaCesta(db.Model):
    __tablename__ = 'retirada_cesta'

    id = db.Column(db.Integer, primary_key=True)
    data_retirada = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    id_cidadao = db.Column(db.ForeignKey('cidadao.id'), nullable=False, index=True)

    cidadao = db.relationship('Cidadao', primaryjoin='RetiradaCesta.id_cidadao == Cidadao.id', backref='retirada_cestas')



class Saude(db.Model):
    __tablename__ = 'saude'

    id = db.Column(db.Integer, primary_key=True)
    deficiencia_fisica = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    saude_mental = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    hiv_aids = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    dependencia_quimica = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    cancer = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    diabetes = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    hipertensao = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    obesidade = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    gestante = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    outros = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    descricao_outros = db.Column(db.String(255))
    dengue = db.Column(db.Integer, nullable=False)
    vezes_dengue = db.Column(db.Integer)



class ServicoSaude(db.Model):
    __tablename__ = 'servico_saude'

    id = db.Column(db.Integer, primary_key=True)
    servico = db.Column(db.String(255), nullable=False)



class SituacaoHabitacional(db.Model):
    __tablename__ = 'situacao_habitacional'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    tipo_imovel = db.Column(db.ForeignKey('tipo_imovel.id'), primary_key=True, nullable=False, index=True)
    endereco = db.Column(db.String(255), nullable=False)
    agua = db.Column(db.Integer)
    luz = db.Column(db.Integer)
    esgoto = db.Column(db.Integer)
    coleta_lixo = db.Column(db.Integer)
    entrega_correios = db.Column(db.Integer)
    entrega_comercio = db.Column(db.Integer)
    area_municipio = db.Column(db.Enum('U', 'R'), nullable=False, info='U = Urbano\\nR = Rural')
    num_comodos = db.Column(db.Integer, nullable=False)

    tipo_imovel1 = db.relationship('TipoImovel', primaryjoin='SituacaoHabitacional.tipo_imovel == TipoImovel.id', backref='situacao_habitacionals')
    transportes = db.relationship('Transporte', secondary='situacao_habitacionalxtransporte', backref='situacao_habitacionals')


class TipoImovel(db.Model):
    __tablename__ = 'tipo_imovel'

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(255), nullable=False)



class Transporte(db.Model):
    __tablename__ = 'transporte'

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(255), nullable=False)
    necessario = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    disponibilidade = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class Cidadao(db.Model):
    __tablename__ = 'cidadao'

    id = db.Column(db.Integer, primary_key=True)
    chefe_familia = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    nome = db.Column(db.String(255), nullable=False)
    rg = db.Column(db.String(15))
    cpf = db.Column(db.String(14))
    nis = db.Column(db.String(45))
    sus = db.Column(db.Integer)
    data_nascimento = db.Column(db.String(10), nullable=False)
    cidade_natal = db.Column(db.String(255))
    uf_natal = db.Column(db.String(2))
    vinculo_familiar = db.Column(db.String(45))
    profissao = db.Column(db.String(255))
    ocupacao_formal = db.Column(db.Integer)
    renda_familiar_sm = db.Column(db.Integer)
    numero_filhos = db.Column(db.Integer)
    participacao_social = db.Column(db.Integer)
    desc_participacao_social = db.Column(db.String(255))
    obs_saude = db.Column(db.String(255))
    conhece_cidade = db.Column(db.Integer)
    locais_nao_visitados = db.Column(db.String)
    id_chefe_familia = db.Column(db.ForeignKey('cidadao.id'), index=True)
    id_situacao_habitacional = db.Column(db.ForeignKey('situacao_habitacional.id'), index=True)
    covid = db.Column(db.ForeignKey('covid.id'), index=True)
    talentos_habilidades = db.Column(db.String)
    raca = db.Column(db.Enum('B', 'P', 'PD', 'A', 'I'), info='B = Branco\\nP = Preto\\nPD = Pardo\\nA = Amarelo\\nI = Indio')
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    updated_at = db.Column(db.DateTime)
    id_estado_civil = db.Column(db.ForeignKey('estado_civil.id'), nullable=False, index=True)
    id_escolaridade = db.Column(db.ForeignKey('escolaridade.id'), nullable=False, index=True)
    id_religiao = db.Column(db.ForeignKey('religiao.id'), nullable=False, index=True)
    email = db.Column(db.String(100))
    observacoes = db.Column(db.String)
    entrevistador = db.Column(db.ForeignKey('accounts.id'), index=True)

    covid1 = db.relationship('Covid', primaryjoin='Cidadao.covid == Covid.id', backref='cidadaos')
    account = db.relationship('Account', primaryjoin='Cidadao.entrevistador == Account.id', backref='cidadaos')
    parent = db.relationship('Cidadao', remote_side=[id], primaryjoin='Cidadao.id_chefe_familia == Cidadao.id', backref='cidadaos')
    escolaridade = db.relationship('Escolaridade', primaryjoin='Cidadao.id_escolaridade == Escolaridade.id', backref='cidadaos')
    estado_civil = db.relationship('EstadoCivil', primaryjoin='Cidadao.id_estado_civil == EstadoCivil.id', backref='cidadaos')
    religiao = db.relationship('Religiao', primaryjoin='Cidadao.id_religiao == Religiao.id', backref='cidadaos')
    situacao_habitacional = db.relationship('SituacaoHabitacional', primaryjoin='Cidadao.id_situacao_habitacional == SituacaoHabitacional.id', backref='cidadaos')
    informacoes_adicionais = db.relationship('InformacoesAdicionai', secondary='cidadaoxinformacoes_adicionais', backref='cidadaos')
    saudes = db.relationship('Saude', secondary='cidadaoxsaude', backref='cidadaos')
    servico_saude = db.relationship('ServicoSaude', secondary='cidadaoxservico_saude', backref='cidadaos')
