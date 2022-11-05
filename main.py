from tkinter import *

from ferramentas import cadastroFerramentas,consultarFerramentas,listarFerramentas 
from funcionarios import cadastroFuncionarios
from solicitacoes import cadastroSolicitacoes

master =  Tk()
master.title("---Controle de Ferramentas---")
master.geometry('995x643+491+115')

barraMenu =  Menu(master)


menuFerramentas= Menu(barraMenu)

menuFuncionarios= Menu(barraMenu)

menuSolicitacoes= Menu(barraMenu)

menuFerramentas.add_command(label='Cadastrar Ferramentas',command=cadastroFerramentas)
menuFerramentas.add_separator()
menuFerramentas.add_command(label='Consultar Ferramentas',command=consultarFerramentas)
menuFerramentas.add_separator()
menuFerramentas.add_command(label='listar Ferramentas',command=listarFerramentas)

menuFuncionarios.add_command(label='Cadastrar Funcionários',command='')
menuFuncionarios.add_separator()
menuFuncionarios.add_command(label='Consultar Funcionário',command='')
menuFuncionarios.add_separator()
menuFuncionarios.add_command(label='listar Funcionários',command='')

menuSolicitacoes.add_command(label='Cadastrar Solicitações',command='')
menuSolicitacoes.add_separator()
menuSolicitacoes.add_command(label='Consultar Solicitação',command='')
menuSolicitacoes.add_separator()
menuSolicitacoes.add_command(label='listar Solicitações',command='')


barraMenu.add_cascade(label='Ferramentas',menu=menuFerramentas)
barraMenu.add_cascade(label='Funcionarios',menu=menuFuncionarios)
barraMenu.add_cascade(label='Solicitações',menu=menuSolicitacoes)
barraMenu.add
master.config(menu=barraMenu)
master.mainloop()