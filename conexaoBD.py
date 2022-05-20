import psycopg2
import psycopg2.extras

class Conexao(object):
    _db=None
    def __init__(self, app):
        self._db = psycopg2.connect(host=app['HOST'], database=app['DB'], user=app['USER'],  password=app['PASSWORD'])
    
    def manipular(self, sql):
        try:
            cur=self._db.cursor()
            cur.execute(sql)
            cur.close()
            self._db.commit()
            #print(sql)
        except:
            print(sql)
            return False
        return True

    def inserir(self, sql):
        try:
            cur=self._db.cursor()
            cur.execute(sql)
            id = cur.fetchone()
            cur.close()
            self._db.commit()
            #print(sql)
        except:
            print(sql)
            return 0
        return id


    def consultar(self, sql):
        rs=None
        try:
            cur=self._db.cursor()
            cur.execute(sql)
            rs=cur.fetchall()
            cur.close()
        except:
            return None
        return rs

    def consultarDict(self, sql):
        rs=None
        try:
            cur=self._db.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            cur.execute(sql)
            rs=cur.fetchall()
            cur.close()
        except:
            return None
        return [dict(row) for row in rs]

    def proximaPK(self, tabela, chave):
        sql='select max('+chave+') from '+tabela
        rs = self.consultar(sql)
        pk = rs[0][0]
        return pk+1
        
    def fechar(self):
        self._db.close()