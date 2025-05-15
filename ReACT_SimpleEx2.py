import wikipedia  # Import the Wikipedia API library

# TOOL 1: Calculator Tool
def calculator(expression):
    """
    This tool evaluates basic math expressions.
    WARNING: Using eval() is dangerous in untrusted environments.
    """
    try:
        return str(eval(expression))  # Calculate and return result as string
    except Exception as e:
        return f"Calculator Error: {str(e)}"  # Return error if something goes wrong

# TOOL 2: Wikipedia Lookup Tool
def wiki_lookup(query):
    """
    This tool fetches a brief summary from Wikipedia for a given topic.
    """
    try:
        # Get a short (2-sentence) summary of the topic
        summary = wikipedia.summary(query, sentences=2)
        return summary
    except Exception as e:
        return f"Wikipedia Error: {str(e)}"  # Handle cases like no page found

# Main ReACT agent function
def react_agent(question):
    print(f"Question: {question}")  # Show the question

    # CASE 1: If question is about square roots (math-based)
    if "square root" in question:
        # Step 1: Reasoning
        print("Thought: I need to calculate the sum and then find the square root.")

        # Step 2: Action – perform 49 + 51
        sum_expr = "49 + 51"
        total = calculator(sum_expr)
        print(f"Action: calculator('{sum_expr}') → {total}")

        # Step 3: Reasoning – now calculate the square root
        sqrt_expr = f"{total}**0.5"  # Square root using exponent 0.5
        result = calculator(sqrt_expr)
        print(f"Action: calculator('{sqrt_expr}') → {result}")

        # Step 4: Final answer
        print(f"Final Answer: {result}")

    # CASE 2: If the question mentions "Eiffel Tower" (knowledge-based)
    elif "Eiffel Tower" in question:
        # Step 1: Thought – find out where the Eiffel Tower is
        print("Thought: I need to know which country the Eiffel Tower is in.")

        # Step 2: Action – use Wikipedia to get info
        info = wiki_lookup("Eiffel Tower")
        print(f"Action: wiki_lookup('Eiffel Tower') →\n{info[:200]}...")  # Show first 200 chars

        # Step 3: Final response
        print("Final Answer: This information was retrieved from Wikipedia.")

    # CASE 3: For other general knowledge questions
    else:
        print("Thought: Let me try to find general information using Wikipedia.")

        # Try searching Wikipedia directly
        info = wiki_lookup(question)
        print(f"Action: wiki_lookup('{question}') →\n{info[:200]}...")  # Show a brief preview
        print("Final Answer: This information was retrieved from Wikipedia.")

react_agent("What is the square root of the sum of 49 and 51?")
react_agent("What is the capital of the country where the Eiffel Tower is located?")
