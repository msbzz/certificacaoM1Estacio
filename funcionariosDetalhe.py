from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from dadosXLSX import Dados


def detalheFuncionario():

    cData = Dados()
    # PRODUÇÃO
    lsDetalhe = cData.readFileTemp()

    print('lsDetalhe ------>>', lsDetalhe)
    # APENAS DEBUG
    # AKI DEBUG
    #lsDetalhe=['FULANO SILVA', '(21)99212912', '890.332.121.98', 'NOITE', 'BALADA']

    # AKI PRODUCAO
    master_ch = Toplevel()
    # AKI DEBUG
    #master_ch = Tk()

    # LABELS e ENTRYS Y
    nIPADY = 8  # labels
    nPADY = 8  # entrys

    nIPADX = 8  # labels
    nPADX = 8  # entrys

    # linha elementos
    linElementos = 5

    # width campos info
    nWinfo = 40
    nWcaption = 21

    #master_ch.title("Detalhe Solicitação")
    master_ch.geometry('900x600+610+255')
    master_ch.wm_resizable(width=False, height=False)

    #FRAME1 / TITULO
    frame1 = Frame(master_ch, width=900, height=100)  # ,bg='green'
    frame1.grid(row=0, column=0, columnspan=3, sticky='nsew')

    lblTit = Label(frame1, text="DETALHE FUNCIONÁRIO", font=("Calibri", 16))
    lblTit.grid(row=0, column=0, pady=40, padx=300)

    # FRAME2 / LABELS------------------------
    frame2 = Frame(master_ch, width=300, height=500)
    frame2.grid(row=1, column=0, sticky='nsew')

    # essa dicionario serve apenas para saber o indice
    dadosDetalhe = {
        'nome': 0,
        'cpf': 1,
        'telefone': 2,
        'turno': 3,
        'equipe': 4 
     }

    # PONTO DE CONFIGURAÇÃO / LABELs CONSULTA DETALHE

    # NOME caption
    Label(frame2, text="NOME", font=(
        "Calibri", 12), width=nWcaption).grid(row=linElementos,
                                              column=0, ipady=nIPADY, padx=nIPADX)

    # NOME info
    Label(frame2, text=lsDetalhe[0], relief=SUNKEN, width=nWinfo,
          font=("Calibri", 12)).grid(row=linElementos,
                                     column=1, pady=nPADY,
                                     padx=nPADX)

 
    # CPF label
    Label(frame2, text="CPF", font=(
        "Calibri", 12), width=nWcaption).grid(row=linElementos+1,
                                              column=0, ipady=nIPADY, padx=nIPADX)

    # CPF info
    Label(frame2, text=lsDetalhe[1], relief=SUNKEN, font=(
        "Calibri", 12), width=nWinfo).grid(row=linElementos+1, column=1,
                                           pady=nPADY, padx=nPADX)

    # TELEFONE label
    Label(frame2, text="TELEFONE", font=(
        "Calibri", 12), width=nWcaption).grid(row=linElementos+2,
                                              column=0, ipady=nIPADY,
                                              padx=nIPADX)

    # CPF TELEFONE
    Label(frame2, text=lsDetalhe[2], relief=SUNKEN, font=(
        "Calibri", 12), width=nWinfo).grid(row=linElementos+2,
                                           column=1, pady=nPADY, padx=nPADX)

    # TURNO label
    Label(frame2, text="TELEFONE", font=(
        "Calibri", 12), width=nWcaption).grid(row=linElementos+3,
                                              column=0, ipady=nIPADY,
                                              padx=nIPADX)

    # TURNO info
    Label(frame2, text=lsDetalhe[3], relief=SUNKEN,
          font=("Calibri", 12), width=nWinfo).grid(row=linElementos+3,
                                                   column=1,
                                                   pady=nPADY,
                                                   padx=nPADX)

    # EQUIPE label
    Label(frame2, text="TURNO", font=(
        "Calibri", 12), width=nWcaption).grid(row=linElementos+4,
                                              column=0,
                                              ipady=nIPADY,
                                              padx=nIPADX)

    # EQUIPE info
    Label(frame2, text=lsDetalhe[4], relief=SUNKEN, font=(
        "Calibri", 12), width=nWinfo).grid(row=linElementos+4,
                                           column=1,
                                           pady=nPADY,
                                           padx=nPADX)
 
    # FRAME3 / INFO------------------------
    # frame3 = Frame(master_ch, width=300, height=500)  # ,bg='white'
    #frame3.grid(row=1, column=1, sticky='nsew')

    Button(master_ch, text="retornar", width=16, height=2,
           bg="orange", command=master_ch.destroy).place(x=696, y=544)

    # AKI DEBUG
    #master_ch.mainloop()
# AKI DEBUG
#detalheFuncionario()
 