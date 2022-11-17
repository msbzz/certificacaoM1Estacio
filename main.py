from tkinter import *
import tkinter as tk
import tkinter as tkk

from ferramentasCadastro import cadastroFerramentas
from ferramentasConsultas import consultarFerramentas

from funcionariosCadastro import cadastroFuncionarios
from funcionariosConsultas import consultarFuncionarios

from solicitacoesCadastro import cadastroSolicitacoes
from solicitacoesConsultas import consultarSolicitacoes


# botão
btn = '#EB6440'
backGR = '#497174'
#janela
master = tk.Tk()
master.title("Controle de Ferramentas e Funcionários")
master.geometry('995x643+491+115')
master.wm_resizable(width=False,height=False)
master['background'] = backGR
#Ícone
photo = PhotoImage(file='imagens/toolsIco-48.png')
master.iconphoto(False, photo)
#fonte
fontP =('calibri', 12, 'normal')
fontTxt=('calibri', 12, 'normal')
#Responsividade
top = Frame(master)
bottom = Frame(master)
top.pack(side=TOP, pady=30)
bottom.pack(side=BOTTOM, pady=60)#, fill=BOTH, expand=True)
top['background'] = backGR
bottom['background'] = backGR

#Seção de ferramentas
#photoFer = PhotoImage(file="C:/Users/fabio.prado/Documents/GitHub/cerificacaoM1Estacio/imagens/fer.gif")
titFerramentas = Label(top, text="Sessão de Ferramentas", font=fontTxt, bg=backGR)
cadferramentas = tk.Button(top, text="Cadastro de Ferramentas", bg=btn, font=fontP, command=cadastroFerramentas)
consferramentas = tk.Button(top, text="Consulta de Ferramentas", bg=btn, font=fontP, command=consultarFerramentas)

#Funcionarios
titFuncionarios = Label(top, text="Controle de Funcionários", font=fontTxt, bg=backGR)
cadfuncionarios = tk.Button(top, text="Cadastrar Funcionário", bg=btn, font=fontP, command=cadastroFuncionarios)
consfuncionarios = tk.Button(top, text="Consultar Funcionário", bg=btn, font=fontP, command=consultarFuncionarios)


#solicitações
titSolicitacoes = Label(bottom, text="Área de Solicitações", font=fontTxt, bg=backGR)
bSCadastro = tk.Button(bottom, text="Cadastrar Solicitações", bg=btn, font=fontP, command=cadastroSolicitacoes)
bSconsult = tk.Button(bottom, text="Consultar Solicitações", bg=btn, font=fontP, command=consultarSolicitacoes)

titFerramentas.grid(row=0, column=0, padx=0, pady=0)
titFuncionarios.grid(row=0, column=2, padx=10, pady=0)
cadferramentas.grid(row=0, column=1, padx=50, pady=5)
consferramentas.grid(row=1, column=1, padx=50, pady=5)
cadfuncionarios.grid(row=0, column=3, padx=0, pady=0)
consfuncionarios.grid(row=1, column=3, padx=0, pady=0)
titSolicitacoes.grid(row=4, column=1, padx=0, pady=0)
bSCadastro.grid(row=5, column=1, padx=5, pady=0)
bSconsult.grid(row=5, column=2, padx=5, pady=0)


img = PhotoImage(file='imagens/workers-g-256.png')
label_image= Label(master,image=img).place(x=280,y=185) 
#label_image.pack()

master.mainloop()