from config import database
import sqlite3

class BancodeDados():
    def conectarBanco(self):
        caminhoBanco = database["caminhoBanco"]
        try: 
            self.banco = sqlite3.connect(caminhoBanco)
            self.cursor = self.banco.cursor()
            return self.banco,self.cursor
        except:
            return "Erro ao conectar no banco."

    def obterDadosComFiltro(self,cursor,tabela,tag_id):
        querySelector = f"SELECT * FROM {tabela} WHERE tag_id='{tag_id}'"
        try:
            cursor.execute(querySelector)
            return cursor.fetchall()
        except:
            return "Falha na execução da query obterDadoscomFiltro."

    def obterDados(self,cursor,tabela):
        querySelector = f"SELECT * FROM {tabela}"
        try:
            cursor.execute(querySelector)
            return cursor.fetchall()
        except:
            return "Falha na execução da query obterDados."

    def inserirDados(self,banco,cursor,tabela,tag_id):
        querySelector = f"INSERT INTO {tabela}(tag_id) VALUES('{tag_id}')"
        try:
            cursor.execute(querySelector)
            banco.commit()
            return "Entrada"
        except:
            return querySelector
    
    def apagarDados(self,banco,cursor,tabela,tag_id):
        querySelector = f"DELETE FROM {tabela} WHERE tag_id='{tag_id}'"
        try:
            cursor.execute(querySelector)
            banco.commit()
            return "Saida"
        except:
            return "Falha na execução da query apagar dados."

