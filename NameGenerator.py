# Import necessary modules from various libraries
from authenticator import google_api_key  # Import the Google API key from the authenticator module
from langchain_google_genai import GoogleGenerativeAI  # Import the Generative AI interface for Google models
from langchain_core.prompts import PromptTemplate  # Import the PromptTemplate class for creating custom prompts
from langchain.chains import LLMChain  # Import the LLMChain for chaining prompt templates and models

# Initialize a Google Generative AI model with specified parameters
llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=google_api_key, temperature=1)

# Define a function to generate a restaurant name and a list of menu items based on the cuisine type
def generate_restaurant_name_and_items(cuisine):
    # Generate a restaurant name using a templated prompt based on the cuisine type
    prompt_restaurant_name = PromptTemplate(input_variables=["cuisine"], template="I want to open a restaurant for {cuisine} food. Suggest me only one fancy name for this.")
    restaurant_name_llm = prompt_restaurant_name | llm  # Chain the prompt template with the language model
    rn = restaurant_name_llm.invoke({'cuisine': cuisine})  # Invoke the chain to generate a restaurant name
    
    # Generate a list of menu items using a templated prompt based on the generated restaurant name
    prompt_menu_items = PromptTemplate(input_variables=["restaurant_name"], template="Give me a list of 20 items for {restaurant_name}. Just return food item names as a comma separated list. Make sure it is a comma-separated values and not anything else.")
    menu_items_llm = prompt_menu_items | llm  # Chain the prompt template with the language model
    menu_items = menu_items_llm.invoke({'restaurant_name': rn})  # Invoke the chain to generate a list of menu items

    # Return both the restaurant name and the menu items as a dictionary
    return {'restaurant_name': rn, 'menu_items': menu_items}

# Main execution block to test the function with 'Indian' cuisine
if __name__ == "__main__":
    # Print the output of the function
    print(generate_restaurant_name_and_items('Indian'))
