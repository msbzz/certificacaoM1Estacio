from tkinter import ttk
from tkinter import *

from dadosXLSX import Dados

 
def cadastroFerramentas():
    
    cData=Dados()

    def limparCampos():
         
        _sCodigo.set('')
        _sDescricao.set('')
        _sFabricante.set('')
        _sVoltagem.set('')
        _sPartNumber.set('')
        _sTamanho.set('')
        _sUnidade.set('')
        _sTpFerramenta.set('')
        _sMaterial.set('')

    def salvar():

        dadosCadastro=[
                _sCodigo.get(),
                _sDescricao.get(),
                _sFabricante.get(),
                _sVoltagem.get(),
                _sPartNumber.get(),
                _sTamanho.get(),
                _sUnidade.get(),
                _sTpFerramenta.get(),
                _sMaterial.get()
                ]
         
         
        cData.createInsertXLSX('ferramentas.xlsx','ferramentas',dadosCadastro)
        limparCampos()

    #AKI PRODUCAO 
    master =  Toplevel()
    #AKI DEBUG
    #master = Tk()

    #LABELS e ENTRYS
    nIPADY=8 
    nPADY=8
    
    master.title("---Ferramentas---")
    master.geometry('900x600+591+215')
    master.wm_resizable(width=False,height=False)

    nomePlanilhaDeListas='listasdeferramentas.xlsx'

    #FRAME3 / TITULO
    frame1=Frame(master,width=900,height=100)#,bg='green' 
    frame1.grid(row=0,column=0,columnspan=3,sticky='nsew')
    lblTit=Label(frame1, text="CADASTRO DE FERRAMENTAS", font= ("Calibri",16))
    lblTit.pack(fill='both',pady=40,padx=300)  
     
    #FRAME3 / LABELS------------------------
    frame2=Frame(master,width=300,height=500)# 
    frame2.grid(row=1,column=0,sticky='nsew')

    Label(frame2, text="CODIGO", font=("Calibri", 12)).pack(fill='both',ipady=nIPADY) 
    Label (frame2, text="DESCRICAO", font=("Calibri", 12)).pack(fill='x',ipady=nIPADY) 
    #combo box Fabricante
    Label ( frame2, text="FABRICANTE", font=("Calibri", 12)).pack(fill='x',ipady=nIPADY) 
    Label ( frame2, text="VOLTAGEM DE USO", font=("Calibri", 12)).pack(fill='x',ipady=nIPADY)
    Label ( frame2, text="PART NUMBER", font=("Calibri", 12)).pack(fill='x',ipady=nIPADY)

    Label ( frame2, text="TAMANHO", font=("Calibri", 12)).pack(fill='x',ipady=nIPADY)
    Label ( frame2, text="UNIDADE DE MEDIDA", font=("Calibri", 13)).pack(fill='x',ipady=nIPADY)
    Label ( frame2, text="TIPO DE FERRAMENTA", font=("Calibri", 12)).pack(fill='x',ipady=nIPADY)
    Label ( frame2, text="MATERIAL", font=("Calibri", 12)).pack(fill='x',ipady=nIPADY)

    #FRAME3 / ENTRY------------------------
    frame3=Frame(master,width=300,height=500)#,bg='white' 
    frame3.grid(row=1,column=1,sticky='nsew')
   
    _sCodigo=StringVar() 
    Entry(frame3,bd=2,font=('Calibri',12),textvariable=_sCodigo).pack(fill='both',pady=nPADY)

    _sDescricao=StringVar()
    Entry(frame3,bd=2,font=('Calibri',12),textvariable=_sDescricao).pack(fill='both',pady=nPADY)
    
    # get lista fabricantes
    lst=cData.getList(nomePlanilhaDeListas,'fabricante')
    _sFabricante=StringVar()
    ttk.Combobox ( frame3,value=lst,font=("Calibri", 12),width=19,textvariable=_sFabricante).pack(fill='both',pady=nPADY)
         
    #combo box voltagem
    lst=cData.getList(nomePlanilhaDeListas,'voltagem') 
    _sVoltagem=StringVar()
    ttk.Combobox(frame3,value=lst,font=("Calibri", 12),width=19,textvariable=_sVoltagem).pack(fill='both',pady=nPADY)
        
    _sPartNumber=StringVar()
    Entry ( frame3,bd=2,font=('Calibri',12),textvariable=_sPartNumber).pack(fill='both',pady=nPADY)
    
    _sTamanho=StringVar() 
    Entry (frame3,bd=2,font=('Calibri',12),textvariable=_sTamanho).pack(fill='both',pady=nPADY) 
    
    #combo box UNIDADE DE MEDIDA
    lst=cData.getList(nomePlanilhaDeListas,'unidade de medida')    
    _sUnidade=StringVar()
    ttk.Combobox (frame3,value=lst,font=("Calibri", 12),textvariable=_sUnidade,width=19).pack(fill='both',pady=nPADY)
    
    #combo box TIPO DE FERRAMENTA
    lst=cData.getList(nomePlanilhaDeListas,'tipo de ferramentas')
    _sTpFerramenta=StringVar()
    ttk.Combobox (frame3,value=lst,font=("Calibri", 12),width=19,textvariable=_sTpFerramenta).pack(fill='both',pady=nPADY)
    
    
    #combo box MATERIAL
    lst=cData.getList(nomePlanilhaDeListas,'material') 
    _sMaterial=StringVar()  
    ttk.Combobox (frame3,value=lst,font=("Calibri", 12),width=19,textvariable=_sMaterial).pack(fill='both',pady=nPADY)    

       

    #FRAME4 / NECESSÁRIO PARA EQUILIBRAR------------------------
    frame4=Frame(master,width=300,height=500)#,bg='yellow' 
    frame4.grid(row=1,column=2)    

    #dadosCadastro=[] 

    Button(master, text="confimar", width=16, height=2, bg="orange",command=salvar).place(x=509, y=544)
    Button(master, text="retornar", width=16, height=2, bg="orange",command=master.destroy ).place(x=696, y=544)
     
    #AKI DEBUG
    #master.mainloop()

def consultarFerramentas():
    pass

def listarFerramentas():
    pass

#AKI DEBUG
#cadastroFerramentas()
 
 