import requests

class BaseClient:

#Inserir sua key e token do Trello aqui
    key = ""
    token = ""

    def criar_board(self,board_name):
        response = requests.post("https://api.trello.com/1/boards/", params={
            "key": self.key,
            "token": self.token,
            "name": board_name
        })
        return response

    def criar_lista(self,list_name, board_id): 
        response = requests.post("https://api.trello.com/1/lists", params={
            "key": self.key,
            "token": self.token,
            "idBoard": board_id,
            "name": list_name,
        })
        return response

    def criar_card(self,card_name, list_id):
        response = requests.post("https://api.trello.com/1/cards", params={
            "key": self.key,
            "token": self.token,
            "idList": list_id,
            "name": card_name,
        })
        return response