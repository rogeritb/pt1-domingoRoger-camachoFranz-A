"""
Roger Domingo Meléndez - Franz Camacho Panozo
04/03/2024
ASIXc M03 UF2 pt1 R2: Disseny Modular, R2, data_source.py
Descripcio
És l’encarregada d’obtenir les dades. En aquesta versió les demanarà per teclat. Tot i que és probable, que en posteriors versions, demani les dades per fitxer.
Per tant, hauré d’implementar el mètode:
"""

import requests
import openai
def get_data_from_keyboard():
    datos = input("Introduce los datos perra: ")
    return datos

def get_data_from_server(URL):
    limit = 3
    YOUR_API_KEY = "rX2ddvNuDfo+Zm4dVePPKQ==QRXDMgsQsNHOkfIx"
    api_url = 'https://api.api-ninjas.com/v1/dadjokes?limit={}'.format(limit)
    response = requests.get(api_url, headers={'X-Api-Key': YOUR_API_KEY})
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)

def get_data_from_chatGTP(questio):
    openai.api_key = "sk-TyAnHRfKPI7oxjVt1WfvT3BlbkFJZPGlzLKLRaB2N6umpwJeme"

    ENGINE = "text-davinci-003"

    ANSWER_QUANTITY = 1

    MAX_TOKENS = 2048  # How many words?

def get_data_from_file(file_name):
    pass

