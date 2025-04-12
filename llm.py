# Imports OpenAI model from LangChain & Imports dotenv for managing environment variables
from langchain_openai import OpenAI
from dotenv import load_dotenv

# function loads environment variables from a .env file.
load_dotenv()

# initializing an instance of the OpenAI class.
llm = OpenAI(model='gpt-3.5-turbo-instruct')

str=input("Ask me your question, Please! \n")
# .invoke() method sends a single query to the LLM and gets the response.
# result = llm.invoke("What is the capital of Lakshdweep")
result = llm.invoke(str)
# printing the result
print(result.strip())