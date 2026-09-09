from BaseClient import BaseClient

baseclient = BaseClient()

response_board = baseclient.criar_board("Teste API trello")
board_id_teste = response_board.json()["id"]
lista_teste = baseclient.criar_lista("Teste API trello - lista", board_id_teste)
list_id_teste = lista_teste.json()["id"]

def test_criar_card():
    response = baseclient.criar_card("Teste API trello - card", list_id_teste)
    assert response.status_code == 200

def test_criar_card_nome_vazio():
    response = baseclient.criar_card("", list_id_teste)
    assert response.status_code == 200

def test_criar_card_1_caractere():
    response = baseclient.criar_card("a", list_id_teste)
    assert response.status_code == 200

def test_criar_card_2_caracteres():
    response = baseclient.criar_card("ab", list_id_teste)
    assert response.status_code == 200

def test_criar_card_caracteres_latinos():
    response = baseclient.criar_card("Card de Teste QA", list_id_teste)
    assert response.status_code == 200

def test_criar_card_caracteres_nao_latinos():
    response = baseclient.criar_card("看板テスト", list_id_teste)
    assert response.status_code == 200

def test_criar_card_com_emoji():
    response = baseclient.criar_card("Card de Teste 🚀", list_id_teste)
    assert response.status_code == 200

def test_criar_card_caracteres_especiais():
    response = baseclient.criar_card("Card !@#$%^&*()", list_id_teste)
    assert response.status_code == 200

def test_criar_card_com_numeros():
    response = baseclient.criar_card("Card123456", list_id_teste)
    assert response.status_code == 200