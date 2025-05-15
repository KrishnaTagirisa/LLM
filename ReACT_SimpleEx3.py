from langchain.agents import initialize_agent, Tool, AgentType
from langchain.llms import OpenAI
from dotenv import load_dotenv
import wikipedia
import os

# Load environment variables from .env file
load_dotenv()

# Define the Wikipedia search function
def search_wikipedia(query: str) -> str:
    try:
        return wikipedia.summary(query, sentences=2)
    except Exception as e:
        return f"Wikipedia error: {str(e)}"

# Define a simple calculator
def calculator(expression: str) -> str:
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Calculator error: {str(e)}"

# Tools required for REACT_DOCSTORE: names must be 'Search' and 'Lookup'
tools = [
    Tool(
        name="Search",
        func=search_wikipedia,
        description="Useful for general Wikipedia searches about a topic."
    ),
    Tool(
        name="Lookup",
        func=search_wikipedia,  # reuse same tool for simplicity
        description="Useful for looking up specific facts or definitions on Wikipedia."
    )
]

# Create the OpenAI LLM
llm = OpenAI(temperature=0)

# Initialize the REACT_DOCSTORE agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.REACT_DOCSTORE,
    verbose=True
)

# Run examples
agent.run("What is the square root of the sum of 49 and 51?")
agent.run("What is the capital of the country where the Eiffel Tower is located?")
