from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from dadosXLSX import Dados

def detalheFerramenta():
    
    cData=Dados()
    
    #PRODUÇÃO
    lsDetalhe=cData.readFileTemp()
    #DEGUB
    #lsDetalhe=['MMEI-W45', 'FERRAMENTA2', 'BOSCH', 220, 'DIEOW-3', '44X9', 'PESAGEM', 'CHAVE PHILLIPS', 'AÇO RÁPIDO']
    print('detalheFerramenta-->>>',lsDetalhe)
    # AKI PRODUCAO
    master_ch = Toplevel()
    # AKI DEBUG
    #master_ch = Tk()

    # LABELS e ENTRYS
    nIPADY = 8
    nPADY = 8

    master_ch.title("Consultar Ferramentas")
    master_ch.geometry('900x600+610+255')
    master_ch.wm_resizable(width=False, height=False)

    #nomePlanilhaDeListas = 'listasdeferramentas.xlsx'

    print('detalheFerramenta2 --->',lsDetalhe)
    #FRAME3 / TITULO
    frame1 = Frame(master_ch, width=900, height=100)  # ,bg='green'
    frame1.grid(row=0, column=0, columnspan=3, sticky='nsew')

    lblTit = Label(frame1, text="DETALHE FERRAMENTA", font=("Calibri", 16))
    lblTit.pack(fill='both', pady=40, padx=300)

    # FRAME3 / LABELS------------------------
    frame2 = Frame(master_ch, width=300, height=500)
    frame2.grid(row=1, column=0, sticky='nsew')

    Label(frame2, text="CODIGO", width=20, font=(
        "Calibri", 12)).pack(fill='both', ipady=nIPADY)
    Label(frame2, text="DESCRICAO", font=(
        "Calibri", 12)).pack(fill='x', ipady=nIPADY)
    # combo box Fabricante
    Label(frame2, text="FABRICANTE", font=(
        "Calibri", 12)).pack(fill='x', ipady=nIPADY)
    Label(frame2, text="VOLTAGEM DE USO", font=(
        "Calibri", 12)).pack(fill='x', ipady=nIPADY)
    Label(frame2, text="PART NUMBER", font=(
        "Calibri", 12)).pack(fill='x', ipady=nIPADY)

    Label(frame2, text="TAMANHO", font=("Calibri", 12)).pack(
        fill='x', ipady=nIPADY)
    Label(frame2, text="UNIDADE DE MEDIDA", font=(
        "Calibri", 13)).pack(fill='x', ipady=nIPADY)
    Label(frame2, text="TIPO DE FERRAMENTA", font=(
        "Calibri", 12)).pack(fill='x', ipady=nIPADY)
    Label(frame2, text="MATERIAL", font=(
        "Calibri", 12)).pack(fill='x', ipady=nIPADY)

    # FRAME3 / INFO------------------------
    frame3 = Frame(master_ch, width=300, height=500)  # ,bg='white'
    frame3.grid(row=1, column=1, sticky='nsew')

    
    #PONTO DE CONFIGURAÇÃO / LABELs CONSULTA DETALHE
    print('len lsDetalhe...',len(lsDetalhe))
    
    dadosDetalhe = {
        'Codigo':0,
        'Descricao':1,
        'Fabricante':2,
        'Voltagem':3,
        'PartNumber':4,
        'Tamanho':5,
        'Unidade':6,
        'TpFerramenta':7,
        'Material':8
    } 
    Label(frame3, text=lsDetalhe[0], relief=SUNKEN, width=50,
        font=("Calibri", 12)).pack(fill='both', ipady=nIPADY)
    Label(frame3, text=lsDetalhe[1], relief=SUNKEN, font=(
        "Calibri", 12)).pack(fill='x', ipady=nIPADY)
    # combo box Fabricante
    Label(frame3, text=lsDetalhe[2], relief=SUNKEN, font=(
        "Calibri", 12)).pack(fill='x', ipady=nIPADY)
    Label(frame3, text=lsDetalhe[3], relief=SUNKEN,
        font=("Calibri", 12)).pack(fill='x', ipady=nIPADY)
    Label(frame3, text=lsDetalhe[4], relief=SUNKEN, font=(
        "Calibri", 12)).pack(fill='x', ipady=nIPADY)

    Label(frame3, text=lsDetalhe[5], relief=SUNKEN, font=(
        "Calibri", 12)).pack(fill='x', ipady=nIPADY)
    Label(frame3, text=lsDetalhe[6], relief=SUNKEN,
        font=("Calibri", 13)).pack(fill='x', ipady=nIPADY)
    Label(frame3, text=lsDetalhe[7], relief=SUNKEN,
        font=("Calibri", 12)).pack(fill='x', ipady=nIPADY)
    Label(frame3, text=lsDetalhe[8], relief=SUNKEN, font=(
        "Calibri", 12)).pack(fill='x', ipady=nIPADY)

    # FRAME4 / NECESSÁRIO PARA EQUILIBRAR------------------------
    frame4 = Frame(master_ch, width=300, height=500)  # ,bg='yellow'
    frame4.grid(row=1, column=2)

    #Button(master, text="confimar", width=16, height=2, bg="orange",command='').place(x=509, y=544)
    Button(master_ch, text="retornar", width=16, height=2,
        bg="orange", command=master_ch.destroy).place(x=696, y=544)

    # AKI DEBUG
    #master_ch.mainloop()

# AKI DEBUG
#detalheFerramenta()
