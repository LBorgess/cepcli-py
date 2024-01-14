import requests

BASE_URL = 'https://viacep.com.br/ws/'
TYPE = '/json/'

def get_cep_api(cep):    
    URL = f'{BASE_URL}{cep}{TYPE}'
    request = requests.get(URL)
    request = request.json()

    if 'erro' in request:
        print('\nCEP informado é inválido ou inexistente.\n')        
    else:
        return request
        
def get_cep(cep):
    data = get_cep_api(cep) 

    if not data:
        return
    else:
        print()
        print(f'Rua....: {data["logradouro"]}')
        print(f'Bairro.: {data["bairro"]}')
        print(f'Cidade.: {data["localidade"]}')
        print(f'Estado.: {data["uf"]}\n')

