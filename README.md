 Honda Concessionária - API REST

API desenvolvida com Flask e PostgreSQL para gerenciar os veículos de uma concessionária Honda. Oferece funcionalidades de CRUD completas com suporte à paginação e implementa boas práticas de arquitetura para APIs.

📆 Status do Projeto

✅ Em desenvolvimento ativo - contribuidores são bem-vindos!

🔌 Tecnologias Utilizadas

Python 3.11+

Flask

Flask-SQLAlchemy

PostgreSQL (Render Cloud)

Gunicorn (Deploy)

dotenv (gerenciamento de ambientes)

🚀 Instalação Local

git clone https://gitlab.com/pedrohccoimbra123/honda_concessionaria.git
cd honda_concessionaria
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

🔢 Configuração do .env

Crie um arquivo .env com as seguintes variáveis:

DB_USER=seu_usuario
PASSWORD=sua_senha
HOST=seu_host.render.com
DB_PORT=5432
DATABASE=nome_do_banco
env=local

🔎 Endpoints Disponíveis

✅ GET /concessionaria/

Lista veículos com paginação.

Query Params:

page (int) - página atual (default: 1)

per_page (int) - itens por página (default: 10)

curl -X GET 'https://honda-concessionaria.onrender.com/concessionaria/?page=1&per_page=5'

✅ GET /concessionaria/{id}

Busca um veículo pelo ID.

curl -X GET 'https://honda-concessionaria.onrender.com/concessionaria/1'

➕ POST /concessionaria/

Cria um novo veículo.

{
  "modelo": "Civic",
  "marca": "Honda",
  "ano": 2023,
  "cor": "Preto",
  "preco": 120000.00
}

curl -X POST 'https://honda-concessionaria.onrender.com/concessionaria/' \
  -H 'Content-Type: application/json' \
  -d '{"modelo":"Civic","marca":"Honda","ano":2023,"cor":"Preto","preco":120000.0}'

✍️ PUT /concessionaria/{id}

Atualiza um veículo existente.

curl -X PUT 'https://honda-concessionaria.onrender.com/concessionaria/1' \
  -H 'Content-Type: application/json' \
  -d '{"modelo":"City","marca":"Honda","ano":2024,"cor":"Prata","preco":98000.0}'

❌ DELETE /concessionaria/{id}

Remove um veículo do banco de dados.

curl -X DELETE 'https://honda-concessionaria.onrender.com/concessionaria/1'

📈 Códigos de Status Comuns

Código

Descrição

200

Sucesso

201

Criado com sucesso

204

Sem conteúdo

400

Requisição inválida

404

Recurso não encontrado

500

Erro interno no servidor

🚧 Como Contribuir

Fork este repositório

Crie uma branch: git checkout -b minha-feature

Commit suas alterações: git commit -m 'feat: minha feature'

Push para sua branch: git push origin minha-feature

Crie um Pull Request

👤 Autor

Pedro Coimbra - GitLab

📚 Licença

Este projeto está licenciado sob a Licença MIT.