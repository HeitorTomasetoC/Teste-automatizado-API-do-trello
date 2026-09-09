# Testes de API - Trello
 
Teste para API do Trello (Boards, Lists, Cards) de duas formas: Postman e Python + Pytest.
 
A ideia de usar o Trello veio da vontade de misturar QA com gestão de processos - Kanban é isso, então testar a API de uma ferramenta de mercado real fez mais sentido.
 
## Arquivos
 
- `BaseClient.py` - classe com key/token centralizados e os métodos de criar board, lista e card
- `test_board.py`, `test_lista.py`, `test_card.py` - os testes em si
- `Trello_API_Tests.postman_collection.json` - a versão em Postman
## Testes
 
26 testes no total, cobrindo criação normal + valores limite (vazio, 1 e 2 caracteres, emoji, caracteres especiais, japonês, números).
 
## Rodando
 
Cola sua key e token do Trello no `BaseClient.py` (os campos estão vazios de propósito):
 
```python
key = ""
token = ""
```
 
Instala e roda:
 
```
pip install requests pytest
pytest -v
```
 
A versão Postman é só importar o `.json` e preencher `trello_key` / `trello_token` nas variáveis da coleção.
