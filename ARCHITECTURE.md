# Estrutura do Projeto

Este documento explica, de forma geral, o papel de cada arquivo da API.

A aplicação foi organizada em arquivos separados para deixar a conexão com o banco, os modelos, os schemas, as operações CRUD e as rotas em lugares diferentes. Isso facilita a leitura e a manutenção do código.

## Visão geral

```txt
app/
├── database.py
├── models.py
├── schemas.py
├── crud.py
└── main.py
```

## `database.py`

Arquivo responsável pela conexão com o banco de dados.

Ele carrega a variável `DATABASE_URL` do arquivo `.env`, cria o `engine` do SQLAlchemy e define a sessão usada para acessar o PostgreSQL.

Também possui a função `get_db()`, que abre uma sessão com o banco para cada requisição e fecha essa sessão ao final.

Em resumo, esse arquivo cuida da parte de infraestrutura da conexão com o banco.

## `models.py`

Arquivo responsável por representar as tabelas do banco em classes Python.

Nele aparecem classes como:

- `Endereco`
- `Pessoa`
- `CategoriaQuarto`
- `Quarto`
- `Reserva`
- `ReservaQuarto`

Cada classe representa uma tabela do PostgreSQL. Os campos das classes representam as colunas das tabelas.

Nesta versão da API, o CRUD implementado é apenas para `Quarto`, mas o arquivo ainda mantém outras classes porque elas fazem parte da modelagem geral do banco.

Um ponto importante é que `Quarto` se relaciona com `CategoriaQuarto`, pois o tipo do quarto precisa existir na tabela de categorias.

## `schemas.py`

Arquivo responsável por definir os formatos de entrada e saída da API.

Ele usa Pydantic para validar os dados recebidos nas requisições e organizar os dados retornados nas respostas.

Nesta versão, existem schemas para:

- `Endereco`
- `CategoriaQuarto`
- `Quarto`

Apesar de existirem schemas de endereço e categoria, as rotas expostas atualmente são apenas de quartos.

Os principais schemas usados nas rotas são:

- `QuartoCreate`: usado para criar um quarto;
- `QuartoUpdate`: usado para atualizar um quarto;
- `QuartoResponse`: usado para definir como o quarto será retornado pela API.

## `crud.py`

Arquivo responsável pelas operações feitas diretamente no banco.

Nesta versão, ele possui funções para:

- listar quartos;
- buscar quarto por número;
- criar quarto;
- atualizar quarto;
- deletar quarto.

Antes de criar um quarto, o código verifica se a categoria informada existe em `categoria_quarto`. Isso evita cadastrar quartos com tipos inválidos.

Esse arquivo separa a lógica de acesso ao banco das rotas da API.

## `main.py`

Arquivo principal da aplicação FastAPI.

Ele cria a API e define as rotas disponíveis.

Nesta versão, as rotas implementadas são:

- `GET /`
- `GET /quartos`
- `GET /quartos/{numero}`
- `POST /quartos`
- `PUT /quartos/{numero}`
- `DELETE /quartos/{numero}`

As rotas recebem a requisição, usam os schemas para validar os dados e chamam as funções do `crud.py` para acessar o banco.

Também são tratados erros como quarto não encontrado e categoria de quarto inexistente.

## Análise da versão atual

A versão atual está coerente com a proposta de deixar apenas o CRUD de quartos.

O `main.py` expõe somente rotas relacionadas a quartos, e o `crud.py` também possui apenas funções dessa entidade. Isso deixa claro que a parte de reservas foi retirada da API atual.

No entanto, o `models.py` ainda mantém as classes `Reserva` e `ReservaQuarto`. Isso não impede o funcionamento, mas pode gerar dúvida para quem for ler o projeto. Existem duas opções:

1. manter essas classes porque elas representam tabelas reais do banco e podem ser usadas depois;
2. remover temporariamente essas classes se a ideia for deixar o projeto focado apenas em quartos.

Se outra pessoa vai implementar a parte de reservas, faz sentido manter essas classes ou deixar uma observação no README explicando que elas ainda não possuem rotas.

Também existem schemas de `Endereco` e `CategoriaQuarto`, mas ainda não há rotas para criar, listar ou atualizar essas entidades. Isso não é necessariamente erro, mas indica que esses schemas estão preparados para uma possível expansão futura.

## Fluxo da aplicação

De forma simples, o fluxo funciona assim:

```txt
main.py recebe a requisição
↓
schemas.py valida os dados
↓
crud.py executa a ação no banco
↓
models.py representa as tabelas usadas pelo SQLAlchemy
↓
database.py fornece a conexão com o PostgreSQL
```

## Resumo

- `database.py`: conecta a API ao banco;
- `models.py`: representa as tabelas;
- `schemas.py`: valida entrada e saída de dados;
- `crud.py`: executa as operações no banco;
- `main.py`: define as rotas da API.

A estrutura está adequada para um projeto simples com FastAPI e SQLAlchemy, principalmente por separar responsabilidades e deixar o CRUD de quartos isolado.
