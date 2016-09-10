# -*- coding: utf-8 -*-
# !/usr/bin/env python
u"""Operações com o Banco de Dados."""
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

    def list_table(self):
        u"""Lista registros da tabela."""
        self.cursor.execute(
            'SELECT * FROM persons')
        return self.cursor.fetchall()

    def query_id(self, idd):
        u"""Realiza query na tabela."""
        self.cursor.execute(
            'SELECT * FROM persons WHERE id=%d', idd)
        return self.cursor.fetchall()

    def query_name(self, name):
        u"""Realiza query na tabela."""
        self.cursor.execute(
            'SELECT * FROM persons WHERE name=%s', name)
        return self.cursor.fetchall()

    def insert(self, idd, name):
        u"""Insere registro na tabela."""
        self.cursor.execute(
            'INSERT INTO persons VALUES (%d, %s, %s)',
            (idd, name, name))
        self.conn.commit()

    def update(self, idd, name):
        u"""Insere registro na tabela."""
        self.cursor.execute(
            'UPDATE persons SET name=%s, salesrep=%s WHERE id=%d',
            (name, name, idd))
        self.conn.commit()

    def delete(self, idd):
        u"""Realiza query na tabela."""
        self.cursor.execute(
            'DELETE FROM persons WHERE id=%s', idd)
        self.conn.commit()

    def disconnect(self):
        u"""Disconecta do Banco de Dados."""
        self.conn.close()
        print "Disconnected!"
