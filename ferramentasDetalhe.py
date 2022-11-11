from tkinter import ttk
from tkinter import *

from dadosXLSX import Dados

 
def detalheFerramentas():
    
    cData=Dados()
 
    #AKI PRODUCAO 
    #master =  Toplevel()
    #AKI DEBUG
    master = Tk()

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
    lblTit=Label(frame1, text="DETALHE FERRAMENTA", font= ("Calibri",16))
    lblTit.pack(fill='both',pady=40,padx=300)  
     
    #FRAME3 / LABELS------------------------
    frame2=Frame(master,width=300,height=500)# 
    frame2.grid(row=1,column=0,sticky='nsew')

    Label(frame2, text="CODIGO", width=20,font=("Calibri", 12)).pack(fill='both',ipady=nIPADY) 
    Label (frame2, text="DESCRICAO", font=("Calibri", 12)).pack(fill='x',ipady=nIPADY) 
    #combo box Fabricante
    Label ( frame2, text="FABRICANTE", font=("Calibri", 12)).pack(fill='x',ipady=nIPADY) 
    Label ( frame2, text="VOLTAGEM DE USO", font=("Calibri", 12)).pack(fill='x',ipady=nIPADY)
    Label ( frame2, text="PART NUMBER", font=("Calibri", 12)).pack(fill='x',ipady=nIPADY)

    Label ( frame2, text="TAMANHO", font=("Calibri", 12)).pack(fill='x',ipady=nIPADY)
    Label ( frame2, text="UNIDADE DE MEDIDA", font=("Calibri", 13)).pack(fill='x',ipady=nIPADY)
    Label ( frame2, text="TIPO DE FERRAMENTA", font=("Calibri", 12)).pack(fill='x',ipady=nIPADY)
    Label ( frame2, text="MATERIAL", font=("Calibri", 12)).pack(fill='x',ipady=nIPADY)

    #FRAME3 / INFO------------------------
    frame3=Frame(master,width=300,height=500)#,bg='white' 
    frame3.grid(row=1,column=1,sticky='nsew')

    #data = ['Car', 'Bus', 'Truck', 'Bike', 'Airplane'] 
    #var = StringVar(win) 
    #my_spinbox = Spinbox(win, values=data, textvariable=var)

    #background='red'

    Label(frame3, text="CODIGO",relief=SUNKEN,width=50 ,font=("Calibri", 12)).pack(fill='both',ipady=nIPADY) 
    Label (frame3, text="DESCRICAO",relief=SUNKEN , font=("Calibri", 12)).pack(fill='x',ipady=nIPADY) 
    #combo box Fabricante
    Label ( frame3, text="FABRICANTE",relief=SUNKEN , font=("Calibri", 12)).pack(fill='x',ipady=nIPADY) 
    Label ( frame3, text="VOLTAGEM DE USO",relief=SUNKEN , font=("Calibri", 12)).pack(fill='x',ipady=nIPADY)
    Label ( frame3, text="PART NUMBER", relief=SUNKEN ,font=("Calibri", 12)).pack(fill='x',ipady=nIPADY)

    Label ( frame3, text="TAMANHO", relief=SUNKEN ,font=("Calibri", 12)).pack(fill='x',ipady=nIPADY)
    Label ( frame3, text="UNIDADE DE MEDIDA",relief=SUNKEN , font=("Calibri", 13)).pack(fill='x',ipady=nIPADY)
    Label ( frame3, text="TIPO DE FERRAMENTA",relief=SUNKEN , font=("Calibri", 12)).pack(fill='x',ipady=nIPADY)
    Label ( frame3, text="MATERIAL",relief=SUNKEN , font=("Calibri", 12)).pack(fill='x',ipady=nIPADY)
       

    #FRAME4 / NECESSÁRIO PARA EQUILIBRAR------------------------
    frame4=Frame(master,width=300,height=500)#,bg='yellow' 
    frame4.grid(row=1,column=2)    
    
 
    #Button(master, text="confimar", width=16, height=2, bg="orange",command='').place(x=509, y=544)
    Button(master, text="retornar", width=16, height=2, bg="orange",command=master.destroy ).place(x=696, y=544)
    
    
    #AKI DEBUG
    master.mainloop()
    
#AKI DEBUG
detalheFerramentas()