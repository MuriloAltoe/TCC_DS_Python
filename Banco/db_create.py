import connection

connection.cursor.execute(
    """
    CREATE TABLE cliente(
        id_cli INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome_cli TEXT NOT NULL
        data_nasc DATE NOT NULL
        cpf_cnpj INT NOT NULL
        celular INT NOT NULL
    )
    """
)

connection.conn.close()