CREATE DATABASE IF NOT EXISTS dadosBancarios;
USE dadosBancarios;

CREATE TABLE IF NOT EXISTS banco (
    id_transacao INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(15),
    valor DECIMAL(10,2),
    saldo_total DECIMAL(10,2),
    data_hora DATETIME DEFAULT CURRENT_TIMESTAMP
);