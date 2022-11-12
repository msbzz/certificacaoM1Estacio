from tkinter import *
import tkinter as tk
import tkinter as tkk

from ferramentasCadastro import cadastroFerramentas
from ferramentasConsultas import consultarFerramentas

from funcionariosCadastro import cadastroFuncionarios
from funcionariosConsultas import consultarFuncionarios

from solicitacoesCadastro import cadastroSolicitacoes
from solicitacoesConsultas import consultarSolicitacoes
#janela
master = tk.Tk()



master.title("Controle de Ferramentas e Funcionários")
master.geometry('995x643+491+115')

 
photo = PhotoImage(file = 'imagens/toolsIco-48.png')# es.ico
master.iconphoto(False, photo)
#fonte
fontP =('calibri', 12, 'normal')
#Responsividade
jFerramentas = tk.Frame(master)
jFuncionarios = tk.Frame(master)
jSolicitacoes = tk.Frame(master)

#Seção de ferramentas
scFerramentas = tk.Listbox(jFerramentas)
#photo = tk.PhotoImage(master, arquivo="/cerificacaoM1Estacio/imagens/ferramentas.jpg")
bFCadastro = tk.Button(jFerramentas, text="Cadastro de Ferramentas", font=fontP, command=cadastroFerramentas).grid(row=1, column=0)
bFConsulta = tk.Button(jFerramentas, text="Consulta de Ferramentas", font=fontP,command=consultarFerramentas).grid(row=2, column=0)
#bFListar = tk.Button(jFerramentas, text="Listar de Ferramentas", font=fontP).grid(row=3, column=0)


#Funcionarios
scFuncionarios = tk.Listbox(jFuncionarios)
bCadastroF = tk.Button(jFuncionarios, text="Cadastrar Funcionário", font=fontP, command=cadastroFuncionarios).grid(row=1, column=1)
bConsultaF = tk.Button(jFuncionarios, text="Consultar Funcionário", font=fontP,command=consultarFuncionarios).grid(row=2, column=1)
#bListF = tk.Button(jFuncionarios, text="Listar Funcionário", font=fontP).grid(row=3, column=1)

#solicitações
scSolicitacoes = tk.Listbox(jSolicitacoes)
bSCadastro = tk.Button(jSolicitacoes, text="Cadastrar Solicitações", font=fontP, command=cadastroSolicitacoes).grid(row=5, column=1)
bSconsult = tk.Button(jSolicitacoes, text="Consultar Solicitações", font=fontP,command=consultarSolicitacoes).grid(row=6, column=1)
#bSList = tk.Button(jSolicitacoes, text="Listar Solicitações", font=fontP).grid(row=7, column=1)


jFerramentas.pack(anchor=NW, padx=50, pady=30)
jFuncionarios.pack(anchor=NE, padx=50, pady=30)
jSolicitacoes.pack(anchor=SW, padx=50, pady=30)




master.mainloop()