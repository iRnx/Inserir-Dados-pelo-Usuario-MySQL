import mysql.connector
from mysql.connector import Error
# Inserir registros em um banco de dados MySQL
con = ''
cursor = ''
print('Rotina para cadastro de produtos no banco de dados')
print('Entre com os dados conforme solicitado')

while True:
    nomeProduto = str(input('Nome do Produto: '))
    precoProduto = float(input('Preço: '))
    quantProduto = int(input('Quantidade: '))

    # Inserir registros em um Banco de Dados MySQL #
    try:
        con = mysql.connector.connect(
            host='localhost',
            database='python',
            user='root',
            password='root')
        declaracao = f"""INSERT INTO produtos
        (nome, preco, estoque)
        VALUES
        ('{nomeProduto}', {precoProduto}, {quantProduto})
        """

        cursor = con.cursor()
        cursor.execute(declaracao)
        con.commit()
        print(f'{cursor.rowcount} Registros inseridos na tabela!')

    except Error as erro:
        print(f'Falha ao inserir dados no Banco de Dados python: {erro}')

    finally:
        if con.is_connected():
            cursor.close()
            con.close()
            print('Conexão ao MySQL finalizada com Sucesso!')

    resp = str(input('Gostaria de continuar? [S/N]')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Gostaria de continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break



