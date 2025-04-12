from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI()

class Person(BaseModel):
    name: str = Field(description='Name of the person')
    age: int = Field(description='Age of the person')
    city: str = Field(description='Name of the city the person belongs to')

parser = PydanticOutputParser(pydantic_object=Person)

template=PromptTemplate(
    template='generate the Name, age and city of a fictional {place} person \n {format_instruction}',
    input_var=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'place': 'Bapatla'})
print(result)

