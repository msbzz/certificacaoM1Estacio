Apresentação
------------

  Certificação mundo 1

Nome do grupo
-------------

  Dev team 30 

Ano periodo
------------ 
  2022.3 full stack

Integrantes
-----------
  Ricardo Alves dos Santos Junior
  Renan Matheus Linhares Abrantes
  Mateus Felipe Alves Martins
  Juliano Jeremias Guarizzo
  Marco Sergio Albino Vittorio Barozzi
  Fernanda Guimarães Vargas
  Fábio Henrique Morales Prado

Cronologia da formação do grupo
----------------------------------  
  dia 26/10
     sai a lista v5 com o grupo
   
  dia 30/10   
    Ricardo entra em contato
    
    formação do grupo
      
  dia 31/10  
    Fernanda é realocada e entra no grupo
     
  dia 03/11
    Fabio encontra o grupo
   
  dia 06/11
      Renan encontra o grupo
       
  dia 21/11
     Mateus Felipe encontra o grupo     
      
Distribuição de tarefas e dificuldades
---------------------------------------  
  
    A primeira dificuldade foi o conciliar o conhecimento experiencia em resoluções de problemas para poder identificar 
  o nivel de tarefas a serem distribuidas
   
    Sendo assim achei valido isolar as tarefas para depois integra-las como um todo explicando posteriormente sua utilização através de
  links usados como estudo dos problemas em questão e assim como sanar qualquer duvida sobre o desenvolvimento.  
  
    A segunda dificuladade foi a disponibilidade individual do tempo para o desenvolvimento considerando o primeiro
  item de dificuladade juntamente a disponibilidade de tempo em função da vida cotidiana de cada um o que influenciava
  diretamente no tempo de resposta contendo resultados que influenciariam na definição do projeto.
  
    Finalmente,nenhum de nós tinha expericiencia em python tkinter e a tentaviva de optar por uma ferramentas de interface grafica
  não obteve sucesso devido ao tempo de aprendizagem juntamente com a reformulação do que estava pronto. Isso nos fez optar por
  continuar a usar recursos nativos.
  
    Sendo assim existem pontos não concluidos do projeto como falta de icones e imagens proprias dos formulários, layout de relatório,
  explorar mais eventos para reduzir o numero de click entre outros.No mais, acredito que com um pouco mais de tempo, tudo poderiamos ter 
  sido concluido ou mesmo melhorado. 

    Umas ultimas observações são as de que, optamos em determinado ponto em compartilhar arquivos tambem por e-mail por motivo de falta 
  de conhecimento no manuseio do gitHub. Tambem optamos por usar como canal de comunicação o grupo do whatsapp já que não tinhamos muito 
  tempo para nos reunirmos nem como consolidar horários.  
  
    Por fim achamos essa forma mais produtiva. 
  
  Para concluir fica aqui o agradecimento a todos pelo empenho.

Requisitos
-----------
python,tkinter

instalação das bibliotecas tkcalendar e openpyxl
  

Estrutura de arquivos utilizados na persistencia dos dados
--------------------------------------------------------------  
  Arquivos excel na persistencia assim como base de informações disponibilizadas
  pelas listas (combobox)
  
  obs: planilhas nomeadas como listas são as usadas como base para o combobox

Estrurura do projeto
---------------------
  Apresentação dos modulos desenvolvidos e integrados
  para confecção do projeto como um todo
  

Funcionalidades 
-------------- 

cadastro 
 --------   
    Ferramentas
    
      codigo - edição livre
      descrição - edição livre
      fabricante - pré definidos em lista
      voltagem  - pré definidos em lista 
      part number - edição livre
      unidade de medida - pré definidos em lista
      tipo de ferramenta - pré definidos em lista 
      material - pré definidos em lista
      
    Funcionários
      
      nome completo - edição livre
      cpf - edição livre
      telefone - edição livre
      turno- pré definidos em lista
      equipe- pré definidos em lista
    
    obs: a critica e realizada na confirmação onde é exigida a obrigatoriedade de 
        todos os campos assim como a verificado se a chave primeria estas repetida
    
	    ferramentas
	      codigo
	    
	    funcionario
	      nome e cpf 

   Solicitações
     
     nome,cpf e equipe	      
       No caso desses campos, a informação vem diretamente da planilha
       de funcionários onde selecionando por cpf ou nome os demais campos são preenchidos
   
       ex:
        cpf traz nome e equipe
        nome traz cpf é equipe
   
     codigo da ferramente 
     
       vem da planilha de ferramentas onde após selecionada
       é verificado dentro da planilha de solicitações se a ferramenta ja se
       encontra alocada apresentado com quem está e qual a previsão de entrega.
       
       No de estar reservadar é apresentada a data da saida podendo ser liberada
       no caso de queda da reserva
   
     datas de saida e devolução 
       
       são definidas atravez de calendarios no qual a 
       data atual já vem selecionada como opção de saida porem no caso de reserva 
       essa data e acrescida de um dia
   
     horário de saida e devolução 
     
       são pré definidos em lista 
   
     motivo 
     
       Pré definido em lista 
     
    obs: critica é realizada na confirmação onde é exigida a obrigatoriedade de todos os campos 
  
  consultas
  ---------    
    Ferramentas
    Funcionarios
    Solicitações
    
    As consultas ou filtros, são feitas diretamente na planilha 
    dependendo do modulo e os filtros são particulares a cada
    modulo
    
    Ferramentas
    Funcionários
    Solicitações
     
 
 obs: todas as funcionalidades de consulta tem opção de
      listagem 
