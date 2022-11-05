from tkinter import ttk
from tkinter import *

from dadosXLSX import Dados

 
def cadastroFerramentas():
    
    cData=Dados()

    def limparCampos():
         
        _sCodigo.delete(0,'end')
        _sDescricao.delete(0,'end')
        _sFabricante.delete(0,'end')
        _sVoltagem.delete(0,'end')
        _sPartNumber.delete(0,'end')
        _sTamanho.delete(0,'end')
        _sUnidade.delete(0,'end')
        _sTpFerramenta.delete(0,'end')
        _sMaterial.delete(0,'end')

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

    #somente desabilitar para testes 
    master =  Toplevel()
    #somente habilitar para testes
    #master = Tk()

    frame=Frame(master) 

    master.title("---Ferramentas---")
    master.geometry('995x643+591+215')
    master.wm_resizable(width=False,height=False)
 
    #imgLayout = PhotoImage(file='CADASTRO_FERRAMENTAS.png')
    imgLayout =None

    labelLayout = Label(frame,image=imgLayout)
    labelLayout.place(x=0, y=0)
    Label(frame, text="CADASTRO DE FERRAMENTAS", font= ("Calibri",20)).grid(row=0,column=0,columnspan=40,padx=280,pady=20)
     
    
    #ISSO AKI É PARA CRIAR O ESPAÇAMANTO DO TITULO
    #QUEM TIVER A SOLUÇÂO AVISE
    """
    Label (frame,text='').grid(row=1,column=0 )
    Label (frame,text='').grid(row=1,column=1)
    Label (frame,text='').grid(row=2,column=0 )
    Label (frame,text='').grid(row=2,column=1)
    """
    lin=6
    nomePlanilhaDeListas='listasdeferramentas.xlsx'
    # --------------------------------------------------------------
    Label(frame, text="CODIGO", font=("Calibri", 15)).grid(row=lin,column=0,sticky='w',padx=5 )
    _sCodigo= Entry(frame,bd=2,font=('Calibri',15))
    _sCodigo.grid(row=lin,column=1)
    # --------------------------------------------------------------
    Label (frame, text="DESCRICAO", font=("Calibri", 15)).grid(row=lin+1,column=0,sticky='w',padx='5')
    _sDescricao= Entry (frame,bd=2,font=('Calibri',15))
    _sDescricao.grid(row=lin+1,column=1,padx='5',pady='5')
    # --------------------------------------------------------------    
    Label (frame, text="FABRICANTE", font=("Calibri", 15)).grid(row=lin+2,column=0,sticky='w',padx='5')
    #combo box Fabricante
    lst=cData.getList(nomePlanilhaDeListas,'fabricante')  
    _sFabricante = ttk.Combobox (frame,value=lst,font=("Calibri", 15),width=19)
    _sFabricante.grid(row=lin+2,column=1,padx=16,sticky='w')
    # --------------------------------------------------------------
    Label (frame, text="VOLTAGEM DE USO", font=("Calibri", 15)).grid(row=lin+3,column=0,sticky='w',padx='5' )
    #combo box voltagem
    lst=cData.getList(nomePlanilhaDeListas,'voltagem') 
    _sVoltagem = ttk.Combobox (frame,value=lst,font=("Calibri", 15),width=19)
    _sVoltagem.grid(row=lin+3,column=1,padx='5',pady='5')
    # --------------------------------------------------------------
    Label (frame, text="PART NUMBER", font=("Calibri", 15)).grid(row=lin+4,column=0,sticky='w',padx='5' )
    _sPartNumber= Entry (frame,bd=2,font=('Calibri',15))
    _sPartNumber.grid(row=lin+4,column=1,padx='5',pady='5')
    # --------------------------------------------------------------
    Label (frame, text="TAMANHO", font=("Calibri", 15)).grid(row=lin+5,column=0,sticky='w',padx='5' )
    _sTamanho= Entry (frame,bd=2,font=('Calibri',15)) 
    _sTamanho.grid(row=lin+5,column=1,padx='5',pady='5')
    # --------------------------------------------------------------    
    Label (frame, text="UNIDADE DE MEDIDA", font=("Calibri", 15)).grid(row=lin+6,column=0,sticky='w',padx='5')
    #combo box TIPO DE FERRAMENTA
    lst=cData.getList(nomePlanilhaDeListas,'unidade de medida')    
    _sUnidade= ttk.Combobox (frame,value=lst,font=("Calibri", 15),width=18)
    _sUnidade.grid(row=lin+6,column=1,padx='2',pady='5')
    # --------------------------------------------------------------
    Label (frame, text="TIPO DE FERRAMENTA", font=("Calibri", 15)).grid(row=lin+7,column=0,sticky='w',padx='5')
    #combo box TIPO DE FERRAMENTA
    lst=cData.getList(nomePlanilhaDeListas,'tipo de ferramentas')
    _sTpFerramenta= ttk.Combobox (frame,value=lst,font=("Calibri", 15),width=18) 
    _sTpFerramenta.grid(row=lin+7,column=1,padx='2',pady='5')
    # --------------------------------------------------------------     
    Label (frame, text="MATERIAL", font=("Calibri", 15)).grid(row=lin+8,column=0,sticky='w',padx='5')
    #combo box MATERIAL
    lst=cData.getList(nomePlanilhaDeListas,'material')   
    _sMaterial= ttk.Combobox (frame,value=lst,font=("Calibri", 15),width=18)    
    _sMaterial.grid(row=lin+8,column=1,padx='2',pady='5')
    



    #print(ls)   
    #entrada
    Button(master, text="confimar", width=16, height=2, bg="orange",command=salvar).place(x=629, y=564)
    Button(master, text="retornar", width=16, height=2, bg="orange",command=master.destroy ).place(x=816, y=564)
    
    frame.pack()
     
    dadosCadastro=[] 

    #somente habilitar para testes
    #master.mainloop()

def consultarFerramentas():
    pass

def listarFerramentas():
    pass

#somente habilitar para testes
#cadastroFerramentas()
 
 