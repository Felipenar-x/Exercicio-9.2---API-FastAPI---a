# Exercício 9.2 - API RESTful com FastAPI


## 🚀 Como executar a API

1. Certifique-se de ter o Python instalado.
2. Instale as dependências necessárias:
   ```bash
   pip install fastapi uvicorn
   ```
3. Navegue até a pasta do projeto e execute o servidor:

   ```bash
   python -m uvicorn main:app --reload
   ```
A API estará disponível em: http://127.0.0.1:8000

📑 Endpoints da API
```bash
GET / : Mensagem de boas-vindas.

GET /items : Lista todos os itens.

GET /items/{id} : Busca um item específico por ID.

POST /items : Cria um novo item (Requer Body JSON).

PUT /items/{id} : Atualiza um item existente.

DELETE /items/{id} : Remove um item.
```
