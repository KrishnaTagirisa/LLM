# Import ChatOpenAI model from LangChain's OpenAI integration
# Import PromptTemplate to define custom prompts
# Import output parser to convert model output to plain strings
# Import building blocks for chaining operations
# Import dotenv to load environment variables (like API keys) from a .env file

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableLambda, RunnablePassthrough, RunnableParallel
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Define a simple Python function to count words in a text
def word_count(text):
    return len(text.split())

# Create a prompt template that asks the model to write a joke about a given topic
prompt = PromptTemplate(
    template='Write a joke about {topic}',  # Prompt with a placeholder
    input_variables=['topic']              # Declare the placeholder variable
)

# Initialize the OpenAI language model (default GPT model via LangChain)
model = ChatOpenAI()

# Set up a parser to convert the model's response into a plain string
parser = StrOutputParser()

# Create a sequential chain: prompt → model → output parser
joke_gen_chain = RunnableSequence(prompt, model, parser)

# Set up a parallel chain:
# - 'joke' just passes through the model's output
# - 'word_count' computes the number of words in the joke
parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),          # Pass the joke through unchanged
    'word_count': RunnableLambda(word_count) # Apply the word count function
})

# Combine both chains in sequence: generate a joke first, then compute the word count in parallel
final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

# Invoke the chain with a topic ("AI")
result = final_chain.invoke({'topic': 'AI'})

# Format the final result with the joke and its word count
final_result = """{} \n word count - {}""".format(result['joke'], result['word_count'])

# Print the final output
print(final_result)
