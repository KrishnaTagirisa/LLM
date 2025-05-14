from langchain.agents import Tool, initialize_agent, AgentType
from langchain.llms import OpenAI
import re  # Used for extracting clean numbers from messy input strings

# Helper function to extract exactly two integers from the input string
def parse_input(input_str):
    # Find all numeric substrings (e.g., "7", "5", etc.)
    numbers = re.findall(r'\d+', input_str)
    
    # Ensure exactly two numbers are found, or raise an error
    if len(numbers) != 2:
        raise ValueError("Expected exactly two integers.")
    
    # Convert to integers and return
    return int(numbers[0]), int(numbers[1])

# Tool function for addition
def add_numbers(input: str) -> str:
    a, b = parse_input(input)  # Clean and parse input
    return str(a + b)          # Return result as string

# Tool function for multiplication
def multiply_numbers(input: str) -> str:
    a, b = parse_input(input)  # Clean and parse input
    return str(a * b)          # Return result as string

# Define two tools and describe them clearly for the agent
tools = [
    Tool(
        name="AdditionTool",                     # Name the tool
        func=add_numbers,                        # Function to call
        description="Adds two numbers. Input: any text containing two integers (e.g., '7 5')"  # LLM reads this to decide when to use it
    ),
    Tool(
        name="MultiplicationTool",
        func=multiply_numbers,
        description="Multiplies two numbers. Input: any text containing two integers (e.g., '12 10')"
    )
]

# Initialize the language model (OpenAI) with zero temperature (deterministic output)
llm = OpenAI(temperature=0)

# Initialize the agent with tools and a reasoning strategy (Zero-shot ReAct)
agent = initialize_agent(
    tools=tools,                              # Provide our custom tools
    llm=llm,                                  # Language model to use
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  # Type of agent (decides tools from natural language)
    verbose=True                              # Print internal reasoning and tool usage
)

# Ask a complex question; the agent figures out the right order: (7 + 5) * 10
result = agent.run("What is 7 plus 5 multiplied by ten?")

# Print final result
print("\nFinal Answer:", result)
