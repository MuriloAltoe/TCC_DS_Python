import connection

def inserir(nome,data,cpf,celular ):

    insert = [nome,data,cpf,celular]

    connection.cursor.execute("""
        INSERT INTO clientes (nome_cli, data_nasc, cpf_cnpj, celular)
        VALUES (?, ?, ?, ?)
        """, insert)
    
    connection.conn.commit()
    



