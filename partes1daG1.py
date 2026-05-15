



4  Explique como você utilizaria estruturas if para controlar o sistema?
O if será para verificar se ou quando o botão for precionado .
O segundo quando é para classificar a intencidade por exemplo :
tipo led 1 liga (baixa)
led 2 liga (média)
led 3 liga (alto)Você foi contratado para desenvolver a lógica de um sistema automatizado utilizado em uma máquina industrial que realiza um processo contínuo, como mistura ou aquecimento.
O operador controla o sistema por meio de um botão de iniciar. Além disso, o sistema possui dois potenciômetros que influenciam diretamente seu funcionamento.
O primeiro potenciômetro será utilizado para definir o tempo de execução do processo. Esse valor varia de 0 a 1023 e deve ser interpretado pelo sistema como um tempo entre 1 e 10 segundos, em que valores menores representam tempos mais curtos e valores maiores representam tempos mais longos.
Ao pressionar o botão iniciar, o sistema deve ler o valor do potenciômetro de tempo e iniciar o processo. Durante esse período, o LED amarelo deve permanecer aceso, indicando que o processo está em execução. Após o tempo definido, o processo deve encerrar automaticamente, apagando o LED amarelo e acendendo o LED verde, indicando que o ciclo foi finalizado.
Quando o sistema estiver parado, antes de iniciar um novo ciclo, o LED vermelho deve permanecer aceso.
O segundo potenciômetro será utilizado para ajustar a intensidade do processo. Essa intensidade deve ser representada por três LEDs adicionais: um LED aceso indica intensidade baixa, dois LEDs acesos indicam intensidade média e três LEDs acesos indicam intensidade alta.
Durante a execução do processo, o sistema deve indicar a intensidade configurada no momento do início do ciclo. Caso o operador altere os potenciômetros durante a execução, a alteração só será considerada em um novo ciclo.


1  Identifique as entradas e saídas do sistema ?
Entrada
botão 1 para iniciar, 2 potenciômetro (o primeiro é para definir o tempo da execução de 0 a 1023 interpretado como tempo de 1 a 10) o ( segundo potenciômetro vai para definir a intencidade ).
Saída
botão led 1
botão led 2
botão led 3

2 Apresente todos os componentes do sistema e para que eles servem?

inical: botão 1 para iniciar, 2 potenciômetro (o primeiro é para definir o tempo da execução de 0 a 1023 interpretado como tempo de 1 a 10) o ( segundo potenciômetro vai para definir a intencidade ).
SaídaSaídas de luzes: LED Vermelho (Pino 3), LED Amarelo (Pino 4), LED Verde (Pino 5).
Saídas de Intensidades: LED Nível 1 (Pino 6), LED Nível 2 (Pino 7), LED Nível 3 (Pino 8).


EXEMPLO DOIS:
arduino( 1); potenciômetro (2); leds (3); botão para iniciar a operação (1).



3  Apresente as regras de funcionamento a serem implementadas?
Ler o botão se o botão foi apertado irá ler se não vai ficar desligado, depois ver se o potenciômetro 1 está funcionando na parte do tempo , depois vamos para o potenciômetro dois ver se  a intencidade dele está funcinando, 
durante o periodo deve ser vericado se o led amarelo está ligado como até o tempo que foi pedido, se logo em seguida o led verde acender significa que o ciclo está encerrado.
Depois disso, para ser iniciado o novo ciclo deve estar o led vermelho ligado, proximo passo é o segundo potenciômetro será usado para ajustar a intencidade no processo. Nele serão representada nos três leds de dois tipos de intencidade o primeiro led será intencidade baixa mais o segundo e terçeiro leds serão intensidade média.
Mas os três leds no total indiram que sua intensidade é alta.

Led 1 - baixa
Led 2 - média
Led 3 - alta
 OU  SEGUNDO TIPO DE EXPLICAÇÃO
Estado Civil: aonde o sistema irá começar a parado led vermelho em aceso
Ciclo Inicial: que após ser apertado o botão o sistema irá  ler o atual estado do potenciômetro
Tempo: potenciômetro 1 (0-1023)  no caso irá mudar para 1 a 10 segundos
A parte das luzes ou melhor sinalização:tipo led vermelho apaga e o led amarelo liga
FINAL:agora o led amarelo desliga e o led verd irá ligar.



E é claro que não poderá falta os tempos atual, tempo inicial , e tempo final
