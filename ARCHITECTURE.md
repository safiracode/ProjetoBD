# Estrutura do Projeto

Este documento explica, de forma geral, o papel de cada parte da API do Sistema Hoteleiro.

A aplicação foi organizada em módulos separados para deixar a conexão com o banco, os modelos, os schemas, as operações CRUD e as rotas em lugares diferentes. Isso facilita a leitura e a manutenção do código.

## Visão geral

```txt
app/
├── database.py
├── main.py
├── models/
│   ├── __init__.py
│   ├── endereco.py
│   ├── pessoa.py
│   ├── funcionario.py
│   ├── dependente.py
│   ├── diretor.py
│   ├── gerente.py
│   ├── pessoa_operacional.py
│   ├── cozinheiro.py
│   ├── camareiro.py
│   ├── auxiliar_servicos_gerais.py
│   ├── recepcionista.py
│   ├── idioma_recepcionista.py
│   ├── reserva.py
│   ├── titular_financeiro.py
│   ├── hospede.py
│   ├── empresa.py
│   ├── pagamento.py
│   ├── categoria_quarto.py
│   ├── quarto.py
│   ├── reserva_quarto.py
│   ├── item.py
│   └── consome.py
├── schemas/
│   ├── __init__.py
│   ├── base.py
│   └── (um arquivo por entidade)
├── crud/
│   ├── __init__.py
│   ├── base.py
│   └── (um arquivo por entidade)
└── routes/
    ├── __init__.py
    ├── helpers.py
    └── (um arquivo por entidade)
sql/
└── 01_create_normalized_schema.sql
DOCS/
├── DECISOES_DE_FIDELIDADE.md
├── ENTRADAS_DE_TESTE.md
└── NORMALIZACAO_E_ORDEM.md
```

## `database.py`

Arquivo responsável pela conexão com o banco de dados.

Ele carrega a variável `DATABASE_URL` do arquivo `.env`, cria o `engine` do SQLAlchemy e define a sessão usada para acessar o PostgreSQL.

Também possui a função `get_db()`, que abre uma sessão com o banco para cada requisição e fecha essa sessão ao final. A função `check_database_connection()` é utilizada pela rota `/health` para verificar a conectividade com o banco.

Para ambientes com Supabase, o módulo adiciona automaticamente `sslmode=require` se necessário.

## `models/`

Diretório que contém as representações das tabelas do banco em classes Python usando SQLAlchemy.

Cada arquivo corresponde a uma tabela do PostgreSQL. As classes definidas são:

- `Endereco` — dados de endereço separados por normalização
- `Pessoa` — cadastro unificado de pessoas (com propriedade calculada `idade`)
- `Funcionario` — especialização de pessoa com matrícula, cargo, salário
- `Dependente` — dependentes de funcionários
- `Diretor` — especialização de funcionário com percentual de participação
- `Gerente` — especialização de funcionário com certificação de gestão
- `PessoaOperacional` — equipes operacionais gerenciadas por gerentes
- `Cozinheiro` — especialização com certificação gastronômica
- `Camareiro` — especialização com velocidade de troca de lençóis
- `AuxiliarServicosGerais` — especialização com área de atuação
- `Recepcionista` — especialização com turno, conhecimento do sistema e idiomas
- `IdiomaRecepcionista` — idiomas fluentes dos recepcionistas (tabela `idiomas_rec`)
- `Reserva` — estadias com data de entrada/saída, quantidade de pessoas, status
- `TitularFinanceiro` — responsável financeiro da reserva
- `Hospede` — especialização de pessoa com e-mail
- `Empresa` — empresa parceira com CNPJ, razão social, telefone
- `Pagamento` — registros de pagamento com tipo, valor, data
- `CategoriaQuarto` — tipo, capacidade máxima e valor da diária
- `Quarto` — número, tipo e status do quarto
- `ReservaQuarto` — tabela associativa entre reservas e quartos
- `Item` — itens vendidos pelo hotel com código, descrição e valor
- `Consome` — consumo de itens por reserva com chave composta (reserva + item + data + hora)

Todos os modelos seguem fielmente o script SQL normalizado em `sql/01_create_normalized_schema.sql`.

## `schemas/`

Diretório que define os formatos de entrada e saída da API usando Pydantic.

Cada entidade possui schemas para:

- `*Create` — usado para criar registros
- `*Update` — usado para atualizar registros (campos opcionais)
- `*Response` — usado para definir como o registro será retornado pela API

