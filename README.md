#  Honda Concessionária - API REST

API desenvolvida com **Flask** e **PostgreSQL** para gerenciar os veículos de uma concessionária Honda. Oferece funcionalidades de **CRUD completas** com suporte à **paginação** e implementa boas práticas de arquitetura para APIs modernas.

---


##  Tecnologias Utilizadas

- Python 3.11+
- Flask
- Flask-SQLAlchemy
- PostgreSQL (Render Cloud)
- Gunicorn (Deploy)
- dotenv (Gerenciamento de ambientes)

---

##  Instalação Local

```bash
git clone https://gitlab.com/pedrohccoimbra123/honda_concessionaria.git
cd honda_concessionaria
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

###  Configuração do `.env`

Crie um arquivo `.env` com as seguintes variáveis:

```env
DB_USER=seu_usuario
PASSWORD=sua_senha
HOST=seu_host.render.com
DB_PORT=5432
DATABASE=nome_do_banco
env=local
```

---

##  Endpoints Disponíveis

### `GET /concessionaria/`

Retorna uma lista paginada de veículos.

#### Parâmetros (query string):

- `page`: int (padrão: 1)
- `per_page`: int (padrão: 10)

```bash
curl -X GET 'https://honda-concessionaria.onrender.com/concessionaria/?page=1&per_page=5'
```

---

###  `GET /concessionaria/{id}`

Busca um veículo pelo seu ID.

```bash
curl -X GET 'https://honda-concessionaria.onrender.com/concessionaria/1'
```

---

###  `POST /concessionaria/`

Cria um novo veículo no banco de dados.

#### Exemplo de JSON:

```json
{
  "modelo": "Civic",
  "marca": "Honda",
  "ano": 2023,
  "cor": "Preto",
  "preco": 120000.00
}
```

```bash
curl -X POST 'https://honda-concessionaria.onrender.com/concessionaria/'   -H 'Content-Type: application/json'   -d '{"modelo":"Civic","marca":"Honda","ano":2023,"cor":"Preto","preco":120000.0}'
```

---

###  `PUT /concessionaria/{id}`

Atualiza os dados de um veículo existente.

```bash
curl -X PUT 'https://honda-concessionaria.onrender.com/concessionaria/1'   -H 'Content-Type: application/json'   -d '{"modelo":"City","marca":"Honda","ano":2024,"cor":"Prata","preco":98000.0}'
```

---

###  `DELETE /concessionaria/{id}`

Remove um veículo do banco de dados pelo ID.

```bash
curl -X DELETE 'https://honda-concessionaria.onrender.com/concessionaria/1'
```

---

##  Códigos de Status Comuns

| Código | Descrição                |
|--------|--------------------------|
| 200    | Sucesso                  |
| 201    | Criado com sucesso       |
| 204    | Sem conteúdo             |
| 400    | Requisição inválida      |
| 404    | Recurso não encontrado   |
| 500    | Erro interno no servidor |

---


---

##  Autor

**Pedro Coimbra** – [GitLab](https://gitlab.com/pedrohccoimbra123) - Matricula: 22070215
**Carlos Egger** – [GitLab](https://gitlab.com/Carlos-Egger) - Matricula: 22070044
---

## 📚 Licença

Este projeto está licenciado sob a [Licença MIT](https://opensource.org/licenses/MIT).
