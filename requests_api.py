import httpx
import config
import json


def requestsApi(employeeID):
    # Concatena link da api com o ID do funcionário
    link_complete_api = config.LINK_API + employeeID

    # Faz a requisição GET para URL e obtém o retorno em json
    with httpx.Client() as client:
        response = client.get(link_complete_api)

        data = response.json()
        phone_number = data['phoneNumber']
        start_date = data['startDate']

        return phone_number, start_date
