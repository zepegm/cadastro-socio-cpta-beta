from conexaoBD import Conexao

cred = {'HOST':'ec2-34-197-84-74.compute-1.amazonaws.com', 'PORT':5432, 'USER':'piendkrxzduecj', 'PASSWORD':'5af529088848fd2537e0c97f22469dc181a79b2a1cfcc98de6959275e13cab3d', 'DB':'do5a2tog3uf07'}

banco = Conexao(cred)

print(banco.consultar("Select * from cidadao"))

