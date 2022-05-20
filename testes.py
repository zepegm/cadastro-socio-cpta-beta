from conexaoBD import Conexao

cred = {'HOST':'ec2-34-197-84-74.compute-1.amazonaws.com', 'PORT':5432, 'USER':'piendkrxzduecj', 'PASSWORD':'5af529088848fd2537e0c97f22469dc181a79b2a1cfcc98de6959275e13cab3d', 'DB':'do5a2tog3uf07'}

banco = Conexao(cred)

codigoSQL = "select cidadao.nis, cidadao.sus, cidadao.nascimento, cidadao.telefone, cidadao.celular, cidadao.cidade, cidadao.estado, cidadao.profissao, cidadao.renda, cidadao.num_filhos, cidadao.atividades_soc, cidadao.desc_atividades_soc, cidadao.raca, estado_civil.descricao as estado_civil, escolaridade.descricao as escolaridade, religiao.descricao as religiao from cidadao LEFT JOIN religiao on religiao.id = cidadao.religiao LEFT JOIN estado_civil on cidadao.estado_civil = estado_civil.id LEFT JOIN escolaridade on cidadao.escolaridade = escolaridade.id where cidadao.id = %s" % (28)

dadosPessoais = banco.consultarDict(codigoSQL)[0]

print(dadosPessoais)