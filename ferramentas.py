import tkinter as tk

from dadosXLSX import Dados

 
def cadastroFerramentas():
    

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
         
        c=Dados() 
        c.createInsertXLSX('ferramentas.xlsx','ferramentas',dadosCadastro)
        limparCampos()

    master = tk.Toplevel()
    #master = tk.Tk()
    master.title("---Ferramentas---")
    master.geometry('995x643+591+215')
    master.wm_resizable(width=False,height=False)
 
    #imgLayout = PhotoImage(file='CADASTRO_FERRAMENTAS.png')
    imgLayout =None

    labelLayout = tk.Label(master,image=imgLayout)
    labelLayout.place(x=0, y=0)
    tk.Label(master, text="CADASTRO DE FERRAMENTAS", font= ("Calibri",20)).grid(row=0,column=0,columnspan=40,padx=280,pady=20)
     
    
    #ISSO AKI É PARA CRIAR O ESPAÇAMANTO DO TITULO
    #QUEM TIVER A SOLUÇÂO AVISE
    tk.Label(master,text='').grid(row=1,column=0 )
    tk.Label(master,text='').grid(row=1,column=1)
    tk.Label(master,text='').grid(row=2,column=0 )
    tk.Label(master,text='').grid(row=2,column=1)

    lin=3
    
    tk.Label(master, text="CODIGO", font=("Calibri", 15)).grid(row=lin,column=0,sticky='w',padx=5 )
    _sCodigo=tk.Entry(master,bd=2,font=('Calibri',15))
    _sCodigo.grid(row=lin,column=1)
    
    tk.Label(master, text="DESCRICAO", font=("Calibri", 15)).grid(row=lin+1,column=0,sticky='w',padx='5')
    _sDescricao=tk.Entry(master,bd=2,font=('Calibri',15))
    _sDescricao.grid(row=lin+1,column=1,padx='5',pady='5')
    
    tk.Label(master, text="FABRICANTE", font=("Calibri", 15)).grid(row=lin+2,column=0,sticky='w',padx='5')
    _sFabricante=tk.Entry(master,bd=2,font=('Calibri',15))
    _sFabricante.grid(row=lin+2,column=1,padx='5',pady='5')
    
    tk.Label(master, text="VOLTAGEM DE USO", font=("Calibri", 15)).grid(row=lin+3,column=0,sticky='w',padx='5' )
    _sVoltagem=tk.Entry(master,bd=2,font=('Calibri',15))
    _sVoltagem.grid(row=lin+3,column=1,padx='5',pady='5')
    
    tk.Label(master, text="PART NUMBER", font=("Calibri", 15)).grid(row=lin+4,column=0,sticky='w',padx='5' )
    _sPartNumber=tk.Entry(master,bd=2,font=('Calibri',15))
    _sPartNumber.grid(row=lin+4,column=1,padx='5',pady='5')

    tk.Label(master, text="TAMANHO", font=("Calibri", 15)).grid(row=lin+5,column=0,sticky='w',padx='5' )
    _sTamanho=tk.Entry(master,bd=2,font=('Calibri',15)) 
    _sTamanho.grid(row=lin+5,column=1,padx='5',pady='5')
    
    tk.Label(master, text="UNIDADE DE MEDIDA", font=("Calibri", 15)).grid(row=lin+6,column=0,sticky='w',padx='5')
    _sUnidade=tk.Entry(master,bd=2,font=('Calibri',15))
    _sUnidade.grid(row=lin+6,column=1,padx='5',pady='5')

    tk.Label(master, text="TIPO DE FERRAMENTA", font=("Calibri", 15)).grid(row=lin+7,column=0,sticky='w',padx='5')
    _sTpFerramenta=tk.Entry(master,bd=2,font=('Calibri',15)) 
    _sTpFerramenta.grid(row=lin+7,column=1,padx='5',pady='5')
     
    tk.Label(master, text="MATERIAL", font=("Calibri", 15)).grid(row=lin+8,column=0,sticky='w',padx='5')
    _sMaterial=tk.Entry(master,bd=2,font=('Calibri',15))     
    _sMaterial.grid(row=lin+8,column=1,padx='5',pady='5')
    



    #print(ls)   
    #entrada
    tk.Button(master, text="confimar", width=16, height=2, bg="orange",command=salvar).place(x=629, y=564)
    tk.Button(master, text="retornar", width=16, height=2, bg="orange",command=master.destroy ).place(x=816, y=564)
    
     
    dadosCadastro=[] 

    #master.mainloop()

def consultarFerramentas():
    pass

def listarFerramentas():
    pass

#cadastroFerramentas()
 
 