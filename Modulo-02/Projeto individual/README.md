# Trabalho de SQL - Sistema de Empresas Parceiras

Este é um trabalho de SQL que cria um banco de dados para um sistema de empresas parceiras. O banco de dados inclui tabelas para empresas parceiras, colaboradores, tecnologias e departamentos.

## Estrutura do Banco de Dados

### Tabela Empresa_Parceira

CREATE TABLE Empresa_Parceira(
    IdEmpre_Parce INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100),
    Endereco VARCHAR(100),
    CNPJ VARCHAR(14),
    Telefone VARCHAR(15),
    Email VARCHAR(100)
);
![Texto Alternativo](url_da_imagem)

### Tabela Colaborador 


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
![Texto Alternativo](url_da_imagem)

### Tabela Tecnologia


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
![Texto Alternativo](url_da_imagem)

### Tabela Departamento

CREATE TABLE Departamento(
    IdDepartamento INT AUTO_INCREMENT PRIMARY KEY,
    Setor VARCHAR(50)
);
![Texto Alternativo](url_da_imagem)

_________________________________________________________________________________________________________

### Utilização
Para utilizar este banco de dados, siga os passos abaixo:

1. Execute os comandos SQL fornecidos neste README para criar as tabelas e inserir os dados.
2. Execute as consultas SQL conforme necessário para acessar as informações armazenadas no banco de dados.

##Exemplos de Consulta

-- Selecionar todas as empresas parceiras
SELECT * FROM Empresa_Parceira;

-- Selecionar todos os colaboradores de um determinado departamento
SELECT * FROM Colaborador WHERE Departamento_Id = 1;

-- Selecionar todas as tecnologias utilizadas por uma empresa parceira específica
SELECT * FROM Tecnologia WHERE IdEmpre_Parce = 1;


