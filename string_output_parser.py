from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI()

template1 = PromptTemplate(
    template = 'Write a detailed report on a {topic}',
    input_var = ['topic']
)
template2 = PromptTemplate(
    template = 'Write a five line summary on text \n {text}',
    input_var = ['text']
)
parser=StrOutputParser()

chain=template1|model|parser|template2|model|parser

result=chain.invoke({'topic': 'black hole'})

print(result)
