import requests
from requests.auth import HTTPBasicAuth

response = requests.get('https://teste.agendamento.rnp.br/rnp-agendamento/api/reunioes/todas?dataInicial=11/12/2019&dataFinal=12/12/2019&sala=44', auth=HTTPBasicAuth('escritoriointeligenternp@gmail.com', 'c167f6e5'))
print(response)