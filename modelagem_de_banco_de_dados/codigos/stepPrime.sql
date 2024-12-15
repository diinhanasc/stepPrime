CREATE DATABASE StepPrime;
USE StepPrime;

-- Criando a tabela Pessoas
CREATE TABLE Pessoas (
    idPessoas INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(150) NOT NULL,
    email VARCHAR(200) UNIQUE,
    telefone INT(9) UNIQUE
);

-- Criando a tabela Clientes
CREATE TABLE Clientes (
    idCliente INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    idPessoa INT NOT NULL,
    FOREIGN KEY (idPessoa) REFERENCES Pessoas(idPessoas)
);

-- Criando a tabela Funcionarios
CREATE TABLE Funcionarios (
    idFuncionario INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    cargo VARCHAR(150) NOT NULL,
    salario DECIMAL(10,2) NOT NULL,
    idPessoa INT NOT NULL,
    FOREIGN KEY (idPessoa) REFERENCES Pessoas(idPessoas)
);

-- Criando a tabela Calcados
CREATE TABLE Calcados (
    idCalcado INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    modelo VARCHAR(150) NOT NULL,
    tamanho VARCHAR(150) NOT NULL,
    marca VARCHAR(150) NOT NULL,
    cor VARCHAR(150) NOT NULL
);

-- Criando a tabela PedidoCompras
CREATE TABLE PedidoCompras (
    idPedidoCompra INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    idCalcado INT NOT NULL,
    idCliente INT NOT NULL,
    quantidade INT NOT NULL,
    FOREIGN KEY (idCalcado) REFERENCES Calcados(idCalcado),
    FOREIGN KEY (idCliente) REFERENCES Clientes(idCliente)
);

-- Criando a tabela Compras
CREATE TABLE Compras (
    idCompra INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    dataCompra DATE NOT NULL,
    idPedidoCompra INT NOT NULL,
    FOREIGN KEY (idPedidoCompra) REFERENCES PedidoCompras(idPedidoCompra)
);

-- Inserindo dados na tabela Pessoas
INSERT INTO Pessoas (nome, email, telefone) VALUES
('João Silva', 'joao.silva@email.com', 123456789),
('Maria Oliveira', 'maria.oliveira@email.com', 987654321),
('Carlos Souza', 'carlos.souza@email.com', 456789123),
('Ana Lima', 'ana.lima@email.com', 789123456);

-- Inserindo dados na tabela Clientes
INSERT INTO Clientes (idPessoa) VALUES
(1),
(2);

-- Inserindo dados na tabela Funcionarios
INSERT INTO Funcionarios (cargo, salario, idPessoa) VALUES
('Gerente', 5000.00, 3),
('Vendedor', 2500.00, 4);

-- Inserindo dados na tabela Calcados
INSERT INTO Calcados (modelo, tamanho, marca, cor) VALUES
('Esportivo', '42', 'Nike', 'Preto'),
('Casual', '38', 'Adidas', 'Branco');

-- Inserindo dados na tabela PedidoCompras
INSERT INTO PedidoCompras (idCalcado, idCliente, quantidade) VALUES
(1, 1, 2),
(2, 2, 1);

-- Inserindo dados na tabela Compras
INSERT INTO Compras (dataCompra, idPedidoCompra) VALUES
('2024-12-01', 1),
('2024-12-02', 2);

-- Consultando os dados de cada tabela
SELECT * FROM Pessoas;
SELECT * FROM Clientes;
SELECT * FROM Funcionarios;
SELECT * FROM Calcados;
SELECT * FROM PedidoCompras;
SELECT * FROM Compras;
