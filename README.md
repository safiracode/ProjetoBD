# API do Sistema Hoteleiro

API em FastAPI + SQLAlchemy para conectar o projeto de Banco de Dados do hotel ao PostgreSQL/Supabase.

A estrutura foi reorganizada para seguir fielmente o minimundo, o modelo lógico e a normalização do projeto. Todas as 22 entidades do modelo lógico possuem modelos, schemas, CRUDs e rotas.

## Estrutura

```txt
app/
├── database.py
├── main.py
├── models/
├── schemas/
├── crud/
└── routes/
sql/
└── 01_create_normalized_schema.sql
DOCS/
├── DECISOES_DE_FIDELIDADE.md
├── ENTRADAS_DE_TESTE.md
└── NORMALIZACAO_E_ORDEM.md
```

Para detalhes sobre cada parte, veja `ARCHITECTURE.md`.

## Como configurar

Crie um arquivo `.env` na raiz do projeto:

```env
DATABASE_URL=postgresql://usuario:senha@host:porta/postgres?sslmode=require
```

No Supabase, use a URL do pooler com `sslmode=require`.

## Como instalar

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Como rodar

```powershell
python -m uvicorn app.main:app --reload
```

## Testes rápidos

```txt
GET http://127.0.0.1:8000/
GET http://127.0.0.1:8000/health
GET http://127.0.0.1:8000/docs
```

A documentação interativa em `/docs` (Swagger UI) lista todas as rotas disponíveis, organizadas por entidade.

## Rotas disponíveis

A API expõe CRUD completo para todas as entidades do sistema:

| Prefixo | Entidade |
|---|---|
| `/pessoas` | Pessoa |
| `/enderecos` | Endereço |
| `/funcionarios` | Funcionário |
| `/dependentes` | Dependente |
| `/diretores` | Diretor |
| `/gerentes` | Gerente |
| `/equipes-operacionais` | Equipe Operacional |
| `/cozinheiros` | Cozinheiro |
| `/camareiros` | Camareiro |
| `/auxiliares-servicos-gerais` | Auxiliar de Serviços Gerais |
| `/recepcionistas` | Recepcionista |
| `/idiomas-recepcionista` | Idioma de Recepcionista |
| `/reservas` | Reserva |
| `/titulares-financeiros` | Titular Financeiro |
| `/hospedes` | Hóspede |
| `/empresas` | Empresa |
| `/pagamentos` | Pagamento |
| `/categorias-quarto` | Categoria de Quarto |
| `/quartos` | Quarto |
| `/reservas-quartos` | Reserva-Quarto |
| `/itens` | Item |
| `/consumos` | Consumo |

## Observação importante sobre Endereço

O fluxo principal não expõe `POST /enderecos` como fluxo de entrada, porque endereço aparece no minimundo como dado de Pessoa. A tabela `endereco` existe por causa da normalização, mas a criação principal acontece em `POST /pessoas` com o endereço embutido.

Exemplo:

```json
{
  "numero_documento": "99999999901",
  "nome": "Pessoa Teste API",
  "tipo_documento": "CPF",
  "data_nascimento": "2000-01-10",
  "endereco": {
    "tipo_logradouro": "Rua",
    "nome_logradouro": "Rua Teste API",
    "numero": "123",
    "bairro": "Varzea",
    "cidade": "Recife",
    "cep": "50740-000"
  }
}
```

## Documentação adicional

- `DOCS/DECISOES_DE_FIDELIDADE.md` — decisões de modelagem e fidelidade ao minimundo
- `DOCS/ENTRADAS_DE_TESTE.md` — fluxo completo de testes com exemplos de JSON
- `DOCS/NORMALIZACAO_E_ORDEM.md` — normalização aplicada e ordem de povoamento
- `ARCHITECTURE.md` — detalhes técnicos da arquitetura da API
