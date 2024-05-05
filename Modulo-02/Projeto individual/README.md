# Trabalho de SQL - Sistema de Empresas Parceiras

Este é um trabalho de SQL que cria um banco de dados para um sistema de empresas parceiras. O banco de dados inclui tabelas para empresas parceiras, colaboradores, tecnologias e departamentos.

# Modelo de Banco de Dados para Empresas Parceiras

Este é um modelo de banco de dados para gerenciamento de empresas parceiras, colaboradores, tecnologias utilizadas e departamentos. Abaixo estão as respostas para algumas perguntas frequentes sobre o modelo.

## Entidades Necessárias

1. **Empresa_Parceira**: Armazena informações sobre as empresas parceiras.
2. **Colaborador**: Registra os colaboradores das empresas parceiras.
3. **Tecnologia**: Descreve as tecnologias utilizadas pelas empresas e colaboradores.
4. **Departamento**: Define os departamentos onde os colaboradores estão alocados.

## Principais Campos e Tipos de Dados

1. **Empresa_Parceira**:
   - IdEmpre_Parce (INT, PK)
   - Nome (VARCHAR(100))
   - Endereco (VARCHAR(100))
   - CNPJ (VARCHAR(14))
   - Telefone (VARCHAR(15))
   - Email (VARCHAR(100))

2. **Colaborador**:
   - IdColaborador (INT, PK)
   - Nome (VARCHAR(100))
   - DataContrato (DATE)
   - Cadastro (VARCHAR(100))
   - Cargo (VARCHAR(45))
   - Departamento_Id (INT, FK referenciando Departamento)
   - IdEmpre_Parce (INT, FK referenciando Empresa_Parceira)
   - Detalhes (VARCHAR(255))

3. **Tecnologia**:
   - IdTecnologia (INT, PK)
   - Nome (VARCHAR(100))
   - Area (VARCHAR(60))
   - Departamento_Id (INT, FK referenciando Departamento)
   - IdEmpre_Parce (INT, FK referenciando Empresa_Parceira)
   - Detalhes (VARCHAR(255))
   - IdColaborador (INT, FK referenciando Colaborador)

4. **Departamento**:
   - IdDepartamento (INT, PK)
   - Setor (VARCHAR(50))

## Relacionamentos entre as Entidades

- **Colaborador** possui uma relação de muitos para um com **Departamento** (um departamento pode ter muitos colaboradores) e uma relação de muitos para um com **Empresa_Parceira** (um colaborador pertence a uma empresa parceira).
- **Tecnologia** tem uma relação de muitos para um com **Departamento** (uma tecnologia é utilizada em um departamento) e uma relação de muitos para um com **Empresa_Parceira** (uma tecnologia é utilizada por uma empresa parceira).
- Os campos `Departamento_Id`, `IdEmpre_Parce`, e `IdColaborador` nas tabelas **Colaborador** e **Tecnologia** são chaves estrangeiras que referenciam as respectivas tabelas de **Departamento**, **Empresa_Parceira** e **Colaborador**.

## Exemplos de Registros

### Empresa_Parceira
```
| IdEmpre_Parce | Nome             | Endereco                  | CNPJ           | Telefone    | Email               |
|---------------|------------------|---------------------------|----------------|-------------|---------------------|
| 1             | Pizzaria Patios  | Rua da Cara duara A, 123  | 12345678900010 | 1112345678  | pizza.patio@test.com |
| 2             | AvaLancher       | Avenida da Barroco, 456   | 98765432100010 | 2298765432  | ava_lanche@test.com |
```

### Colaborador
```
| IdColaborador | Nome             | DataContrato | Cadastro | Cargo       | Departamento_Id | IdEmpre_Parce | Detalhes    |
|---------------|------------------|--------------|----------|-------------|-----------------|---------------|-------------|
| 1             | valdeilson souza | 2013-05-01   | 1a2b3c   | Garçon      | 1               | 1             | atendimento direto |
| 2             | Dorema Pires     | 2012-03-19   | 4d5e6f   | Caixa       | 1               | 1             | Recebimento de pagamento e reservas |
| 3             | Pedro Bix        | 2006-12-21   | 2b5e1a   | Entregador  | 2               | 1             | Entrega a domicilio |
| 4             | Maria das Dores  | 2019-12-20   | 6f8i3c   | Limpeza     | 3               | 2             | Atuar na limpeza do local |
```

