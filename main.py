import streamlit as st
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
import tiktoken
encoding = tiktoken.encoding_for_model("gpt-3.5-turbo-instruct")
load_dotenv()
import os

def lista_to_html(lista, keyword):
    html = f"<h1>Plano de curso para: {keyword.title()}</h1><br>"
    for item in lista:
      html += f"<h2>{item['capitulo']}</h2><br>"
      html += "<ul>"
      for topico in item['topicos']:
        html += f"\t<li> {topico}\n"
      html += "</ul><br>"

    return html

os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")

st.image("imagem.jpg", use_column_width=True)
st.title("Anwar's AI")

keyword = st.text_input(label = "O que você quer construir? Coloque abaixo o tema do seu produto e iremos sugerir estratégias de vendas e um plano de curso para o seu produto.", placeholder = "Aprenda a tocar piano, noções básicas de culinária, redes sociais para negócios...")
submit = st.button(label = "Enviar")


if keyword and submit:
  prompt = PromptTemplate(
    input_variables = ["nicho"],
    template = "A partir de um nicho específico entre crases triplas, quero que retorne uma estrutura de um curso completo que ela pode vender na internet sobre aquele determinado nicho. O curso deve ser separado em capítulos e tópicos. Teremos de 3 a 5 capítulos, onde cada capítulo terá de 4 a 6 tópicos específicos. Os tópicos devem ser muito bem detalhados, com o que será dito naquele tópico em específico e o que a pessoa será capaz de fazer ao finalizá-lo. Retorne uma lista com 3 a 5 dicionários dentro. Os dicionários terão as chaves 'capitulo' (lembre-se de colocar as aspas na chave), com o título do capítulo, e 'topicos' (lembre-se de colocar as aspas na chave), com uma lista com a descrição de cada tópico. Com isso, retorne uma lista para o nicho: ```{nicho}```"
  )

  prompt = prompt.format(nicho = keyword)
  tokens = encoding.encode(prompt)
  llm = OpenAI(temperature = 0, max_tokens = 4000 - len(tokens))

  lista = eval(llm(prompt))

  html = lista_to_html(lista, keyword)

  st.markdown(html, unsafe_allow_html=True)
  
  prompt_estrategia = PromptTemplate(
    input_variables = ["nicho"],
    template = "A partir de um nicho específico entre crases triplas, quero que retorne um plano com estratégias de vendas para o infoproduto com esse determinado nicho. A estratégia de vendas deve ser bem detalhada, com a persona, as estratégias de marketing, sugestões de calendários e linhas editoriais etc.. Seja bem específico e dê o máximo de informações possível. No final, dê sugestões de preço para o infoproduto e diga o motivo do preço. O preço, se for um curso em vídeo, varia entre 397 a 1997 reais, dependendo da complexidade do assunto. Se for um e-book, de 37 até 97 reais. O nicho é: ```{nicho}```"
  )
  prompt = prompt_estrategia.format(nicho = keyword)
  tokens = encoding.encode(prompt)
  llm = OpenAI(temperature = 0, max_tokens = 4000 - len(tokens))
  markdown = "<h1>Estratégia de vendas</h1>" + llm(prompt)

  st.markdown(markdown, unsafe_allow_html = True)


  