
from dadosXLSX import Dados
 
c=Dados()
 

"""

unidade de medida
tipo de ferramentas
material
     
"""
#ls=['a','b','c']
#c.createInsertXLSX('testesPlanilha.xlsx','teste1',ls)


#print(c.getList('listasdeferramentas.xlsx','fabricante'))
#print(c.getList('listasdeferramentas.xlsx','tipo de ferramentas'))
#print(c.getList('listasdeferramentas.xlsx','material'))
#print(c.getList('listasdeferramentas.xlsx','unidade de medida'))

lscab=['a','b','c','d','e','f','g']

ls1=c.OpenReadXLSX('ferramentas.xlsx','ferramentas',lscab)
print(ls1)
 
 
 