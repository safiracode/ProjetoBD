DROP TABLE IF EXISTS consome CASCADE;
DROP TABLE IF EXISTS reserva_quarto CASCADE;
DROP TABLE IF EXISTS quarto CASCADE;
DROP TABLE IF EXISTS categoria_quarto CASCADE;
DROP TABLE IF EXISTS pagamento CASCADE;
DROP TABLE IF EXISTS empresa CASCADE;
DROP TABLE IF EXISTS hospede CASCADE;
DROP TABLE IF EXISTS titular_financeiro CASCADE;
DROP TABLE IF EXISTS reserva CASCADE;
DROP TABLE IF EXISTS idiomas_rec CASCADE;
DROP TABLE IF EXISTS recepcionista CASCADE;
DROP TABLE IF EXISTS auxiliar_servicos_gerais CASCADE;
DROP TABLE IF EXISTS camareiro CASCADE;
DROP TABLE IF EXISTS cozinheiro CASCADE;
DROP TABLE IF EXISTS pessoa_operacional CASCADE;
DROP TABLE IF EXISTS gerente CASCADE;
DROP TABLE IF EXISTS diretor CASCADE;
DROP TABLE IF EXISTS dependentes CASCADE;
DROP TABLE IF EXISTS funcionario CASCADE;
DROP TABLE IF EXISTS item CASCADE;
DROP TABLE IF EXISTS pessoa CASCADE;
DROP TABLE IF EXISTS endereco CASCADE;

CREATE TABLE endereco (
    id_endereco SERIAL PRIMARY KEY,
    tipo_logradouro VARCHAR(20),
    nome_logradouro VARCHAR(100),
    numero VARCHAR(20),
    bairro VARCHAR(50),
    cidade VARCHAR(50),
    cep VARCHAR(15)
);

CREATE TABLE pessoa (
    numero_documento VARCHAR(20) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    tipo_documento VARCHAR(20) NOT NULL,
    data_nascimento DATE,
    id_endereco INT,
    CONSTRAINT fk_pessoa_endereco FOREIGN KEY (id_endereco) REFERENCES endereco(id_endereco)
);

CREATE TABLE item (
    codigo VARCHAR(20) PRIMARY KEY,
    valor_unitario NUMERIC(10, 2) NOT NULL,
    descricao VARCHAR(255)
);

CREATE TABLE funcionario (
    matricula VARCHAR(20) PRIMARY KEY,
    numero_documento VARCHAR(20) NOT NULL UNIQUE,
    cargo VARCHAR(50),
    salario NUMERIC(10, 2),
    data_contratacao DATE,
    CONSTRAINT fk_funcionario_pessoa FOREIGN KEY (numero_documento) REFERENCES pessoa(numero_documento)
);

CREATE TABLE dependentes (
    numero_documento VARCHAR(20) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    tipo_documento VARCHAR(20),
    data_nascimento DATE,
    parentesco VARCHAR(30),
    f_matricula VARCHAR(20),
    CONSTRAINT fk_dependentes_funcionario FOREIGN KEY (f_matricula) REFERENCES funcionario(matricula)
);

CREATE TABLE diretor (
    matricula VARCHAR(20) PRIMARY KEY,
    percentual_participacao NUMERIC(5, 2),
    g_matricula VARCHAR(20),
    CONSTRAINT fk_diretor_funcionario FOREIGN KEY (matricula) REFERENCES funcionario(matricula)
);

CREATE TABLE gerente (
    matricula VARCHAR(20) PRIMARY KEY,
    certificacao_gestao VARCHAR(100),
    d_matricula VARCHAR(20),
    CONSTRAINT fk_gerente_funcionario FOREIGN KEY (matricula) REFERENCES funcionario(matricula)
);

CREATE TABLE pessoa_operacional (
    id_equipe VARCHAR(20) PRIMARY KEY,
    g_matricula VARCHAR(20),
    CONSTRAINT fk_operacional_gerente FOREIGN KEY (g_matricula) REFERENCES gerente(matricula)
);

CREATE TABLE cozinheiro (
    matricula VARCHAR(20) PRIMARY KEY,
    certificacao_gastronomica VARCHAR(100),
    id_equipe VARCHAR(20),
    CONSTRAINT fk_cozinheiro_funcionario FOREIGN KEY (matricula) REFERENCES funcionario(matricula),
    CONSTRAINT fk_cozinheiro_equipe FOREIGN KEY (id_equipe) REFERENCES pessoa_operacional(id_equipe)
);

CREATE TABLE camareiro (
    matricula VARCHAR(20) PRIMARY KEY,
    velocidade_troca_lencol VARCHAR(50),
    id_equipe VARCHAR(20),
    CONSTRAINT fk_camareiro_funcionario FOREIGN KEY (matricula) REFERENCES funcionario(matricula),
    CONSTRAINT fk_camareiro_equipe FOREIGN KEY (id_equipe) REFERENCES pessoa_operacional(id_equipe)
);

