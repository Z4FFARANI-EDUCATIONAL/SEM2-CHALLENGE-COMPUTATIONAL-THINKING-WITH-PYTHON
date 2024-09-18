import json

def carregar_blitz(arquivo):
    try:
        with open(arquivo, 'r') as file:
            dados = json.load(file)
            return dados.get('Blitz', 0)
    except FileNotFoundError:
        return 0

def salvar_blitz(arquivo, blitz):
    with open(arquivo, 'w') as file:
        json.dump({'Blitz': blitz}, file)