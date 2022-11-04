import tkinter as tk

def cadastroFerramentas():
     
    master = tk.Toplevel()
    master.title("---Ferramentas---")
    master.geometry('995x643+491+115')
    #master.wm_resizable(width=False,height=False)
 
    #imgLayout = PhotoImage(file='CADASTRO_FERRAMENTAS.png')
    imgLayout =None

    labelLayout = tk.Label(master,image=imgLayout)
    labelLayout.place(x=0, y=0)
    tk.Label(master, text="CADASTRO DE FERRAMENTAS", font= ("Calibri",20)).grid(row=0,column=0,columnspan=40,padx='280',pady='20')
    #
    
    
    tk.Label(master,text='').grid(row=1,column=0,rowspan=10)
    lin=2
    
    tk.Label(master, text="CODIGO", font=("Calibri", 15)).grid(row=lin,column=0,sticky='w',padx='5' )
    eCodigo=tk.Entry(master,bd=2,font=('Calibri',15))
    eCodigo.grid(row=lin,column=1)
    
    tk.Label(master, text="DESCRICAO", font=("Calibri", 15)).grid(row=lin+1,column=0,sticky='w',padx='5')
    eDescricao=tk.Entry(master,bd=2,font=('Calibri',15))
    eDescricao.grid(row=lin+1,column=1,padx='5',pady='5')
     
    
    #Label(master, text="FABRICANTE", font=("Calibri", 15)).place(x=31, y=194)
    #Entry(master,bd=2,font=('Calibri',15)).place(width=241,height=30,x=300,y=187)

    #Label(master, text="VOLTAGEM DE USO", font=("Calibri", 15)).place(x=31, y=234)
    #Entry(master,bd=2,font=('Calibri',15)).place(width=241,height=30,x=300,y=226)

    #Label(master, text="PART NUMBER", font=("Calibri", 15)).place(x=31, y=273)
    #Entry(master,bd=2,font=('Calibri',15)).place(width=241,height=30,x=300,y=266)

    #Label(master, text="TAMANHO", font=("Calibri", 15)).place(x=31, y=313)
    #Entry(master,bd=2,font=('Calibri',15)).place(width=241,height=30,x=300,y=316)

    #Label(master, text="UNIDADE DE MEDIDA", font=("Calibri", 15)).place(x=31, y=353)
    #Entry(master,bd=2,font=('Calibri',15)).place(width=241,height=30,x=300,y=356)

    #Label(master, text="TIPO DE FERRAMENTA", font=("Calibri", 15)).place(x=31, y=400)
    #Entry(master,bd=2,font=('Calibri',15)).place(width=241,height=30,x=300,y=400)

    #Label(master, text="MATERIAL", font=("Calibri", 15)).place(x=31, y=440)
    #Entry(master,bd=2,font=('Calibri',15)).place(width=241,height=30,x=300,y=440)    
    

    #entrada
    tk.Button(master, text="confimar", width=16, height=2, bg="orange").place(x=629, y=564)
    tk.Button(master, text="retornar", width=16, height=2, bg="orange",command=master.destroy ).place(x=816, y=564)
     
 



 