# Normalização e ordem de execução

Este projeto segue a versão normalizada do banco:

1. `idade` foi removida de `pessoa`, pois pode ser calculada a partir de `data_nascimento`.
2. Os dados de endereço saíram de `pessoa` e foram para `endereco`.
3. `categoria_quarto` guarda `tipo`, `capacidade_maxima` e `valor_diaria`.
4. `quarto` guarda apenas `numero`, `tipo` e `status`.
5. O vínculo entre `reserva` e `quarto` fica em `reserva_quarto`.
6. `consome` usa chave composta completa: `r_numero`, `i_codigo`, `data_pedido`, `hora_pedido`.

## Ordem recomendada para popular o banco

1. endereco
2. pessoa
3. item
4. funcionario
5. dependentes
6. diretor e gerente
7. pessoa_operacional
8. cozinheiro, camareiro, auxiliar_servicos_gerais, recepcionista
9. idiomas_rec
10. reserva
11. titular_financeiro
12. hospede
13. empresa
14. pagamento
15. categoria_quarto
16. quarto
17. reserva_quarto
18. consome
