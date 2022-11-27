## Projeto de certificação M1 - Estácio - Grupo DEV30 / Full Stack
 
 Periodo - 2022.3


### Apresentação 

 Se trata de um projeto voltado para uma aplicação desktop que tem como objetivo criar controle ficticio de aquisição de ferramentas assim como alocação das mesmas para equipes da empresa que fosse adquirir o software 

uma particularidade é a de persistência dos dados que devem ser em planilhas excel

As planilhas de cadastro são 'ferramentes.xlsx','funcionarios.xlsx' e 'solicitacoes.xlsx', estas podem ser removidas que o sistema criará novas porem vazias. As demais são usadas para as listas dos formulários de cadastro.

Nosso projeto foi desenvolvido seguindo a seguinte visão, autenticação e seleção do modulo (ferramentas,funcionários,solicitações) 

Outra observação é a de que por trabalharmos em sistemas operacionais diferentes algumas telas tiveram renderização diferentes, no caso a tela de solicitações vista na gravação no ubuntu renderiza de forma diferente no windows 10. Infelizmente nosso tempo estava muito reduzido pois nosso grupo conseguiu iniciar no dia 31/10 e a entrega em 27//11  onde surgiu uma segunda dificuladade, a disponibilidade individual do tempo para o desenvolvimento devido a disponibilidade possivel em função da vida cotidiana de cada um o que influenciava diretamente no tempo de resposta contendo resultados que estariam influenciando nas definições do projeto.

Sendo assim era necessário primeiro concluir a parte funcional para posteriores reviões.

Por fim a autênticação que poderia ser um dicionario de usuarios e senha, para fins de desenvolvimento, ficou com usuario 'xxx' e senha '12345'

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
     
      - codigo : edição livre 
      - descrição : edição livre 
      - fabricante : pré definido em lista  
      - voltagem  : pré definido em lista 
      - part number : edição livre 
      - unidade de medida : pré definido em lista 
      - tipo de ferramenta : pré definido em lista 
      - material : pré definido em lista 
         
    Campos Funcionários 

      - nome completo : edição livre (campo unico) 
      - cpf : edição livre  (campo unico)
      - telefone : edição livre 
      - turno : pré definido em lista 
      - equipe : pré definido em lista 
               
       obs: a critica e realizada na confirmação onde é exigida a obrigatoriedade de  
           todos os campos assim como a verificado se a chave primeria estas repetida 
        
   Campos Solicitações
      
      - nome : pré definido em lista vindo da planilha funcionarios.xlsx 
      - cpf : pré definido em lista vindo da planilha funcionarios.xlsx 
      - equipe : pré definido em lista vindo da planilha funcionarios.xlsx
      - codigo da ferramenta : pré definido em lista vindo da planilha ferramentas.xlsx 
                
       obs: esse campo é verificado na planilha de solicitações afim de saber se a ferramenta 
            ja se encontra alocada ou reservada onde e apresentado com quem está e qual a previsão 
            de entrega ou saida
      
     - data de saida
     - hora de saida
     
     - data de devolução
     - hora de devolução
                 No de estar reservadar é apresentada a data da saida podendo ser liberada<br>
                 no caso de queda da reserva<br>
                 <br>
                 - datas de saida e devolução<br> 
               <br>
                 são definidas atravez de calendarios no qual a<br> 
                 data atual já vem selecionada como opção de saida porem no caso de reserva<br> 
                 essa data e acrescida de um dia<br>
                 <br>
                 - horário de saida e devolução<br> 
                
                 são pré definidos em lista<br> 
                 <br>
                 - motivo<br><br> 
                 Pré definido em lista<br> 
                 <br>
              obs: critica é realizada na confirmação onde é exigida a obrigatoriedade de todos os campos<br> 
            <br><br>
              <div class="subtitle">Consultas</div><br>
             
              Ferramentas<br>
              Funcionarios<br>
              Solicitações<br>
              <br><br>
              As consultas ou filtros, são feitas diretamente na planilha   
              dependendo do modulo e os filtros são particulares a cada<br>
              modulo<br>
              <br>
 
              <br>
           obs: todas as funcionalidades de consulta tem opção de<br>
                listagem <br>


### Video do projeto

https://youtu.be/Mtfv4Wa3tLw

