# GPT-3 API

This directory contains the code for interacting with the OpenAI GPT-3 API.

## Usage

To use the GPT-3 API, you need to import the `GPT3API` class from the `gpt3_api.py` file and create an instance of the class. You can then use the `generate_text` method to generate text using GPT-3.

Here is an example:


from gpt3_api import GPT3API

gpt3 = GPT3API()

prompt = "Translate the following English text to French: '{}'"
text = "Hello, world!"
response = gpt3.generate_text(prompt.format(text))

print(response)


This will print the French translation of "Hello, world!".

## Requirements

You need to have the `openai` Python package installed to use this code. You can install it with pip:


pip install openai


You also need to set your OpenAI API key as an environment variable named `OPENAI_API_KEY`. You can do this in your shell before running your Python code:


export OPENAI_API_KEY=your-api-key


Replace `your-api-key` with your actual OpenAI API key.