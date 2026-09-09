from BaseClient import BaseClient

baseclient = BaseClient()

response_board = baseclient.criar_board("Teste API trello")
board_id_teste = response_board.json()["id"]

def test_criar_lista():
    response_lista = baseclient.criar_lista("Teste API trello - lista", board_id_teste)
    assert response_lista.status_code == 200

def test_criar_lista_1_caractere():
    response = baseclient.criar_lista("a", board_id_teste)
    assert response.status_code == 200

def test_criar_lista_2_caracteres():
    response = baseclient.criar_lista("ab", board_id_teste)
    assert response.status_code == 200

def test_criar_lista_caracteres_latinos():
    response = baseclient.criar_lista("Lista de Teste QA", board_id_teste)
    assert response.status_code == 200

def test_criar_lista_caracteres_nao_latinos():
    response = baseclient.criar_lista("看板テスト", board_id_teste)
    assert response.status_code == 200

def test_criar_lista_com_emoji():
    response = baseclient.criar_lista("Lista de Teste 🚀", board_id_teste)
    assert response.status_code == 200

def test_criar_lista_caracteres_especiais():
    response = baseclient.criar_lista("Lista !@#$%^&*()", board_id_teste)
    assert response.status_code == 200

def test_criar_lista_com_numeros():
    response = baseclient.criar_lista("Lista123456", board_id_teste)
    assert response.status_code == 200
