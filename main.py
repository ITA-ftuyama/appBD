# -*- coding: utf-8 -*-
# !/usr/bin/env python
u"""Aplicação GUI em alto nível."""
# Professor: Ricardo
# Disciplina: CES-30
# Autor: Felipe Tuyama
from database import Database
from Tkinter import *
import tkMessageBox


class Application:
    u"""Aplicação principal."""

    def __init__(self, master=None):
        u"""Inicializa a GUI."""
        self.giu = master
        self.fontePadrao = ("Consolas", "12")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 20
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 50
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 50
        self.terceiroContainer.pack()

        self.tresmeioContainer = Frame(master)
        self.tresmeioContainer["padx"] = 50
        self.tresmeioContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["pady"] = 20
        self.quintoContainer.pack()

        self.titulo = Label(self.primeiroContainer,
                            text="Gerenciador de Pacientes")
        self.titulo["font"] = ("Arial", "14", "bold")
        self.titulo.pack()

        self.iddLabel = Label(self.segundoContainer,
                              text="__Id  : ", font=self.fontePadrao)
        self.iddLabel.pack(side=LEFT)

        self.idd = Entry(self.segundoContainer)
        self.idd["width"] = 30
        self.idd["font"] = self.fontePadrao
        self.idd.pack(side=LEFT)

        self.nomeLabel = Label(self.terceiroContainer,
                               text="Nome  : ", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.terceiroContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.doencaLabel = Label(self.tresmeioContainer,
                                 text="Doença: ", font=self.fontePadrao)
        self.doencaLabel.pack(side=LEFT)

        self.doenca = Entry(self.tresmeioContainer)
        self.doenca["width"] = 30
        self.doenca["font"] = self.fontePadrao
        self.doenca.pack(side=LEFT)

        self.criad = Button(self.quartoContainer)
        self.criad["text"] = "Criar BD"
        self.criad["font"] = self.fontePadrao
        self.criad["width"] = 12
        self.criad["command"] = self.criar_bd
        self.criad.pack()

        self.buscar_id = Button(self.quartoContainer)
        self.buscar_id["text"] = "Buscar Id"
        self.buscar_id["font"] = self.fontePadrao
        self.buscar_id["width"] = 12
        self.buscar_id["command"] = self.buscar_id_bd
        self.buscar_id.pack()

        self.buscar_nome = Button(self.quartoContainer)
        self.buscar_nome["text"] = "Buscar Nome"
        self.buscar_nome["font"] = self.fontePadrao
        self.buscar_nome["width"] = 12
        self.buscar_nome["command"] = self.buscar_nome_bd
        self.buscar_nome.pack()

        self.inserir = Button(self.quartoContainer)
        self.inserir["text"] = "Inserir"
        self.inserir["font"] = self.fontePadrao
        self.inserir["width"] = 12
        self.inserir["command"] = self.inserir_bd
        self.inserir.pack()

        self.inserir = Button(self.quartoContainer)
        self.inserir["text"] = "Atualizar"
        self.inserir["font"] = self.fontePadrao
        self.inserir["width"] = 12
        self.inserir["command"] = self.editar_bd
        self.inserir.pack()

        self.deletar = Button(self.quartoContainer)
        self.deletar["text"] = "Deletar"
        self.deletar["font"] = self.fontePadrao
        self.deletar["width"] = 12
        self.deletar["command"] = self.deletar_bd
        self.deletar.pack()

        self.listar_bd()

    def listar_bd(self):
        u"""Lista tabela do banco de dados."""
        lista = db.list_table()

        self.quintoContainer.destroy()

        self.quintoContainer = Frame(self.giu)
        self.quintoContainer["pady"] = 40
        self.quintoContainer.pack()

        self.lista_label = Label(
            self.quintoContainer,
            text="Lista de Pacientes",
            font=("Arial", "12", "bold")
        )
        self.lista_label.pack()

        self.entry = Entry(self.quintoContainer)
        self.entry.insert(
            END, '%3s | %17s | %12s' % ("ID", "NOME DO PACIENTE", "DOENÇA")
        )
        self.entry["width"] = 40
        self.entry["font"] = self.fontePadrao
        self.entry.pack()

        for elem in lista:
            self.entry = Entry(self.quintoContainer)
            self.entry["width"] = 40
            self.entry["font"] = self.fontePadrao
            self.entry.insert(
                END, '%3s | %17s | %12s' % (elem[0], elem[1], elem[2])
            )
            self.entry.pack()

    def display_result(self, result):
        u"""Exibe resultado de busca."""
        tkMessageBox.showinfo(
            "Resultado da busca",
            '\n'.join(
                ['%s - %s - %s' % (
                    row[0], row[1], row[2]
                ) for row in result]
            )
        )

    def criar_bd(self):
        u"""Cria nova tabela no banco de dados."""
        db.create_table()
        self.listar_bd()

    def buscar_id_bd(self):
        u"""Busca registro no banco de dados."""
        self.display_result(db.query_id(int(self.idd.get())))

    def buscar_nome_bd(self):
        u"""Busca registro no banco de dados."""
        self.display_result(db.query_name(self.nome.get()))

    def inserir_bd(self):
        u"""Insere registro no banco de dados."""
        db.insert(
            int(self.idd.get()), self.nome.get(), self.doenca.get()
        )
        self.listar_bd()

    def editar_bd(self):
        u"""Edita registro no banco de dados."""
        db.update(
            int(self.idd.get()), self.nome.get(), self.doenca.get()
        )
        self.listar_bd()

    def deletar_bd(self):
        u"""Deleta registro no banco de dados."""
        db.delete(int(self.idd.get()))
        self.listar_bd()

db = Database()
db.connect()
root = Tk()
root.wm_title("Gerenciador de Pacientes")
Application(root)
root.mainloop()
db.disconnect()
