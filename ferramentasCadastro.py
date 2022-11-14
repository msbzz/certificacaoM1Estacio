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

    #LABELS e ENTRYS Y
    nIPADY=8 #labels
    nPADY=8  # entrys

    nIPADX=8 #labels
    nPADX=8  #entrys
    
    #linha elementos
    linElementos=5

   #width campos info
    nWinfo=40
    nWinfoCombo=39
    nWcaption=21
    
    #master.title("---Ferramentas---")
    master.geometry('900x600+591+215')
    master.wm_resizable(width=False,height=False)

    photo = PhotoImage(file = 'imagens/toolsIco-48.png')   
    master.iconphoto(False, photo)
    
    nomePlanilhaDeListas='listasFerramentas.xlsx'

    #FRAME1 / TITULO
    frame1=Frame(master,width=900,height=100)#,bg='green' 
    frame1.grid(row=0,column=0,columnspan=3,sticky='nsew')
    lblTit=Label(frame1, text="CADASTRO DE FERRAMENTAS", font= ("Calibri",16))
    lblTit.grid(row=0,column=0,pady=40,padx=300) 
     
    #FRAME2 / LABELS e ENTRIES
    frame2=Frame(master,width=600,height=500)# 
    frame2.grid(row=1,column=0,sticky='nsew')
    
    #CODIGO
    Label(frame2, text="CODIGO", font=("Calibri", 12),width=nWcaption).grid(row=linElementos,
                                                           column=0,ipady=nIPADY,padx=nIPADX)

    _sCodigo=StringVar() 
    Entry(frame2,bd=2,font=('Calibri',12),width=nWinfo,textvariable=_sCodigo).grid(row=linElementos,
                                                                     column=1,pady=nPADY,
                                                                    padx=nPADX)


    #DESCRICAO
    Label (frame2, text="DESCRICAO", font=("Calibri", 12),width=nWcaption).grid(row=linElementos+1,
                                                                  column=0,ipady=nIPADY,padx=nIPADX)  
    _sDescricao=StringVar()
    Entry(frame2,bd=2,font=('Calibri',12),width=nWinfo,textvariable=_sDescricao).grid(row=linElementos+1,column=1,
                                                                         pady=nPADY,padx=nPADX)

    #FABRICANTE / combo box 
    Label ( frame2, text="FABRICANTE", font=("Calibri", 12),width=nWcaption).grid(row=linElementos+2,
                                                                  column=0,ipady=nIPADY,
                                                                  padx=nIPADX) 
    
    # get lista 
    lst=cData.getList(nomePlanilhaDeListas,'fabricante')
    _sFabricante=StringVar()
    ttk.Combobox ( frame2,value=lst,font=("Calibri", 12),width=nWinfoCombo,textvariable=_sFabricante).grid(row=linElementos+2,column=1,pady=nPADY,padx=nPADX)
    
    #VOLTAGEM /combo box 
    Label ( frame2, text="VOLTAGEM DE USO", font=("Calibri", 12),width=nWcaption).grid(row=linElementos+3,
                                                                       column=0,ipady=nIPADY,
                                                                        padx=nIPADX)
    
    # get lista 
    lst=cData.getList(nomePlanilhaDeListas,'voltagem')
    print('lst-->>',lst)
    _sVoltagem=StringVar()
    ttk.Combobox ( frame2,value=lst,font=("Calibri", 12),width=nWinfoCombo,
                          textvariable=_sVoltagem).grid(row=linElementos+3,
                                                         column=1,pady=nPADY,
                                                         padx=nPADX)
    
    
    #PART NUMBER
    Label ( frame2, text="PART NUMBER", font=("Calibri", 12),width=nWcaption).grid(row=linElementos+4,
                                                                    column=0,
                                                                    pady=nIPADY,
                                                                    padx=nIPADX)
    _sPartNumber=StringVar()
    Entry(frame2,bd=2,font=('Calibri',12),width=nWinfo,textvariable=_sPartNumber).grid(row=linElementos+4,column=1,pady=nPADY,padx=nPADX)
    
    
    #TAMANHO
    Label ( frame2, text="TAMANHO", font=("Calibri", 12),width=nWcaption).grid(row=linElementos+5,
                                                               column=0,pady=nIPADY,
                                                                padx=nIPADX)
    
    _sTamanho=StringVar() 
    Entry (frame2,bd=2,font=('Calibri',12),width=nWinfo,textvariable=_sTamanho).grid(row=linElementos+5,
                                                                        column=1,pady=nIPADY,
                                                                        padx=nIPADX) 
    

    #UNIDADE DE MEDIDA
    Label ( frame2, text="UNIDADE DE MEDIDA", font=("Calibri", 12),width=nWcaption).grid(row=linElementos+6,column=0,
                                                                         pady=nIPADY,padx=nIPADX)
    #combo box UNIDADE DE MEDIDA
    lst=cData.getList(nomePlanilhaDeListas,'unidade de medida')    
    _sUnidade=StringVar()
    ttk.Combobox (frame2,value=lst,font=("Calibri", 12),textvariable=_sUnidade,width=nWinfoCombo).grid(row=linElementos+6,column=1,
                                                                                                   pady=nIPADY,padx=nIPADX)    

    
    #TIPO DE FERRAMENTA 
    Label ( frame2, text="TIPO DE FERRAMENTA", font=("Calibri", 12),width=nWcaption).grid(row=linElementos+7,
                                                                               column=0,pady=nIPADY,
                                                                               padx=nIPADX)
    #combo box 
    lst=cData.getList(nomePlanilhaDeListas,'tipo de ferramentas')
    _sTpFerramenta=StringVar()
    ttk.Combobox (frame2,value=lst,font=("Calibri", 12),width=nWinfoCombo,
                        textvariable=_sTpFerramenta).grid(row=linElementos+7,
                                                        column=1,pady=nIPADY,
                                                        padx=nIPADX)
    
    #MATERIAL
    Label ( frame2, text="MATERIAL", font=("Calibri", 12),width=nWcaption).grid(row=linElementos+8,
                                                                column=0,pady=nIPADY,
                                                                padx=nIPADX)
    #combo box 
    lst=cData.getList(nomePlanilhaDeListas,'material') 
    _sMaterial=StringVar()  
    ttk.Combobox (frame2,value=lst,font=("Calibri", 12),width=nWinfoCombo,textvariable=_sMaterial).grid(row=linElementos+8,
                                                                                                 column=1,pady=nIPADY,
                                                                                                   padx=nIPADX)    
      
    #FRAME3 / ENTRY------------------------
    #frame3=Frame(master,width=300,height=500)#,bg='white' 
    #frame3.grid(row=1,column=1,sticky='nsew')
  
    Button(master, text="confimar", width=16, height=2, bg="orange",command=salvar).place(x=509, y=544)
    Button(master, text="retornar", width=16, height=2, bg="orange",command=master.destroy ).place(x=696, y=544)
     
    #AKI DEBUG
    #master.mainloop()
 

#AKI DEBUG
#cadastroFerramentas()
 
 