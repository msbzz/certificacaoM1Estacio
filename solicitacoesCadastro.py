from tkinter import ttk
from tkinter import *
from tkcalendar import *

from dadosXLSX import Dados

 
def cadastroSolicitacoes():
    
    cData=Dados()

    def limparCampos():
         
        _sCpf.set('')
        _sNome.set('')
        _sEquipe.set('')
        _sCodFerramenta.set('')
        _sDataSaida.set('')
        _sHoraSaida.set('')
        _sDataDevolucao.set('')
        _sHoraDevolucao.set('')
        _Motivo.set('')
        _sReservado.set('NÃO')
    def salvar():
        
        dadosCadastro=[
        _sCpf.get(),
        _sNome.get(),
        _sEquipe.get(),
        _sCodFerramenta.get(),
        _sDataSaida.get(),
        _sHoraSaida.get(),
        _sDataDevolucao.get(),
        _sHoraDevolucao.get(),
        _Motivo.get(),
        _sReservado.get()
        ]     

         

        cData.createInsertXLSX('solicitacoes.xlsx','solicitacoes',dadosCadastro)
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


    #master.title("Cadastro de Solicitações")
    master.geometry('900x600+591+215')
    master.wm_resizable(width=False,height=False)

    photo = PhotoImage(file = 'imagens/solicitacoes-48.png')   
    master.iconphoto(False, photo) 
    
    nomePlanilhaDeListas='listasSolicitacoes.xlsx'
    nomePlanilhaDeFerramentas='ferramentas.xlsx' #codigos
    nomePlanilhaDeListasFuncionarios='listasFuncionarios.xlsx'

    #FRAME1 / TITULO
    frame1=Frame(master,width=900,height=100)#,bg='green' 
    frame1.grid(row=0,column=0,columnspan=3,sticky='nsew')
    lblTit=Label(frame1, text="CADASTRO DE SOLICITAÇÕES", font= ("Calibri",16))
    lblTit.grid(row=0,column=0,pady=40,padx=300)  
     
    #FRAME2 / LABELS e ENTRIES------------------------
    frame2=Frame(master,width=600,height=500)# 
    frame2.grid(row=1,column=0,sticky='nsew')
    
    
    #frame3=Frame(master,width=300,height=500,bg='white')# 
    #frame3.grid(row=1,column=1,sticky='nsew')

    
    # CPF label
    Label(frame2, text="CPF", font=("Calibri",
                 12),width=nWcaption).grid(row=linElementos,
                           column=0,ipady=nIPADY,padx=nIPADX) 
    
    # CPF info
    _sCpf=StringVar() 
    Entry(frame2,bd=2,font=('Calibri',12),textvariable=_sCpf,
                                          width=nWinfo).grid(row=linElementos,
                                                         column=1,pady=nPADY,
                                                         padx=nPADX)
    
    #reserva
    _sReservado=StringVar()
    chkReserva = IntVar()
    
    Checkbutton(frame2, text='RESERVA',font=('Calibri',12),
              variable= chkReserva, onvalue=1, offvalue=0, 
              command=lambda:setReserva(chkReserva)).grid(row=linElementos,column=2,
                                       pady=nPADY,padx=nPADX)


    # NOME label
    Label (frame2, text="NOME", 
          font=("Calibri", 12),width=nWcaption).grid(row=linElementos+1,
                                     column=0,ipady=nIPADY,padx=nIPADX) 
    # NOME info
    _sNome=StringVar()
    Entry(frame2,bd=2,font=('Calibri',12),
         textvariable=_sNome,width=nWinfo).grid(row=linElementos+1,column=1,
                                           pady=nPADY,padx=nPADX)    
    # EQUIPES caption
    Label ( frame2, text="EQUIPE", font=("Calibri", 12),
                   width=nWcaption).grid(row=linElementos+2,
                                        column=0,ipady=nIPADY,
                                        padx=nIPADX) 

    # EQUIPES info
    lst=cData.getList(nomePlanilhaDeListasFuncionarios,'equipes')
    _sEquipe=StringVar()
    ttk.Combobox ( frame2,value=lst,font=("Calibri", 12),width=nWinfoCombo,
                          textvariable=_sEquipe).grid(row=linElementos+2,
                          column=1,pady=nPADY,padx=nPADX)


    #codigo da ferramenta caption
    Label ( frame2, text="CODIGO DA FERRAMENTA", 
                    font=("Calibri", 12),width=nWcaption).grid(row=linElementos+3,
                                               column=0,ipady=nIPADY,
                                               padx=nIPADX)

    #codigo da ferramenta info
    lst=cData.getList(nomePlanilhaDeFerramentas,'ferramentas') 
    _sCodFerramenta=StringVar()
    ttk.Combobox(frame2,value=lst,font=("Calibri", 12),
                        width=nWinfoCombo,textvariable=_sCodFerramenta).grid(row=linElementos+3,
                                                                    column=1,
                                                                    pady=nPADY,
                                                                    padx=nPADX)

    #data saida caption
    Label ( frame2, text="DATA DA SAIDA", 
                   font=("Calibri", 12),width=nWcaption).grid(row=linElementos+4,
                                              column=0,
                                              ipady=nIPADY,
                                              padx=nIPADX)

    #data saida info    
    _sDataSaida=StringVar()
    Label(frame2,bd=2,font=('Calibri',12),textvariable=_sDataSaida,
                 relief=SUNKEN,anchor="w",
                 background='white',width=nWinfo).grid(row=linElementos+4,
                                                   column=1,
                                                   pady=nPADY,
                                                   padx=nPADX) 

    #data calendario
    photo= PhotoImage(file='imagens/calendar-24.png')
    #image=photo 
    Button(frame2, text='data',
                 command=lambda:callCalendario(1)).grid(row=linElementos+4,column=2,padx=2) 

    #hora saida caption
    Label ( frame2, text="HORA DA SAIDA", 
                  font=("Calibri", 12),width=nWcaption).grid(row=linElementos+5,
                                             column=0,ipady=nIPADY,
                                             padx=nIPADX)

    #hora saida info
    _sHoraSaida=StringVar()
    lst=cData.getList(nomePlanilhaDeListas,'horarios')
    ttk.Combobox (frame2,value=lst,font=("Calibri", 12),
                        width=nWinfoCombo,
                        textvariable=_sHoraSaida).grid(row=linElementos+5,
                                                       column=1,
                                                       pady=nPADY,
                                                       padx=nPADX)

    _sHoraDevolucao=StringVar()

    
    #data devolucao caption
    Label ( frame2, text="DATA DA DEVOLUÇÃO", 
                   font=("Calibri", 13),
                   width=nWcaption).grid(row=linElementos+6,column=0,
                                         ipady=nIPADY,padx=nIPADX)

    #data devolucao info
    _sDataDevolucao=StringVar()

    Label(frame2,bd=2,font=('Calibri',12),textvariable=_sDataDevolucao,
                 relief=SUNKEN,anchor="w",background='white',
                width=nWinfo).grid(row=linElementos+6,
                              column=1,pady=nPADY,padx=nPADX) 
    #image==photo,
    Button(frame2, text='data', 
                  command=lambda:callCalendario(2)).grid(row=linElementos+6,column=2,padx=2)
    #hora devolucao caption
    Label ( frame2, text="HORA DA DEVOLUÇÃO", 
                    font=("Calibri", 12),
                    width=nWcaption).grid(row=linElementos+7,
                                          column=0,ipady=nIPADY,
                                          padx=nIPADX)

    #hora devolucao info
    lst=cData.getList(nomePlanilhaDeListas,'horarios')
    _sHoraDevolucao=StringVar()
    ttk.Combobox (frame2,value=lst,
                         font=("Calibri", 12),width=nWinfoCombo,
                         textvariable=_sHoraDevolucao).grid(row=linElementos+7,
                                                           column=1,pady=nPADY,
                                                           padx=nPADX)


    #motivo caption
    Label ( frame2, text="MOTIVO", 
                    font=("Calibri", 12),
                    width=nWcaption).grid(row=linElementos+8,
                                          column=0,ipady=nIPADY,
                                          padx=nIPADX)

    #motivo info
    lst=cData.getList(nomePlanilhaDeListas,'motivo') 
    _Motivo=StringVar()  
    ttk.Combobox (frame2,value=lst,font=("Calibri", 12),
                         width=nWinfoCombo,
                         textvariable=_Motivo).grid(row=linElementos+8,
                                                    column=1,
                                                    pady=nPADY,
                                                    padx=nPADX)    

    #frame4=Frame(master,width=300,height=500)#,bg='yellow' 
    #frame4.grid(row=1,column=2)    

     
    limparCampos()

    Button(master, text="confimar", width=16, height=2, bg="orange",command=salvar).place(x=509, y=544)
    Button(master, text="retornar", width=16, height=2, bg="orange",command=master.destroy ).place(x=696, y=544)
    
    def setReserva(chkReserva):
        if chkReserva ==1:
            _sReservado.set('SIM')
        else:
            _sReservado.set('NÃO')    

    def callCalendario(valor):
        def print_sel():
            if valor==1:
               _sDataSaida.set(cal.get_date())
            else:
               _sDataDevolucao.set(cal.get_date())
 
        def quit1():
            top.destroy()

        import datetime
        current_time = datetime.datetime.now()

        top = Toplevel(master)

        photo = PhotoImage(file = 'imagens/calendar-48.png')   
        top.iconphoto(False, photo)
        top.geometry('450x500+1150+315')

        cal = Calendar(top,
                       font="Arial 14", selectmode='day',
                       cursor="hand1", year=current_time.year, month=current_time.month, day=current_time.day)
        cal.pack(fill="both", expand=True)



        ttk.Button(top, text="ok", command=print_sel).pack()
        ttk.Button(top, text="exit", command=quit1).pack()


        my_label = Label(master, text='')
        my_label.pack(pady=20)
 
    #AKI DEBUG
    #master.mainloop()
 
#AKI DEBUG
#cadastroSolicitacoes()
 
 
