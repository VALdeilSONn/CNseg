DROP DATABASE IF EXISTS DbEmpresasParceiras;
CREATE DATABASE DbEmpresasParceiras;
USE DbEmpresasParceiras;
-- -----------------------------------------------------

CREATE TABLE Empresa_Parceira(
    IdEmpre_Parce INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100),
    Endereco VARCHAR(100),
    CNPJ VARCHAR(14), -- Alterado para VARCHAR
    Telefone VARCHAR(15), -- Alterado para VARCHAR
    Email VARCHAR(100)
);

INSERT INTO Empresa_Parceira (Nome, Endereco, CNPJ, Telefone, Email)
VALUES 
    ('Pizzaria Patios', 'Rua da Cara duara A, 123', '12345678900010', '1112345678', 'pizza.patio@test.com'),
    ('AvaLancher', 'Avenida da Barroco, 456', '98765432100010', '2298765432', 'ava_lanche@test.com');

select * from Empresa_parceira;
-- -----------------------------------------------------
drop table if exists Colaborador;

CREATE TABLE Colaborador(
    IdColaborador INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100),
    DataContrato DATE,
    Cadastro VARCHAR(100),
    Cargo VARCHAR(45),
    Departamento_Id INT,
    FOREIGN KEY (Departamento_Id) REFERENCES Departamento(IdDepartamento),
    IdEmpre_Parce INT,
    FOREIGN KEY (IdEmpre_Parce) REFERENCES Empresa_Parceira(IdEmpre_Parce),
    Detalhes VARCHAR(255)
);

INSERT INTO Colaborador(Nome, DataContrato, Cadastro, Cargo, Departamento_Id) VALUES
('valdeilson souza', '2013-05-01', '1a2b3c', 'Gaeçon', 1), -- ID do departamento
('Dorema Pires', '2012-03-19', '4d5e6f', 'Caixa', 1), -- ID do departamento
('Pedro Bix', '2006-12-21', '2b5e1a', 'Entregador', 2), -- ID do departamento
('Maria das Dores', '2019-12-20', '6f8i3c', 'Limpesa', 3); -- ID do departamento

select * from Colaborador;
-- -----------------------------------------------------
drop TABLE IF exists TECNOLOGIA;

create table Tecnologia(
IdTecnologia int auto_increment primary key,
Nome varchar(100),
Area varchar(60),
Departamento_Id INT,
    FOREIGN KEY (Departamento_Id) REFERENCES Departamento(IdDepartamento),
IdEmpre_Parce INT,
    FOREIGN KEY (IdEmpre_Parce) REFERENCES Empresa_Parceira(IdEmpre_Parce),
    Detalhes VARCHAR(255),
    IdColaborador INT,
     FOREIGN KEY (IdColaborador) REFERENCES Colaborador(IdColaborador)
);

INSERT INTO Tecnologia (Nome, Area, Departamento_Id, IdEmpre_Parce, Detalhes, IdColaborador) VALUES
('Tablete', 'Salão', 1, 1, 'atendimento direto', 1),
('Desktop', 'Entrada', 1, 1, 'Recebimento de pagamento e reservas', 2),
('Moto', 'MotoBoy', 2, 1, 'Entrega a domicilio', 3),
('Moto', 'MotoBoy', 2, 2, 'Entrega a domicilio', 3),
('Aspirador', 'Salão, Play', 3, 2, 'Atuar na limpesa do local', 4),
('Aspirador', 'Salão, Play', 3, 1, 'Atuar na limpesa do local', 4);


select * from Tecnologia;
-- -----------------------------------------------------
drop table if exists Departamento;

create table Departamento(
IdDepartamento int auto_increment primary key,
Setor varchar(50)
);

insert into Departamento(setor) values
('Atendimento'),
('Logistica'),
('ASG');

select * from Departamento;