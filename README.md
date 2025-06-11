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
- SwaggerUI (Interface de documentação dos Endpoints)

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

### `SwaggerUI`

Endpoint do SwaggerUI para facilitar a exploração dos demais Endpoints da API
```
  https://honda-concessionaria.onrender.com/swagger

```


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

# Integração Contínua (CI) com GitHub Actions

Este projeto conta com um pipeline de CI configurado via GitHub Actions para garantir a qualidade do código e a estabilidade da aplicação.

## O que o pipeline realiza?

- **Linting**: Usa o `flake8` para analisar o código Python e garantir conformidade com padrões de estilo, evitando problemas comuns.
- **Testes automatizados**: Executa os testes com `pytest` para validar o comportamento da API.
- **Banco PostgreSQL local no CI**: Um container do PostgreSQL é iniciado no ambiente do GitHub Actions para rodar os testes de integração contra um banco real.
- **Variáveis de ambiente**: Configuradas para simular o ambiente local e permitir a conexão segura com o banco de dados no CI.

## Fluxo simplificado do workflow

1. Código é enviado (`push`/`PR`).
2. O GitHub Actions sobe um container PostgreSQL para testes.
3. O ambiente virtual é criado e as dependências instaladas.
4. O `flake8` verifica o estilo do código.
5. O `pytest` executa os testes, incluindo os que acessam o banco.
6. Relatório de sucesso/falha é gerado.

---

# Sobre o uso do JWT (JSON Web Tokens)

A API utiliza o JWT para autenticação e autorização de rotas protegidas. Usuários precisam realizar login para obter um token JWT que deve ser enviado no cabeçalho `Authorization` das requisições subsequentes.

- O token é válido por um tempo configurado (exemplo: 15 minutos).
- O token deve ser enviado no formato: `Authorization: Bearer <access_token>`.
- Rotas protegidas usam o decorator `@jwt_required()` para garantir o acesso autenticado.
- No backend, o token é validado automaticamente e o usuário autenticado pode ser identificado via `get_jwt_identity()`.

Isso garante uma camada segura de autenticação sem a necessidade de armazenar sessão no servidor.


---

##  Autor

**Carlos Egger** – [GitHub](https://github.com/Carlos-Egger) - Matricula: 22070044
---

## 📚 Licença

Este projeto está licenciado sob a [Licença MIT](https://opensource.org/licenses/MIT).

