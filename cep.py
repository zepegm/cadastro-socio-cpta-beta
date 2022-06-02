from pycep_correios import get_address_from_cep, WebService

def retornarCEP(cep):

    try:
        address = get_address_from_cep(cep, webservice=WebService.APICEP)
    except:
        address = {'bairro': '', 'cep': '12630-000', 'cidade': 'Cachoeira Paulista', 'logradouro': '', 'uf': 'SP', 'complemento': ''}

    return address