from tkinter import ttk
from tkinter import *
from dadosXLSX import Dados

 
def cadastroFuncionaros():
    
    cData=Dados()

    def limparCampos():
         
        _snome.set('')
        _scpf.set('')
        _stelefone.set('')
        _sturno.set('')
        _snome_equipe.set('')
       

    def salvar():

        dadosCadastro=[
                _snome.get(),
                _scpf.get(),
                _stelefone.get(),
                _sturno.get(),
                _snome_equipe.get(),
                ]
         
         
        cData.createInsertXLSX('lista_de_tecnicos.xlsx','tecnicos',dadosCadastro)
        limparCampos()

    #AKI PRODUCAO 
    master =  Toplevel()
    #AKI DEBUG
    master = Tk()

    #LABELS e ENTRYS
    nIPADY=8 
    nPADY=8
    
    master.title("---Cadastro de técnicos---")
    master.geometry('900x600+591+215')
    master.wm_resizable(width=False,height=False)

    nomePlanilhaDeListas='listaTurno.xlsx'

    #FRAME3 / TITULO
    frame1=Frame(master,width=900,height=100)#,bg='green' 
    frame1.grid(row=0,column=0,columnspan=3,sticky='nsew')
    lblTit=Label(frame1, text="CADASTRO DE TÉCNICOS", font= ("Calibri",16))
    lblTit.pack(fill='both',pady=40,padx=300)  
     
    #FRAME3 / LABELS------------------------
    frame2=Frame(master,width=300,height=500)# 
    frame2.grid(row=1,column=0,sticky='nsew')

    Label(frame2, text="NOME COMPLETO", font=("Calibri", 12)).pack(fill='both',ipady=nIPADY) 
    Label (frame2, text="CPF", font=("Calibri", 12)).pack(fill='x',ipady=nIPADY) 
    #combo box Fabricante
    Label ( frame2, text="TELEFONE", font=("Calibri", 12)).pack(fill='x',ipady=nIPADY) 
    Label ( frame2, text="TURNO", font=("Calibri", 12)).pack(fill='x',ipady=nIPADY)
    Label ( frame2, text="NOME DA EQUIPE", font=("Calibri", 12)).pack(fill='x',ipady=nIPADY)

   
    #FRAME3 / ENTRY------------------------
    frame3=Frame(master,width=300,height=500)#,bg='white' 
    frame3.grid(row=1,column=1,sticky='nsew')
   
    _snome=StringVar() 
    Entry(frame3,bd=2,font=('Calibri',12),textvariable=_snome).pack(fill='both',pady=nPADY)

    _scpf=StringVar()
    Entry(frame3,bd=2,font=('Calibri',12),textvariable=_scpf).pack(fill='both',pady=nPADY)

    _stelefone=StringVar()
    Entry(frame3,bd=2,font=('Calibri',12),textvariable=_stelefone).pack(fill='both',pady=nPADY)

    # get lista Turnos
    lst=cData.getList(nomePlanilhaDeListas,'turno')
    _sturno=StringVar()
    ttk.Combobox ( frame3,value=lst,font=("Calibri", 12),width=19,textvariable=_sturno).pack(fill='both',pady=nPADY)

    _snome_equipe=StringVar()
    Entry(frame3,bd=2,font=('Calibri',12),textvariable=_snome_equipe).pack(fill='both',pady=nPADY)
    
   

    #FRAME4 / NECESSÁRIO PARA EQUILIBRAR------------------------
    frame4=Frame(master,width=300,height=500)#,bg='yellow' 
    frame4.grid(row=1,column=2)    

    #dadosCadastro=[] 

    Button(master, text="Confimar", width=16, height=2, bg="orange",command=salvar).place(x=509, y=544)
    Button(master, text="Retornar", width=16, height=2, bg="orange",command=master.destroy ).place(x=696, y=544)
     
    #AKI DEBUG
    #master.mainloop()

def consultarFerramentas():
    pass

def listarFerramentas():
    pass

#AKI DEBUG
#cadastroFuncionaros()
 
