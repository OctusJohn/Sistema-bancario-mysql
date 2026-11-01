Sistema Bancário CLI com Integração MySQL

Este projeto é uma evolução de um sistema bancário hipotético simples desenvolvido via linha de comando (CLI) em Python. A versão atual foi adaptada para persistir todas as movimentações financeiras em um banco de dados relacional MySQL.

Funcionalidades

- Consulta de saldo atualizado diretamente da base de dados.
- Depósito de valores com atualização imediata do saldo e registro do histórico de transações.
- Saque com verificação de saldo suficiente antes da confirmação da operação.
- Registro automatizado de data e hora para cada transação realizada.

Tecnologias Utilizadas

- Python 3
- MySQL
- PyMySQL (Driver de conexão entre Python e MySQL)

Estrutura do Banco de Dados

O projeto utiliza um banco de dados chamado dadosBancarios e uma tabela chamada banco.