CREATE TABLE auxiliar_servicos_gerais (
    matricula VARCHAR(20) PRIMARY KEY,
    area_atuacao VARCHAR(100),
    id_equipe VARCHAR(20),
    CONSTRAINT fk_auxiliar_funcionario FOREIGN KEY (matricula) REFERENCES funcionario(matricula),
    CONSTRAINT fk_auxiliar_equipe FOREIGN KEY (id_equipe) REFERENCES pessoa_operacional(id_equipe)
);

CREATE TABLE recepcionista (
    matricula VARCHAR(20) PRIMARY KEY,
    turno VARCHAR(20),
    conhecimento_sistema VARCHAR(100),
    id_equipe VARCHAR(20),
    CONSTRAINT fk_recepcionista_funcionario FOREIGN KEY (matricula) REFERENCES funcionario(matricula),
    CONSTRAINT fk_recepcionista_equipe FOREIGN KEY (id_equipe) REFERENCES pessoa_operacional(id_equipe)
);

CREATE TABLE idiomas_rec (
    r_matricula VARCHAR(20),
    idioma VARCHAR(50),
    PRIMARY KEY (r_matricula, idioma),
    CONSTRAINT fk_idiomas_recepcionista FOREIGN KEY (r_matricula) REFERENCES recepcionista(matricula)
);

CREATE TABLE reserva (
    numero INT PRIMARY KEY,
    data_entrada DATE,
    data_saida DATE,
    quantidade_pessoas INT,
    status_atual VARCHAR(30),
    r_matricula VARCHAR(20),
    CONSTRAINT fk_reserva_recepcionista FOREIGN KEY (r_matricula) REFERENCES recepcionista(matricula)
);

CREATE TABLE titular_financeiro (
    id_titular VARCHAR(20) PRIMARY KEY,
    r_numero INT,
    CONSTRAINT fk_titular_reserva FOREIGN KEY (r_numero) REFERENCES reserva(numero)
);

CREATE TABLE hospede (
    numero_documento VARCHAR(20) PRIMARY KEY,
    id_titular VARCHAR(20),
    e_mail VARCHAR(100),
    CONSTRAINT fk_hospede_pessoa FOREIGN KEY (numero_documento) REFERENCES pessoa(numero_documento),
    CONSTRAINT fk_hospede_titular FOREIGN KEY (id_titular) REFERENCES titular_financeiro(id_titular)
);

CREATE TABLE empresa (
    id_titular VARCHAR(20) PRIMARY KEY,
    cnpj VARCHAR(20) NOT NULL UNIQUE,
    razao_social VARCHAR(150),
    telefone VARCHAR(20),
    CONSTRAINT fk_empresa_titular FOREIGN KEY (id_titular) REFERENCES titular_financeiro(id_titular)
);

CREATE TABLE pagamento (
    id_pagamento VARCHAR(20) PRIMARY KEY,
    tipo_pagamento VARCHAR(30),
    valor NUMERIC(10, 2),
    data DATE,
    id_titular VARCHAR(20),
    r_matricula VARCHAR(20),
    CONSTRAINT fk_pagamento_titular FOREIGN KEY (id_titular) REFERENCES titular_financeiro(id_titular),
    CONSTRAINT fk_pagamento_recepcionista FOREIGN KEY (r_matricula) REFERENCES recepcionista(matricula)
);

CREATE TABLE categoria_quarto (
    tipo VARCHAR(50) PRIMARY KEY,
    capacidade_maxima INT,
    valor_diaria NUMERIC(10, 2)
);

CREATE TABLE quarto (
    numero INT PRIMARY KEY,
    tipo VARCHAR(50),
    status VARCHAR(30),
    CONSTRAINT fk_quarto_categoria FOREIGN KEY (tipo) REFERENCES categoria_quarto(tipo)
);

CREATE TABLE reserva_quarto (
    r_numero INT,
    q_numero INT,
    PRIMARY KEY (r_numero, q_numero),
    CONSTRAINT fk_rq_reserva FOREIGN KEY (r_numero) REFERENCES reserva(numero),
    CONSTRAINT fk_rq_quarto FOREIGN KEY (q_numero) REFERENCES quarto(numero)
);

CREATE TABLE consome (
    r_numero INT,
    i_codigo VARCHAR(20),
    data_pedido DATE,
    hora_pedido TIME,
    quantidade INT,
    PRIMARY KEY (r_numero, i_codigo, data_pedido, hora_pedido),
    CONSTRAINT fk_consome_reserva FOREIGN KEY (r_numero) REFERENCES reserva(numero),
    CONSTRAINT fk_consome_item FOREIGN KEY (i_codigo) REFERENCES item(codigo)
);

ALTER TABLE diretor
ADD CONSTRAINT fk_diretor_gerente FOREIGN KEY (g_matricula) REFERENCES gerente(matricula);

ALTER TABLE gerente
ADD CONSTRAINT fk_gerente_diretor FOREIGN KEY (d_matricula) REFERENCES diretor(matricula);
