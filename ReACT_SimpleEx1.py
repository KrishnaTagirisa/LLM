# This is a simple ReACT agent that uses a calculator and a knowledge base to answer questions.
# =============================================================================================

# Define a simple calculator tool that evaluates math expressions
def calculator(expression):
    try:
        return str(eval(expression))  # Use Python's eval to compute the result
    except:
        return "Error"  # If something goes wrong, return "Error"

# Define a basic knowledge base lookup tool
def knowledge_base_lookup(query):
    # A small hardcoded "knowledge base" (like a mini search engine)
    knowledge = {
        "Eiffel Tower is located in": "France",
        "Capital of France": "Paris",
        "Capital of Germany": "Berlin",
    }
    # Return the answer if the query exists in the knowledge dictionary
    return knowledge.get(query, "Unknown")

# Main ReACT agent function that takes a question and tries to answer it
def react_agent(question):
    print(f"Question: {question}")
    
    # Check if it's a math-based question
    if "square root" in question:
        # Step 1: Think about what needs to be done
        print("Thought: I need to add 49 and 51 first.")
        
        # Step 2: Use the calculator tool to compute 49 + 51
        total = calculator("49 + 51")
        print(f"Action: calculator('49 + 51') → {total}")

        # Step 3: Think again – now we take the square root of the result
        print(f"Thought: Now I need the square root of {total}.")
        
        # Step 4: Use the calculator tool again for square root
        result = calculator(f"{total}**0.5")  # **0.5 is how you calculate square root in Python
        print(f"Action: calculator('{total}**0.5') → {result}")

        # Step 5: Final answer
        print(f"Final Answer: {result}")

    # Check if it's a knowledge-based question involving Eiffel Tower
    elif "Eiffel Tower" in question:
        # Step 1: Think – find which country the Eiffel Tower is in
        print("Thought: I need to know which country the Eiffel Tower is in.")
        
        # Step 2: Use the knowledge base tool
        country = knowledge_base_lookup("Eiffel Tower is located in")
        print(f"Action: knowledge_base_lookup('Eiffel Tower is located in') → {country}")

        # Step 3: Think – now we want the capital of that country
        print(f"Thought: Now I need to know the capital of {country}.")
        
        # Step 4: Use the knowledge base tool again
        capital = knowledge_base_lookup(f"Capital of {country}")
        print(f"Action: knowledge_base_lookup('Capital of {country}') → {capital}")

        # Step 5: Final answer
        print(f"Final Answer: {capital}")

    # If the question doesn't match our logic
    else:
        print("Sorry, I don't know how to solve that yet.")

# Run the first example: math problem
react_agent("What is the square root of the sum of 49 and 51?")
print("\n" + "-"*50 + "\n")  # Just for visual separation

# Run the second example: knowledge question
react_agent("What is the capital of the country where the Eiffel Tower is located?")
