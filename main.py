import tkinter as tk
from ferramentas import cadastroFerramentas 
from funcionarios import cadastroFuncionarios
from solicitacoes import cadastroSolicitacoes
master = tk.Tk()
master.title("---Controle de Ferramentas---")
master.geometry('995x643+491+115')

barraMenu = tk.Menu(master)


menuFerramentas=tk.Menu(barraMenu)

menuFuncionarios=tk.Menu(barraMenu)

menuSolicitacoes=tk.Menu(barraMenu)

menuFerramentas.add_command(label='Cadastro de Ferramentas',command=cadastroFerramentas)
menuFuncionarios.add_command(label='Cadastro de Funcionarios',command=cadastroFuncionarios)
menuSolicitacoes.add_command(label='Cadastro de Solicitações',command=cadastroSolicitacoes)

barraMenu.add_cascade(label='Ferramentas',menu=menuFerramentas)
barraMenu.add_cascade(label='Funcionarios',menu=menuFuncionarios)
barraMenu.add_cascade(label='Solicitações',menu=menuSolicitacoes)
barraMenu.add
master.config(menu=barraMenu)
master.mainloop()