from BaseClient import BaseClient

baseclient = BaseClient()

def test_criar_board():
    response_board = baseclient.criar_board("Teste API trello")
    assert response_board.status_code == 200
    
def test_criar_board_nome_vazio():
    response = baseclient.criar_board("")
    assert response.status_code == 400

def test_criar_board_1_caractere():
    response = baseclient.criar_board("a")
    assert response.status_code == 200

def test_criar_board_2_caracteres():
    response = baseclient.criar_board("ab")
    assert response.status_code == 200

def test_criar_board_caracteres_latinos():
    response = baseclient.criar_board("Board de Teste QA")
    assert response.status_code == 200

def test_criar_board_caracteres_nao_latinos():
    response = baseclient.criar_board("看板テスト")
    assert response.status_code == 200

def test_criar_board_com_emoji():
    response = baseclient.criar_board("Board de Teste 🚀")
    assert response.status_code == 200

def test_criar_board_caracteres_especiais():
    response = baseclient.criar_board("Board !@#$%^&*()")
    assert response.status_code == 200

def test_criar_board_com_numeros():
    response = baseclient.criar_board("Board123456")
    assert response.status_code == 200