Todos herdam de `ORMBase` (definido em `base.py`), que configura `from_attributes=True` para compatibilidade entre SQLAlchemy e Pydantic.

Schemas com lógica especial:

- `PessoaCreate` aceita endereço embutido ou `id_endereco`
- `HospedeCreate` aceita pessoa aninhada caso a pessoa ainda não exista
- `ReservaCreate` aceita lista de quartos para vínculo automático

## `crud/`

Diretório responsável pelas operações feitas diretamente no banco.

Cada arquivo contém funções para listar, buscar, criar, atualizar e deletar registros da entidade correspondente. O arquivo `base.py` fornece funções genéricas reutilizáveis (`apply_updates`, `create_instance`, `list_all`, `get_by_pk`, `update_by_pk`, `delete_by_pk`).

Validações de integridade implementadas nos CRUDs:

- Verificação de existência de FKs antes de criação (ex: categoria antes de quarto, pessoa antes de funcionário)
- Proteção contra deleção de registros com vínculos ativos (ex: pessoa vinculada a funcionário/hóspede, funcionário com especializações/dependentes, reserva com titular/consumo)
- Validação de regras de negócio (ex: data de saída posterior à entrada, quantidade de pessoas positiva)

## `routes/`

Diretório que define as rotas da API FastAPI.

Cada arquivo cria um `APIRouter` com as rotas CRUD de uma entidade. O arquivo `helpers.py` fornece funções utilitárias `not_found()` e `bad_request()` para padronizar respostas de erro.

### Rotas disponíveis

| Prefixo | Entidade | Métodos |
|---|---|---|
| `/pessoas` | Pessoa | GET, POST, PUT, DELETE |
| `/enderecos` | Endereço | GET, POST, PUT, DELETE |
| `/funcionarios` | Funcionário | GET, POST, PUT, DELETE |
| `/dependentes` | Dependente | GET, POST, PUT, DELETE |
| `/diretores` | Diretor | GET, POST, PUT, DELETE |
| `/gerentes` | Gerente | GET, POST, PUT, DELETE |
| `/equipes-operacionais` | Equipe Operacional | GET, POST, PUT, DELETE |
| `/cozinheiros` | Cozinheiro | GET, POST, PUT, DELETE |
| `/camareiros` | Camareiro | GET, POST, PUT, DELETE |
| `/auxiliares-servicos-gerais` | Auxiliar de Serviços Gerais | GET, POST, PUT, DELETE |
| `/recepcionistas` | Recepcionista | GET, POST, PUT, DELETE |
| `/idiomas-recepcionista` | Idioma de Recepcionista | GET, POST, DELETE |
| `/reservas` | Reserva | GET, POST, PUT, DELETE |
| `/titulares-financeiros` | Titular Financeiro | GET, POST, PUT, DELETE |
| `/hospedes` | Hóspede | GET, POST, PUT, DELETE |
| `/empresas` | Empresa | GET, POST, PUT, DELETE |
| `/pagamentos` | Pagamento | GET, POST, PUT, DELETE |
| `/categorias-quarto` | Categoria de Quarto | GET, POST, PUT, DELETE |
| `/quartos` | Quarto | GET, POST, PUT, DELETE |
| `/reservas-quartos` | Reserva-Quarto | GET, POST, DELETE |
| `/itens` | Item | GET, POST, PUT, DELETE |
| `/consumos` | Consumo | GET, POST, PUT, DELETE |

## `main.py`

Arquivo principal da aplicação FastAPI.

Ele cria a API com título, descrição e versão, e registra todos os routers das 22 entidades. Também define duas rotas internas:

- `GET /` — verifica se a API está funcionando
- `GET /health` — verifica a conexão com o banco de dados

## Fluxo da aplicação

De forma simples, o fluxo funciona assim:

```txt
main.py recebe a requisição
↓
schemas/ valida os dados de entrada
↓
crud/ executa a ação no banco
↓
models/ representa as tabelas usadas pelo SQLAlchemy
↓
database.py fornece a conexão com o PostgreSQL
```

## Resumo

- `database.py`: conecta a API ao banco
- `models/`: representa as tabelas (22 entidades)
- `schemas/`: valida entrada e saída de dados
- `crud/`: executa as operações no banco com validações de integridade
- `routes/`: define as rotas da API
- `main.py`: cria a aplicação e registra os routers

A estrutura está organizada para um projeto completo com FastAPI e SQLAlchemy, separando responsabilidades por entidade e mantendo fidelidade ao minimundo, modelo lógico e normalização do projeto de Banco de Dados.
