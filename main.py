# Import necessary libraries
import streamlit as st

# Import the restaurant name and item generator function from a custom module
from NameGenerator import generate_restaurant_name_and_items

# Set the title of the Streamlit app
st.title("Restaurant Name Generator")

# Load and display an image
image_path = "image.jpg"  # Path to the image file
image = open(image_path, 'rb').read()  # Open the image file in binary-read mode
st.image(image, use_column_width=True)  # Display the image with column width adjustment

# List of famous global cuisines
famous_cuisines = [
    "Italian",    
    "Chinese",
    "Indian",     
    "French",     
    "Japanese",    
    "Mexican",     
    "Thai",      
    "Spanish",
    "Turkish",
    "Greek",
    "Moroccan", 
    "Vietnamese",
    "Korean",
    "Brazilian",
    "Ethiopian"
]

# Create a sidebar select box for choosing a cuisine
cuisine = st.sidebar.selectbox("Pick a cuisine", famous_cuisines)

# Check if a cuisine has been selected
if cuisine:
    # Generate restaurant name and menu items based on the selected cuisine
    response = generate_restaurant_name_and_items(cuisine)

    # Display the generated restaurant name
    st.header(response['restaurant_name'])

    # Split the string of menu items into a list and display them
    menu_items = response['menu_items'].split(',')

    # Display a header for menu items
    st.write("*Menu Items:*")

    # Iterate through the list of menu items and display each item
    for item in menu_items[1:]:  # Start from the second item to skip any leading empty strings
        st.write('- ' + item)  # Display each item as a bullet point
