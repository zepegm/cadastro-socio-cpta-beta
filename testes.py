import csv
from conexaoBD import Conexao

cred = {'HOST':'ec2-34-197-84-74.compute-1.amazonaws.com', 'PORT':5432, 'USER':'piendkrxzduecj', 'PASSWORD':'5af529088848fd2537e0c97f22469dc181a79b2a1cfcc98de6959275e13cab3d', 'DB':'do5a2tog3uf07'}
banco = Conexao(cred)

#print(banco.consultar("Select * from cidadao"))

# lendo csv
with open(r'C:\Users\giuseppe.manzella\Desktop\Dados Aleatorios Prefeitura.csv', newline='', encoding="utf8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar=';')
    for row in spamreader:
        if (row[1] != 'nome'):
            print(row[1])
            codigoSQL = "INSERT INTO cidadao(nome, nascimento, telefone, celular, email, endereco, rg, cpf, nis, sus, chefe_familia, cidade, estado, escolaridade, raca, profissao, renda, num_filhos, estado_civil, religiao, atividades_soc, desc_atividades_soc, tipo_imovel, area, correio, entrega) VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', %s, %s, %s, %s, '%s', '%s', %s, %s, '%s', %s, %s, %s, %s, %s, '%s', %s, '%s', %s, %s)" % (row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25], row[26])
            banco.manipular(codigoSQL)

