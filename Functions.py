import pymysql

def conectar():
    conexao = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="SUA_SENHA_AQUI",
        database="dadosBancarios"
    )
    print("Conectado ao sevirdor sql com sucesso.")
    return conexao

def mostrar_saldo(conexao):#Pega o valor saldo no banco de dados sql.
    cursor = conexao.cursor() #nomeia cursor para ficar mais fácil de ler

    sql = "SELECT saldo_total FROM banco ORDER BY id_transacao DESC LIMIT 1;" # comando de SQL para pegar id especifico
    cursor.execute(sql)#vai executar o programa

    resultado = cursor.fetchone()#atribui a resultado o valor de cursor
    cursor.close()#fechar cursor para não ter problemas

    if resultado is None or resultado[0] is None: #checa para ver se não é o primeiro funcionamento do código
        return 0
    return float(resultado[0])#

def depositar(conexao,deposito:float, saldo):
    if deposito <= 0:
        print("Valor de deposito devem ser maior que 0")
    else:
        saldo += deposito

        #modificação feita para aceitar sql, isso foi ensinado nas minhas pesquisas

        cursor = conexao.cursor() #define o cursor para ficar mais facil de ler

        sql = "INSERT INTO banco (tipo,valor,saldo_total) VALUES (%s, %s, %s)" #prepara o comando base de sql
        valores=('deposito', deposito,saldo)#define o tipo das variaveis

        cursor.execute(sql, valores)#realiza o comando em si
        conexao.commit()#salva as alteraçòes

        cursor.close()#remove o cursor atual para não acontecer erro no futuro

    return saldo

def sacar(conexao,saque, saldo=0.0):
    if saque <= 0:
        print ("Valor de saque devem ser maior que 0")
    elif saque > saldo:
        print("Valor insuficiente para saque")
    else:

        saldo -= saque

        cursor=conexao.cursor()
        sql=" INSERT INTO banco (tipo,valor,saldo_total) VALUES (%s, %s, %s)"
        valores=('saque', saque, saldo)

        cursor.execute(sql, valores)
        conexao.commit()

        cursor.close()

    return saldo

def main():
    conexao = conectar()
    saldo = mostrar_saldo(conexao)
    estaFuncionando = True

    print("=============================")
    print("Bem vindo a sua conta bancaria")
    print("Prosiga com a operação desejada")

    while estaFuncionando:
        print("=============================")
        print("Precione 1 para checar seu saldo")
        print("Precione 2 para realizar um deposito")
        print("Precione 3 para realizar um saque")
        print("Precione 4 para encerrar o programa")

        escolha = int(input("Sua escolha: "))

        if escolha == 1:
            print("=============================")
            print(f"Seu saldo é de R${saldo:.2f}")

        elif escolha == 2:
            print("=============================")
            deposito = float(input("Quanto que depositar? "))
            saldo = depositar(conexao,deposito, saldo,)

        elif escolha == 3:
            print("=============================")
            saque = float(input("Quanto gostaria de sacar?: "))
            saldo = sacar(conexao,saque, saldo,)

        elif escolha == 4:
            conexao.close()
            estaFuncionando = False

        else:
            print("=============================")
            print("Escolha invalida")

    print("=============================")
    print("Obrigado pela a preferencia")


if __name__ == "__main__":
    main()
