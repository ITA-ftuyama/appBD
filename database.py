# -*- coding: utf-8 -*-
# !/usr/bin/env python
u"""Conexão com o Banco de Dados."""
# Professor: Ricardo
# Disciplina: CES-30
# Autor: Felipe Tuyama
import pymssql


class Database(object):
    u"""Banco de dados da aplicação."""

    def connect(self):
        u"""Conecta ao Banco de Dados."""
        print "Attempting to connect..."
        self.conn = pymssql.connect(
            "mssql4.gear.host",
            "hospital7443",
            "Ne6uW3o_?xfc",
            "hospital7443"
        )
        self.cursor = self.conn.cursor()
        print "Connected!"

    def create_table(self):
        u"""Cria tabela no Banco de Dados."""
        print "Creating table..."
        self.cursor.execute("""
            IF OBJECT_ID('persons', 'U') IS NOT NULL
                DROP TABLE persons
            CREATE TABLE persons (
                id INT NOT NULL,
                name VARCHAR(100),
                salesrep VARCHAR(100),
                PRIMARY KEY(id)
            )
        """)
        self.cursor.executemany(
            "INSERT INTO persons VALUES (%d, %s, %s)",
            [(1, 'John Smith', 'John Doe'),
             (2, 'Jane Doe', 'Joe Dog'),
             (3, 'Mike T.', 'Sarah H.')])
        self.conn.commit()
        print "Table created!"

    def list_table(self):
        u"""Lista registros da tabela."""
        print "Listing table..."
        lista = []
        self.cursor.execute('SELECT * FROM persons')
        row = self.cursor.fetchone()
        while row:
            lista.append(row)
            print("ID=%d, Name=%s" % (row[0], row[1]))
            row = self.cursor.fetchone()
        print "Table listed!"
        return lista

    def query_name(self, name):
        u"""Realiza query na tabela."""
        print "Querying name..."
        self.cursor.execute('SELECT * FROM persons WHERE salesrep=%s', name)
        row = self.cursor.fetchone()
        while row:
            print("ID=%d, Name=%s" % (row[0], row[1]))
            row = self.cursor.fetchone()
        print "Successfully queried!"

    def disconnect(self):
        u"""Disconecta do Banco de Dados."""
        self.conn.close()
        print "Disconnected!"
