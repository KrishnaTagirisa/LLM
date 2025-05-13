import os
# Install required packages (this would be run in a notebook or shell)
# !pip install -q langchain-openai langchain-core requests

# Import required modules from LangChain and requests
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import requests

# function loads environment variables from a .env file.
load_dotenv()

# Set your OpenAI API key as an environment variable
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Define a tool using LangChain's @tool decorator
@tool
def multiply(a: int, b: int) -> int:
  """Given 2 numbers a and b this tool returns their product"""
  return a * b

# Test the tool directly by invoking it with arguments
print(multiply.invoke({'a': 3, 'b': 4}))  # Expected output: 12

# Initialize the OpenAI chat model (using default model like gpt-3.5 or gpt-4)
llm = ChatOpenAI()

# Bind the tool to the LLM so that it can decide when to use it
llm_with_tools = llm.bind_tools([multiply])

# Try invoking the model with a basic greeting
llm_with_tools.invoke('Hi how are you')  # Just a warm-up test, no tool usage expected here

# Create a message where the user is asking to multiply 3 and 1000
query = HumanMessage('can you multiply 3 with 1000')
messages = [query]
print("\n Plain given query: ", messages)

# Invoke the LLM with the query. It should recognize the need to use the 'multiply' tool.
result = llm_with_tools.invoke(messages)
messages.append(result)
print("\n Plain given query with result: ", messages)

# Extract the tool call from the result and manually invoke the tool with the parsed parameters
tool_result = multiply.invoke(result.tool_calls[0])
messages.append(tool_result)

# Invoke the LLM again with the updated conversation that now includes the tool result
# This gives the LLM a chance to respond in natural language using the result
print(llm_with_tools.invoke(messages).content)