### Tecnologia
```
| IdTecnologia | Nome      | Area        | Departamento_Id | IdEmpre_Parce | Detalhes                | IdColaborador |
|--------------|-----------|-------------|-----------------|---------------|-------------------------|---------------|
| 1            | Tablete   | Salão       | 1               | 1             | Atendimento direto      | 1             |
| 2            | Desktop   | Entrada     | 1               | 1             | Recebimento de pagamento e reservas | 2 |
| 3            | Moto      | MotoBoy     | 2               | 1             | Entrega a domicilio     | 3             |
| 4            | Moto      | MotoBoy     | 2               | 2             | Entrega a domicilio     | 3             |
| 5            | Aspirador | Salão, Play | 3               | 2             | Atuar na limpeza do local | 4             |
| 6            | Aspirador | Salão, Play | 3               | 1             | Atuar na limpeza do local | 4             |
```



## Estrutura do Banco de Dados

### Tabela Empresa_Parceira
```
CREATE TABLE Empresa_Parceira(
    IdEmpre_Parce INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100),
    Endereco VARCHAR(100),
    CNPJ VARCHAR(14),
    Telefone VARCHAR(15),
    Email VARCHAR(100)
);
```
![Texto Alternativo](https://github.com/VALdeilSONn/CNseg/blob/main/Modulo-02/Projeto%20individual/img/CriandoTabela.jpg)

### Tabela Colaborador 

```
CREATE TABLE Colaborador(
    IdColaborador INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100),
    DataContrato DATE,
    Cadastro VARCHAR(100),
    Cargo VARCHAR(45),
    Departamento_Id INT,
    IdEmpre_Parce INT,
    Detalhes VARCHAR(255),
    FOREIGN KEY (Departamento_Id) REFERENCES Departamento(IdDepartamento),
    FOREIGN KEY (IdEmpre_Parce) REFERENCES Empresa_Parceira(IdEmpre_Parce)
);
```

![Texto Alternativo](https://github.com/VALdeilSONn/CNseg/blob/main/Modulo-02/Projeto%20individual/img/CriandoColaborador.jpg)

### Tabela Tecnologia

```
CREATE TABLE Tecnologia(
    IdTecnologia INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100),
    Area VARCHAR(60),
    Departamento_Id INT,
    IdEmpre_Parce INT,
    Detalhes VARCHAR(255),
    IdColaborador INT,
    FOREIGN KEY (Departamento_Id) REFERENCES Departamento(IdDepartamento),
    FOREIGN KEY (IdEmpre_Parce) REFERENCES Empresa_Parceira(IdEmpre_Parce),
    FOREIGN KEY (IdColaborador) REFERENCES Colaborador(IdColaborador)
);
```

![Texto Alternativo](https://github.com/VALdeilSONn/CNseg/blob/main/Modulo-02/Projeto%20individual/img/CriandoTecnologia.jpg)

### Tabela Departamento

```
CREATE TABLE Departamento(
    IdDepartamento INT AUTO_INCREMENT PRIMARY KEY,
    Setor VARCHAR(50)
);
```

![Texto Alternativo](https://github.com/VALdeilSONn/CNseg/blob/main/Modulo-02/Projeto%20individual/img/CriandoDepartamento.jpg)

_________________________________________________________________________________________________________

### Utilização
Para utilizar este banco de dados, siga os passos abaixo:

1. Execute os comandos SQL fornecidos neste README para criar as tabelas e inserir os dados.
2. Execute as consultas SQL conforme necessário para acessar as informações armazenadas no banco de dados.

###Exemplos de Consulta

```
-- Selecionar todas as empresas parceiras
SELECT * FROM Empresa_Parceira;

-- Selecionar todos os colaboradores de um determinado departamento
SELECT * FROM Colaborador WHERE Departamento_Id = 1;

-- Selecionar todas as tecnologias utilizadas por uma empresa parceira específica
SELECT * FROM Tecnologia WHERE IdEmpre_Parce = 1;
```

