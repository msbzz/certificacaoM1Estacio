from tkinter import  *

 
def cadastroFerramentas():
    def click_mouse(retorno):
        print(retorno)
        print(f'x : {retorno.x} | y : {retorno.y} | geo : {master.geometry()}')

    master = Tk()
    master.title("---Ferramentas---")
    master.geometry('995x643+491+115')
    #master.wm_resizable(width=False,height=False)
 
    #imgLayout = PhotoImage(file='CADASTRO_FERRAMENTAS.png')
    imgLayout =None

    labelLayout = Label(master,image=imgLayout)
    labelLayout.place(x=0, y=0)
    Label(master, text="CADASTRO DE FERRAMENTAS", font= ("Calibri",20)).place(x=247,y=25)
    
    Label(master, text="CODIGO", font=("Calibri", 15)).place(x=31, y=102)
    Entry(master,bd=2,font=('Calibri',15)).place(width=241,height=30,x=300,y=101)

    Label(master, text="DESCRICAO", font=("Calibri", 15)).place(x=31, y=148)
    Entry(master,bd=2,font=('Calibri',15)).place(width=241,height=30,x=300,y=148)

    Label(master, text="FABRICANTE", font=("Calibri", 15)).place(x=31, y=194)
    Entry(master,bd=2,font=('Calibri',15)).place(width=241,height=30,x=300,y=187)

    Label(master, text="VOLTAGEM DE USO", font=("Calibri", 15)).place(x=31, y=234)
    Entry(master,bd=2,font=('Calibri',15)).place(width=241,height=30,x=300,y=226)

    Label(master, text="PART NUMBER", font=("Calibri", 15)).place(x=31, y=273)
    Entry(master,bd=2,font=('Calibri',15)).place(width=241,height=30,x=300,y=266)

    Label(master, text="TAMANHO", font=("Calibri", 15)).place(x=31, y=313)
    Entry(master,bd=2,font=('Calibri',15)).place(width=241,height=30,x=300,y=316)

    Label(master, text="UNIDADE DE MEDIDA", font=("Calibri", 15)).place(x=31, y=353)
    Entry(master,bd=2,font=('Calibri',15)).place(width=241,height=30,x=300,y=356)

    Label(master, text="TIPO DE FERRAMENTA", font=("Calibri", 15)).place(x=31, y=400)
    Entry(master,bd=2,font=('Calibri',15)).place(width=241,height=30,x=300,y=400)

    Label(master, text="MATERIAL", font=("Calibri", 15)).place(x=31, y=440)
    Entry(master,bd=2,font=('Calibri',15)).place(width=241,height=30,x=300,y=440)    


    #entrada
    Button(master, text="confimar", width=16, height=2, bg="orange").place(x=629, y=564)
    Button(master, text="retornar", width=16, height=2, bg="orange" ).place(x=816, y=564)

    Button(master, text="pesquisar", width=16, height=2, bg="orange" ).place(x=20, y=564)
    """
     

    
    """
    master.bind("<Button-1>",click_mouse)
    master.mainloop()


cadastroFerramentas()