## Projeto de certificação M1 - Estácio - Grupo DEV30 / Full Stack
 
 Periodo - 2022.3


### Apresentação 

 Se trata de um projeto voltado para uma aplicação desktop que tem como objetivo criar controle ficticio de aquisição de ferramentas assim como alocação das mesmas para equipes da empresa que fosse adquirir o software 

 Uma particularidade é a de persistência dos dados que devem ser em planilhas excel conforme especificado

 As planilhas de cadastro são 'ferramentes.xlsx','funcionarios.xlsx' e 'solicitacoes.xlsx', estas podem ser removidas que o sistema criará novas porem vazias. As demais são usadas para as listas dos formulários de cadastro.

 Nosso projeto foi desenvolvido seguindo a seguinte visão, autenticação e seleção do modulo (ferramentas,funcionários,solicitações) 

 Outra observação é a de que por trabalharmos em sistemas operacionais diferentes, algumas telas tiveram renderização diferentes, no caso a tela de solicitações vista na gravação no ubuntu renderiza de forma diferente no windows 10. Infelizmente nosso tempo estava muito reduzido pois nosso grupo conseguiu iniciar no dia 31/10 e a entrega em 27//11  onde surgiu uma segunda dificuladade, a disponibilidade individual de tempo para o desenvolvimento que devido estar em função da vida cotidiana de cada um, influenciava diretamente no tempo de resposta e por sua vez nos resultados que estariam definindo os rumos do projeto.

  Sendo assim era necessário primeiro concluir a parte funcional para posteriores reviões 
 
  Outro ponto foi o tentar dar o máximo de embasamento no conhecimento das fontes uitlizadas aos colegas no sentido de 
 acompanharem a evolução do projeto e assim como ter a capacidade de atuarem e compreenderem o codigo. 
 
   Para isso foi criado uma pasta chamada 'estudos' que contem desde testes especificos a funcionalidades como sugestão de 
 links de tutoriais utilizados como base de nosso desenvolvimento.
 
 Acho que esta claro que essa compreensão do que foi feito depende do interesse de cada um.
 
 Por fim a autênticação poderia seguido o principio dos cadastros em planilhas de qualquer formaa, e senha, para fins de desenvolvimento, ficou com usuario 'xxx' e senha '12345'

### Tecnologias utilizadas

Python,tkinter
 
### Requisitos 

Python3.8.10 ou superior

### Bibliotecas

* pip install Pillow
* pip install openpyxl
* pip install reportlab
* pip install tkcalendar

### Executando o projeto

Executar o arquivo main.py

### Definição dos campos
   
    Campos Ferramentas
     
      - codigo : edição livre  (campo unico)
      - descrição : edição livre 
      - fabricante : pré definido em 'listasFerramentas.xlsx' worksheet 'fabricante'   
      - voltagem  : pré definido em 'listasFerramentas.xlsx' worksheet 'voltagem' 
      - part number : edição livre 
      - unidade de medida :pré definido em 'listasFerramentas.xlsx' worksheet 'unidade de medida' 
      - tipo de ferramenta : pré definido em 'listasFerramentas.xlsx' worksheet 'tipo de ferramentas'
      - material : pré definido em 'listasFerramentas.xlsx' worksheet 'material'
               
      obs: a critica e realizada na confirmação onde é exigida a obrigatoriedade de  
           todos os campos assim como a verificado se a chave primaria(campo único) estar repetido
           
    Campos Funcionários 

      - nome completo : edição livre (campo unico) 
      - cpf : edição livre  (campo unico)
      - telefone : edição livre 
      - turno : pré definido em 'listasFuncionarios.xlsx' worksheet 'turno' 
      - equipe : pré definido em 'listasFuncionarios.xlsx' worksheet 'equipes' 
               
      obs: a critica e realizada na confirmação onde é exigida a obrigatoriedade de  
           todos os campos assim como a verificado se a chave primaria(campo único) estar repetido
        
    Campos Solicitações
      
      - nome : pré definido em lista vindo da planilha funcionarios.xlsx 
      - cpf : pré definido em lista vindo da planilha funcionarios.xlsx 
      - equipe : pré definido em lista vindo da planilha funcionarios.xlsx
      - codigo da ferramenta : pré definido em lista vindo da planilha ferramentas.xlsx 
                
      obs: esse campo é verificado na planilha de solicitações afim de saber se a ferramenta 
            ja se encontra alocada ou reservada onde e apresentado com quem está e qual a previsão 
            de entrega ou saida
      
      - data da saida : fornecida por um calendário usando data atual 
      - hora da saida :pré definido em 'listasSolicitacoes.xlsx' worksheet 'horario'
      - data da devolução : fornecida por um calendário usando data atual 
      - hora da devolução : pré definido em 'listasSolicitacoes.xlsx' worksheet 'horario'
     
      obs : no optar por reservar, data da saida e devolução serão acrescidas de um dia considerando a
            data autal 
      
      - motivo : pré definido em 'listasSolicitacoes.xlsx' worksheet 'motivo'
        
### As Consultas 
      
   As consultas ou filtros, são feitas diretamente na respectiva planilha dependendo do assunto. Cada consulta contem 
   filtros especificos por assunto ou seja 
     
     ferramentas : codigo,descricao,fabricante e material
     
     funcionarios : nome,cpf,turno e equipe
     
     solicitações : nome,equipe, codigo da ferramenta e reservada
   
   Todas as funcionalidades de consulta deveriam ter as opçôes de listagens,edição e remoção
   
   obs: no caso da remoção e edição estas deixadas para o final devido a falta de tempo.Com isso tanto a remoção como a edição 
   foram implementadas apenas no módulo de ferramentas onde para ambos os casos, é verificado se existe alguma solicitação podendo 
   a mesma se encontrar alocada ou reservada o que impedirá a operação. 
    

### Video do projeto

https://youtu.be/ECERHzayA5w

 #### 0:07  As planilhas 
     
     Apresentação das planilhas usadas nos cadastros e as de listagens

#### 1:03 Os módulos  
    
    Apresentação dos módulos

#### 1:44 Os cadastros 

    Apresentação da utilização dos combos carregados em função da planilha e realização de um 
     cadastro de funcionários apresentando a critica ao cpf.

#### 3:47 As consultas 
 
    Apresentação da utilização dos filtros e da s listagem do conteudo do grid

#### 5:00 As solicitações

   A realização de um cadastro apresentado a interdependência entre modulos de ferramentas e funcionários. 
   Apresentação do conceito de reserva não permitindo que utilize a data atual. Utilização do filtro
   
 
#### 8:22 Removendo ferramentas 
 
   Apresentação da interdependência entre modulos de ferramentas e solicitações que bloqueia a remoção
  
#### 9:23 Edição de ferramentas  
   
   Apresentação da interdependência entre modulos de ferramentas e solicitações que bloqueia 
   a edição ssim como a critica a edição do codigo que leve a duplicidade.


