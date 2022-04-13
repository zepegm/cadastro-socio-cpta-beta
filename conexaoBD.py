import sqlite3

def executarConsulta(banco, sql):
    conn = sqlite3.connect(banco)
    cursor = conn.cursor()
    #print(sql)
    cursor.execute(sql)

    return cursor.fetchone()

def inserirDadosBasico(banco, sql):
    conn = sqlite3.connect(banco)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()    