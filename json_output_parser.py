from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI()
parser=JsonOutputParser()

template = PromptTemplate(
    template = 'Write a detailed report on a {topic}\n {format_instruction}',
    input_var = ['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain=template | model | parser

result=chain.invoke({'topic': 'black hole'})

print(result)
