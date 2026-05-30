# API do Sistema Hoteleiro

API desenvolvida em **Python** com **FastAPI** e **SQLAlchemy** para conectar a aplicação ao banco de dados PostgreSQL do projeto de Banco de Dados.

Nesta versão, a API expõe operações CRUD para a entidade **Quarto**, utilizando a estrutura normalizada do banco. A tabela `quarto` se relaciona com `categoria_quarto`, garantindo que todo quarto cadastrado esteja associado a uma categoria existente.

---

## Tecnologias utilizadas

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- python-dotenv
- Uvicorn

---

## Estrutura do projeto

```txt
ProjetoBD/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── crud.py
│
├── .env
├── requirements.txt
└── README.md
```

---

## Propósito de cada arquivo

| Arquivo | Propósito |
|---|---|
| `app/main.py` | Arquivo principal da API. Define as rotas/endpoints disponíveis. |
| `app/database.py` | Configura a conexão com o PostgreSQL usando SQLAlchemy. |
| `app/models.py` | Mapeia as tabelas do banco de dados como classes Python. |
| `app/schemas.py` | Define os formatos de entrada e saída dos dados da API. |
| `app/crud.py` | Contém as funções responsáveis por consultar, criar, atualizar e deletar dados no banco. |
| `.env` | Guarda a URL de conexão com o banco de dados. |
| `requirements.txt` | Lista as dependências necessárias para executar o projeto. |

---

## Pré-requisitos

Antes de rodar o projeto, é necessário ter instalado:

- Python 3.10 ou superior
- PostgreSQL
- pip
- Ambiente virtual Python, recomendado

Também é necessário que o banco de dados já tenha sido criado e que os scripts SQL do projeto tenham sido executados no PostgreSQL.

A ordem recomendada é:

```txt
1. Criar o banco no PostgreSQL
2. Executar o script de criação das tabelas
3. Executar o script de normalização
4. Executar o script de povoamento
5. Configurar o arquivo .env
6. Rodar a API
```

---

## Configuração do banco de dados

Crie um arquivo `.env` na raiz do projeto com a variável `DATABASE_URL`.

Exemplo:

```env
DATABASE_URL=postgresql://postgres:sua_senha@localhost:5432/hotel_db
```

Substitua:

- `postgres` pelo seu usuário do PostgreSQL;
- `sua_senha` pela sua senha;
- `localhost` pelo host do banco;
- `5432` pela porta usada pelo PostgreSQL;
- `hotel_db` pelo nome do banco criado.

Exemplo com senha `123456`:

```env
DATABASE_URL=postgresql://postgres:123456@localhost:5432/hotel_db
```

---

## Criando e ativando o ambiente virtual

No PowerShell, dentro da pasta do projeto, crie o ambiente virtual:

```powershell
python -m venv .venv
```

Ative o ambiente virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

Quando o ambiente estiver ativo, o terminal deve mostrar algo parecido com:

```powershell
(.venv) PS C:\Users\Safira\Downloads\repositorios\ProjetoBD>
```

---

## Instalando as dependências

Com o ambiente virtual ativo, execute:

```powershell
python -m pip install -r requirements.txt
```

---

## Rodando a aplicação

Com o ambiente virtual ativo, execute:

```powershell
python -m uvicorn app.main:app --reload
```

A API ficará disponível em:

```txt
http://127.0.0.1:8000
```

A documentação automática do FastAPI ficará disponível em:

```txt
http://127.0.0.1:8000/docs
```

---

## Endpoints disponíveis

### Verificar se a API está funcionando

```http
GET /
```

Resposta esperada:

```json
{
  "message": "API do Sistema Hoteleiro funcionando."
}
```

---

### Listar quartos

```http
GET /quartos
```

Retorna todos os quartos cadastrados no banco.

---

### Buscar quarto por número

```http
GET /quartos/{numero}
```

Exemplo:

```http
GET /quartos/101
```

Caso o quarto exista, retorna seus dados. Caso não exista, retorna erro `404`.

---

### Criar quarto

```http
POST /quartos
```

Exemplo de corpo da requisição:

```json
{
  "numero": 401,
  "tipo": "Standard",
  "status": "Disponível"
}
```

Importante: o campo `tipo` precisa existir previamente na tabela `categoria_quarto`. Caso contrário, a API retorna erro `400` com a mensagem:

```json
{
  "detail": "Categoria de quarto inexistente."
}
```

---

### Atualizar quarto

```http
PUT /quartos/{numero}
```

Exemplo:

```http
PUT /quartos/401
```

Corpo da requisição:

```json
{
  "status": "Manutenção"
}
```

Também é possível atualizar o tipo:

```json
{
  "tipo": "Luxo"
}
```

---

### Deletar quarto

```http
DELETE /quartos/{numero}
```

Exemplo:

```http
DELETE /quartos/401
```

Resposta esperada:

```json
{
  "message": "Quarto removido com sucesso."
}
```

---

## Fluxo da aplicação

O fluxo básico da API é:

```txt
Cliente faz requisição
        ↓
main.py recebe a requisição
        ↓
schemas.py valida os dados
        ↓
crud.py executa a operação no banco
        ↓
models.py representa as tabelas usadas
        ↓
database.py fornece a sessão de conexão
        ↓
API retorna uma resposta JSON
```

---

## Observações importantes

- O projeto espera que as tabelas já existam no PostgreSQL.
- O SQLAlchemy está sendo usado para mapear as tabelas existentes, não para criar automaticamente todo o banco.
- As tabelas `Endereco`, `Pessoa`, `CategoriaQuarto`, `Reserva` e `ReservaQuarto` aparecem em `models.py` porque representam partes relevantes da estrutura normalizada do banco.

---

## Comando principal para execução

```powershell
python -m uvicorn app.main:app --reload
```
