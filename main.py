# -*- coding: utf-8 -*-
# !/usr/bin/env python
u"""Aplicação GUI em alto nível."""
# Professor: Ricardo
# Disciplina: CES-30
# Autor: Felipe Tuyama
from database import Database
from Tkinter import *


class Application:
    u"""Aplicação principal."""

    def __init__(self, master=None):
        u"""Inicializa a GUI."""
        self.fontePadrao = ("Arial", "12")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 20
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["pady"] = 40
        self.quintoContainer.pack()

        self.titulo = Label(self.primeiroContainer,
                            text="Gerenciador de Pacientes")
        self.titulo["font"] = ("Arial", "14", "bold")
        self.titulo.pack()

        self.iddLabel = Label(self.segundoContainer,
                              text="Id", font=self.fontePadrao)
        self.iddLabel.pack(side=LEFT)

        self.idd = Entry(self.segundoContainer)
        self.idd["width"] = 30
        self.idd["font"] = self.fontePadrao
        self.idd.pack(side=LEFT)

        self.nomeLabel = Label(self.terceiroContainer,
                               text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.terceiroContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.buscar = Button(self.quartoContainer)
        self.buscar["text"] = "Buscar"
        self.buscar["font"] = self.fontePadrao
        self.buscar["width"] = 12
        self.buscar["command"] = self.verificaSenha
        self.buscar.pack()

        self.inserir = Button(self.quartoContainer)
        self.inserir["text"] = "Inserir"
        self.inserir["font"] = self.fontePadrao
        self.inserir["width"] = 12
        self.inserir["command"] = self.verificaSenha
        self.inserir.pack()

        self.deletar = Button(self.quartoContainer)
        self.deletar["text"] = "Deletar"
        self.deletar["font"] = self.fontePadrao
        self.deletar["width"] = 12
        self.deletar["command"] = self.verificaSenha
        self.deletar.pack()

        self.mensagem = Label(self.quartoContainer,
                              text="", font=self.fontePadrao)
        self.mensagem.pack()
        self.listar_bd()

    def listar_bd(self):
        u"""Conecta ao banco de dados."""
        lista = db.list_table()

        self.lista_label = Label(
            self.quintoContainer,
            text="Lista de Pacientes",
            font=("Arial", "12", "bold")
        )
        self.lista_label.pack()

        entry = Entry(self.quintoContainer)
        entry.insert(END, '%5s | %20s' % ("ID", "NOME DO PACIENTE"))
        entry["width"] = 30
        entry["font"] = self.fontePadrao
        entry.pack()
        for elem in lista:
            entry = Entry(self.quintoContainer)
            entry["width"] = 30
            entry["font"] = self.fontePadrao
            entry.insert(END, '%5s | %20s' % (elem[0], elem[1]))
            entry.pack()

    def criar_bd(self):
        u"""Cria nova tabela no banco de dados."""
        db.create_table()

    def buscar_bd(self):
        u"""Busca registro no banco de dados."""
        db.query_name('John Smith')

    def verificaSenha(self):
        u"""Lista registros da tabela."""
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "usuariodevmedia" and senha == "dev":
            self.mensagem["text"] = "Autenticado"
        else:
            self.mensagem["text"] = "Erro na autenticação"


db = Database()
db.connect()
root = Tk()
root.wm_title("Gerenciador de Pacientes")
Application(root)
root.mainloop()
db.disconnect()
