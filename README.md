## Como essas ferramentas são criadas?

Você já se perguntou como essas novas ferramentas de inteligência artificial são criadas?

Seja o ONM.AI, seja o Hotmart.AI ou alguma outra nova ferramenta?

Bom, para pessoas que não são profissionais da área, ou pelo menos que não possuem um conhecimento um pouco mais técnico a respeito, podem achar que é um bicho de umas 17 cabeças hahahahah.

Mas a verdade é que é bem simples. E eu mostrarei, hoje, como você pode ter uma inteligência artificial dessa bem na sua casa.

## O que é o Hotmart.AI?

O Hotmart AI nada mais é que uma ferramenta onde você escreve o nicho do seu produto. Observe a imagem abaixo: 

<img src="https://i.ibb.co/CvLdMqT/image-3.png">

Note o quão fácil é. Você digita o seu nicho e pronto! Ele te retorna um plano de curso e estratégias de vendas, como você pode ver abaixo:

<img src="https://i.ibb.co/C8C8qrd/image-4.png">
<img src="https://i.ibb.co/k2Fj545/image-5.png">

Pela qualidade da resposta, você pode pensar que é uma ferramenta muito complexa. Mas, na verdade, você consegue replicá-la com 30 linhas de código (ou até menos).

## Como refiz essa inteligência artificial?

<img src="https://i.ibb.co/t8bJjYm/image-6.png">

A maioria das novas ferramentas de IA que vocês veem por aí são, na verdade, uma adaptação (seja um fine-tuning ou um modelo que possui um prompt pré-definido) do modelo desenvolvido pela OpenAI (GPT-3.5 ou GPT-4). 

Pois é… é só isso! Tanto o Hotmart AI quanto (muito provavelmente) o ONM AI utilizam os modelos da OpenAI com um prompt pré definido para gerar essas respostas. E foi justamente isso que eu fiz!

Observe o resultado da minha própria IA, que é uma réplica do Hotmart AI:

<img src="https://i.ibb.co/4RLTKNW/image-9.png">

Esses foram apenas 2 de 5 capítulos com os tópicos detalhados pela IA do que deve ter em cada capítulo do curso / e-book. Além disso, ele gera toda uma estratégia de marketing. Observe as imagens abaixo:

<img src="https://i.ibb.co/hY5qggb/image-8.png">

<img src="https://i.ibb.co/K9m8rCv/image-7.png">

## Behind the scenes

Agora, chegou o momento em que eu vou te mostrar, sem esconder nada, o que está por trás disso tudo.

Basicamente, utilizei duas bibliotecas bem conhecidas da linguagem de programação Python para fazer essa aplicação: streamlit e langchain.

 O streamlist é o responsável por fazer todo o layout, ele meio que “cria um site” para podermos testar nossa aplicação localmente. Enquanto o Langchain é o responsável pela inteligência por trás de cada prompt e modelo.

Para acessar o código completo, basta clicar no link abaixo:

https://github.com/anwarhermuche/hotmartai_clone/blob/main/main.py
