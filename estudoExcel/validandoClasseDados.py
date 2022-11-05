
from dadosXLSX import Dados
 
c=Dados()
 

"""

unidade de medida
tipo de ferramentas
material
     
"""

print(c.getList('listasdeferramentas.xlsx','fabricante'))
#print(c.getList('listasdeferramentas.xlsx','tipo de ferramentas'))
#print(c.getList('listasdeferramentas.xlsx','material'))
print(c.getList('listasdeferramentas.xlsx','unidade de medida'))
 
 