# <p align="center">Protect KO-35 </p>

## 1) Membros da `Equipe 5`:
<br>


- Bruno Maximo
- [Diego Davis (ddm)](https://github.com/diegodvsmelo)
- [Diogo Rodrigues (dsr)](https://github.com/Monkius-Maximus)
- [Júlio Tenório (jclt)](https://github.com/JulioTenorio)
- William 

<br>
     
## 2) Link para repositório git
  
   https://github.com/JulioTenorio/projeto-p1

<br>

## 3) Como rodar o projeto

### Pré-requisitos

Antes de baixar o projeto você vai precisar ter instalado na sua máquina as seguintes ferramentas:

* [Python 3.9 ou superior](https://www.python.org/downloads/)
* [Pygame](https://www.pygame.org/news)

### Em seguida:

```bash
# Clone o repositório
$ git clone https://github.com/JulioTenorio/projeto-p1.git

# Abrir o projeto
Abra a pasta clonada em seu editor de código favorito.

# Iniciar o jogo
Execute o arquivo main.py

# O seu editor de código rodará o jogo em uma nova janela.
```
### Como jogar:

*Utilize o mouse para interagir com o jogo, escolhendo as melhores posições para defender-se dos invasores inimigos durante ondas, nas quais o jogador pode investir em defesas melhores para enfrentar os próximos desafios.
<br>

## 4) A organização do código; 

### <p align="center">Diagrama de blocos </p>
<p align="center">
  <img alt="Diagrama de blocos" src="https://i.imgur.com/DZRj60w.png" width="100%">
</p>

<br>

## 5) Ferramentas, bibliotecas, frameworks utilizados com as respectivas justificativas para o uso;  

- `pygame`: Escolhido pois foi a biblioteca que mais se adequou as capacidades de aprendizado do grupo, com recursos de ensino  e documentação de fácil acesso para sanar dúvidas e bugs que surgem ao longo do desenvolvimento de qualquer atividade.

- `Figma`: Facilita a criação do design dos elementos de interface do jogo, permitindo a criação de um mockup com já as posições definidas dos elementos na tela, sem precisar testar diretamente no código, além de facilitar mudanças necessárias ao decorrer do projeto.

- `kanban`: Organização das atividades de forma visual de quais atividades eram necessárias para a sprint.

- `Aseprite`: Utilizado ao longo do projeto para criar e editar todas as artes do mapa, inimigos e torres, o que nos deu a possibilidade de trabalhar com pixelart, uma estética que se assemelha as antigas obras que nos buscavamos homenagear.  

- `FL Studio`: Utilizado para criarmos e editar os audios/músicas presentes no projeto.

- `Math`: Utilizado para calcularmos as aréas de ataque das torres quando entrava em contato com os colisores dos inimigos.

- `random`: A biblioteca foi utilizada no spawn dos tipos de inimigos para dar dinamismo ao jogo, de forma que pudessemos criar uma gameplay diferente para cada vez que o usuario experimente nossa obra.
<br>

## 6) A divisão de trabalho dentro do grupo (quem fez o que); 

`Diego`: Arte do mapa; implementação do sistema de dinheiro, vida e contagem, HUD e lógica do jogo; inimigos e vetores de direção

`Diogo`: Criação de assets e animação; implementação das torres e sons; 

`Julio`: Organização do Notion e Github; sistemas de mira e tiro; limitação de torres no mapa; criação de HUD, ReadMe

`Bruno`: Criação da apresentação

`William`: Criação da música tema do jogo
 <br>   

## 7) Conceitos que foram apresentados durante a disciplina e utilizados no projeto (indicando onde foram usados);    

Classes e objetos - Utilizamos classes e objetos para representar elementos do jogo, como inimigos e torres.

Herança - Utilizamos herança para criar subclasses de inimigos

Encapsulamento - ¿¿¿no mapa.py?????


<br>

## 8) Os desafios e erros enfrentados no decorrer do projeto e as lições aprendidas. 

Um desafio foi dividir as atividades entre os membros da equipe, além de utilizar algumas ferramentas que não os membros não tinham tanta familiaridade, o tempo reduzido impossibilitou em ter um onboarding para essas ferramentas e metodologias que poderiam ajudar em nossa organização. O erro foi não ter conversado com toda equipe sobre como estava a disponibilidade de tempo, e a familiaridade com as ferramentas que iriamos utilizar. Além de conhecer melhor a estrutura base do que queriamos construir, visto que em momentos por cada um estar focado em conlcuir uma determinada tarefa gastamos tempo desenvolvendo recursos e funcionalidades que não chegaram a nossas versões finais devido a dificuldade de implementar e documentar todas elas no prazo que tinhamos. O aprendizado que fica é que devemos buscar uma comunicação assertiva o mais cedo possivel no projeto, além de como tempo é essencial para um melhor entendimento e desenvolvimento das habilidades.
 <br>

## 9) Qual foi o maior erro cometido durante o projeto? Como vocês lidaram com ele? 

Não ter feito o mapa utilizando de ferramentas que gerassem dados que auxiliariam na posição, como por exemplo o Tiled. Isso dificultou a implementação de sistemas como a limitação da posição das torres, posição relativa à outras torres, e tudo que precisamos ter posição relativa a outro objeto. Conseguimos contornar esse problema utlizando Pitagoras para calcular a distância entre dois objetos, o que se mostrou funcionar por um bom tempo, mas ao termino do projeto percebemos como isso dificultou, e até mesmo impossibilitou de implementar algumas funções no nosso jogo.

<br>

## 10) Qual foi o maior desafio enfrentado durante o projeto? Como vocês lidaram com ele? 

 De maneira geral, podemos dizer que foi a Conciliação do projeto com outras disciplinas, especialmente na segunda metade do período e nossa vida pessoal/ profissional, visto que a maioria dos integrantes do grupo trabalham ou estão inseridos em atividades extra curriculares nos contra turnos da cadeira, os principais momentos que tinhamos para estudar os coceitos de Programação Orientada a Objetos e aprender autilizar ferramentas e bibliotetcas novas do pygame, e produzirmos o jogo, seria nos finais de semana e nos intervalos entre uma atividade e outra.

<br>        

## 11) Quais as lições aprendidas durante o projeto? 

`Bruno`:

`Diego`: Gestão de tempo, planejamento e trabalho em equipe. São os pilares de qualquer projeto bem feito, o nosso pecou em alguns desses aspectos mas conseguimos nos sobrepor a eles, mas sem duvidas me ensinou a antes de começar a fazer o trabalho em si, organizar bem cada um desses aspectos.

`Diogo`: Dificil de dizer apenas uma, mas eu diria que o projeto apenas serviu para me mostrar a importância do trabalho em equipe, planejamento e comunicação, tendo em vista que durante todo o processo eu pude experimentar as diversas etapas de desenvolvimento de um produto e as dificuldades de se conciliar as expectativas com aquilo que temos de recursos disponiveis no momento, seja isso mão de obra, tempo ou conhecimento, com aquilo que vamos conseguir concluir no prazo determinado. Além disso esse projeto me ajudou a melhor me relacionar com a turma e com os monitores em momentos em que eu pensei em desistir da disciplina, porém a ajuda e o empenho dos mesmos me forneceu um gás para permanecer tentando.

`Júlio`:

`William`:

 <br>
 <br>

## 12) Capturas de tela do sistema funcionando para compor a galeria de projetos 

<p align="center">
  <img alt="Sistema Funcionando" src="https://imgur.com/a/b6IdTHf" width="100%">
</p>

<br>
