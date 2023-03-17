import requests


def search_zip_code(zip_code):
    """
    Search a zip code for brazilian streets.
    """
    try:
        response = requests.get(f'https://viacep.com.br/ws/{zip_code}/json/')
        data = response.json()
        if 'erro' not in data:
            return {
                'zip_code': data['cep'],
                'state': data['uf'],
                'city': data['localidade']
            }
        else:
            return {'error': 'CEP inválido ou inexistente.'}
    except ValueError:
        return {'error': 'CEP inválido ou inexistente.'}

