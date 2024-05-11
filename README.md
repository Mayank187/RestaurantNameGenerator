# Restaurant Name and Menu Generator

Welcome to the repository for the Restaurant Name and Menu Generator, a web-based application designed to generate unique restaurant names and corresponding menu items based on selected global cuisines. This project leverages advanced AI technologies to provide creative and tailored outputs that can inspire entrepreneurs and restaurateurs.

## Overview

The project is divided into two primary components:

1. **main.py**: This is a Streamlit-based web application that serves as the user interface. Users can interact with the application to select a cuisine and receive a generated restaurant name and a list of menu items.
2. **NameGenerator.py**: This script houses the core logic for generating restaurant names and menu items. It utilizes Google's Generative AI models via the LangChain library.

## Detailed Description

### main.py

This script is the front end of our application, built using Streamlit, which allows for rapid prototyping of web apps for machine learning and data science projects. Here's what each part of the script does:

- **Imports**: Essential libraries are imported, including Streamlit for the web app, and functions from `NameGenerator.py`.
- **Title and Image Display**: The Streamlit app's title is set, and an image representative of the application is displayed.
- **Cuisine Selection**: Users can choose from a predefined list of world cuisines via a dropdown menu in the sidebar.
- **Output Display**: Once a cuisine is selected, the script calls the generator function to produce a restaurant name and menu items, which are then displayed on the page.

### NameGenerator.py

This module is the backbone of the application, handling the generation of restaurant names and menu items:

- **Imports and Model Initialization**: The script imports necessary modules from the LangChain library and initializes a Google Generative AI model.
- **Function `generate_restaurant_name_and_items`**: 
  - **Restaurant Name Generation**: Utilizes a templated prompt that incorporates the selected cuisine to generate a restaurant name.
  - **Menu Item Generation**: Generates a list of menu items using another templated prompt that ensures the outputs are formatted as a comma-separated list.
- **Main Block**: Contains a test block that can be used to run the generator function independently for debugging or development purposes.

## Installation

### Prerequisites

- Python 3.8+
- Access to the internet to install packages and run Streamlit.

### Setup

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Mayank187/RestaurantNameGenerator.git
cd RestaurantNameGenerator
pip install -r requirements.txt
