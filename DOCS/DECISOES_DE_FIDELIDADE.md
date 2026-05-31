# Decisões de fidelidade ao projeto de Banco de Dados

Esta API foi organizada para seguir o minimundo, o modelo lógico e a normalização do projeto do hotel.

## 1. Pessoa e Endereço

No minimundo, o hotel mantém um cadastro unificado de pessoas com dados de endereço. Na normalização, esses dados foram separados em uma tabela `endereco`, e `pessoa` passou a guardar somente `id_endereco`.

Por isso, o fluxo principal da API é:

```txt
POST /pessoas
```

com o endereço embutido no corpo da requisição. A rota `POST /enderecos` não foi exposta como fluxo principal, porque endereço não é uma entidade operacional independente no minimundo. O CRUD interno de endereço existe porque a tabela existe no banco, mas a criação de endereço é feita junto com pessoa.

## 2. Pessoa, Funcionário e Hóspede

Uma pessoa pode ser hóspede e/ou funcionário. Por isso:

1. `POST /pessoas` cria a pessoa base.
2. `POST /funcionarios` especializa uma pessoa existente como funcionário.
3. `POST /hospedes` especializa uma pessoa existente como hóspede.

Para facilitar testes, `POST /hospedes` também aceita uma pessoa aninhada caso a pessoa ainda não exista.

## 3. Funcionários especializados

A documentação descreve funcionários especializados: diretor, gerente, recepcionista, camareiro, auxiliar de serviços gerais e cozinheiro. Na API, cada especialização tem uma rota própria e usa a matrícula como chave primária e FK para `funcionario`.

Fluxo correto:

```txt
POST /pessoas
POST /funcionarios
POST /recepcionistas ou /gerentes ou /diretores etc.
```

## 4. Diretor, Gerente e Equipe Operacional

O diretor lidera o gerente, e o gerente gerencia os demais funcionários operacionais. O script do projeto representa isso com:

- `diretor.g_matricula`
- `gerente.d_matricula`
- `pessoa_operacional.g_matricula`

Por haver referência cruzada entre diretor e gerente, o fluxo mais seguro é criar primeiro com um lado nulo e depois atualizar o vínculo.

## 5. Quarto e Categoria de Quarto

A normalização removeu `capacidade_maxima` e `valor_diaria` da tabela `quarto`, porque esses atributos dependem do tipo do quarto. Assim, a API exige que uma categoria exista antes de cadastrar um quarto.

Fluxo correto:

```txt
POST /categorias-quarto
POST /quartos
```

## 6. Reserva e Reserva_Quarto

A normalização removeu `r_numero` de `quarto` e criou `reserva_quarto`, preservando o histórico de quais quartos foram usados em quais reservas.

O fluxo principal permite criar a reserva já com uma lista de quartos:

```json
{
  "numero": 9001,
  "data_entrada": "2026-08-01",
  "data_saida": "2026-08-05",
  "quantidade_pessoas": 2,
  "status_atual": "Confirmada",
  "r_matricula": "R900",
  "quartos": [901]
}
```

Também existe `/reservas-quartos` para manutenção do vínculo.

## 7. Consome

A tabela `consome` tem chave primária composta por:

```txt
r_numero + i_codigo + data_pedido + hora_pedido
```

Isso permite que a mesma reserva consuma o mesmo item mais de uma vez em horários diferentes, como definido na normalização.

## 8. Pagamento e Titular Financeiro

O minimundo define que uma reserva é paga por um titular financeiro, que pode ser hóspede ou empresa. A API segue o script do banco:

1. Cria reserva.
2. Cria titular financeiro ligado à reserva.
3. Liga hóspede ou empresa ao titular.
4. Registra pagamento ligado ao titular e ao recepcionista.
