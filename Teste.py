import requests
from BaseClient import BaseClient

baseclient = BaseClient()

#Criando o Board
response_board = baseclient.criar_board("Teste API trello")
print(response_board.status_code)
print(response_board.json())

#Criando uma lista
response_list = baseclient.criar_lista("Teste API trello - lista", response_board.json()["id"])
print(response_list.status_code)
print(response_list.json())

#Criando um card
response_card = baseclient.criar_card("Teste API trello - card", response_list.json()["id"])
print(response_card.status_code)
print(response_card.json())