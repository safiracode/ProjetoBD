# Entradas de teste em ordem segura

Use a documentação automática em `http://127.0.0.1:8000/docs`.

## 1. Criar pessoa com endereço embutido

`POST /pessoas`

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

## 2. Criar funcionário recepcionista base

`POST /funcionarios`

```json
{
  "matricula": "R900",
  "numero_documento": "99999999901",
  "cargo": "Recepcionista",
  "salario": 3500.00,
  "data_contratacao": "2026-05-30"
}
```

## 3. Criar pessoa para gerente

`POST /pessoas`

```json
{
  "numero_documento": "99999999902",
  "nome": "Gerente Teste API",
  "tipo_documento": "CPF",
  "data_nascimento": "1985-03-20",
  "endereco": {
    "tipo_logradouro": "Av.",
    "nome_logradouro": "Avenida Teste API",
    "numero": "456",
    "bairro": "Boa Vista",
    "cidade": "Recife",
    "cep": "50000-000"
  }
}
```

## 4. Criar funcionário gerente

`POST /funcionarios`

```json
{
  "matricula": "G900",
  "numero_documento": "99999999902",
  "cargo": "Gerente",
  "salario": 9000.00,
  "data_contratacao": "2026-05-30"
}
```

## 5. Criar gerente

`POST /gerentes`

```json
{
  "matricula": "G900",
  "certificacao_gestao": "Gestão Hoteleira",
  "d_matricula": null
}
```

## 6. Criar equipe operacional

`POST /equipes-operacionais`

```json
{
  "id_equipe": "EQ900",
  "g_matricula": "G900"
}
```

## 7. Criar recepcionista

`POST /recepcionistas`

```json
{
  "matricula": "R900",
  "turno": "Diurno",
  "conhecimento_sistema": "Avançado",
  "id_equipe": "EQ900"
}
```

## 8. Criar idioma da recepcionista

`POST /idiomas-recepcionista`

```json
{
  "r_matricula": "R900",
  "idioma": "Inglês"
}
```

## 9. Criar categoria de quarto

`POST /categorias-quarto`

```json
{
  "tipo": "Teste API",
  "capacidade_maxima": 2,
  "valor_diaria": 199.90
}
```

## 10. Criar quarto

`POST /quartos`

```json
{
  "numero": 900,
  "tipo": "Teste API",
  "status": "Disponível"
}
```

## 11. Criar reserva já vinculando quarto

`POST /reservas`

```json
{
  "numero": 9001,
  "data_entrada": "2026-08-01",
  "data_saida": "2026-08-05",
  "quantidade_pessoas": 2,
  "status_atual": "Confirmada",
  "r_matricula": "R900",
  "quartos": [900]
}
```

## 12. Criar titular financeiro

`POST /titulares-financeiros`

```json
{
  "id_titular": "T900",
  "r_numero": 9001
}
```

## 13. Criar hóspede usando pessoa aninhada

`POST /hospedes`

```json
{
  "numero_documento": "99999999903",
  "id_titular": "T900",
  "e_mail": "hospede.teste@email.com",
  "pessoa": {
    "numero_documento": "99999999903",
    "nome": "Hospede Teste API",
    "tipo_documento": "CPF",
    "data_nascimento": "2001-09-30",
    "endereco": {
      "tipo_logradouro": "Rua",
      "nome_logradouro": "Rua do Hospede",
      "numero": "789",
      "bairro": "Madalena",
      "cidade": "Recife",
      "cep": "50720-000"
    }
  }
}
```

## 14. Criar pagamento

`POST /pagamentos`

```json
{
  "id_pagamento": "P900",
  "tipo_pagamento": "PIX",
  "valor": 799.60,
  "data": "2026-08-01",
  "id_titular": "T900",
  "r_matricula": "R900"
}
```

## 15. Criar item

`POST /itens`

```json
{
  "codigo": "IT900",
  "valor_unitario": 12.50,
  "descricao": "Água mineral teste"
}
```

## 16. Criar consumo

`POST /consumos`

```json
{
  "r_numero": 9001,
  "i_codigo": "IT900",
  "data_pedido": "2026-08-02",
  "hora_pedido": "10:30:00",
  "quantidade": 2
}
```

## 17. Testar consumo repetido em outro horário

`POST /consumos`

```json
{
  "r_numero": 9001,
  "i_codigo": "IT900",
  "data_pedido": "2026-08-02",
  "hora_pedido": "15:45:00",
  "quantidade": 1
}
```
