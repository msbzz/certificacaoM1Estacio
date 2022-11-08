from tkinter import *

master = Tk()

master.title("--- LOGIN DE ACESSO ---")
master.geometry("605x500+307+109") #Largura x Altura + Distancia esquerda + Distancia Topo

# importa imagem
loginImg = PhotoImage(file="login.png")

# label
labelSolicitacao = Label(master, image=loginImg)
labelSolicitacao.place(x=0, y=0)

# Criação dos botoes
bt1 = Button(master, text="teste", font="Arial 30")


# funções
def clique_esq_mouse(retorno):
    print(f'X: {retorno.x} | Y: {retorno.y} Geo: {master.geometry()}')

# eventos
master.bind("<Button-1>", clique_esq_mouse)
master.mainloop()