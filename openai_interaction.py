from dotenv import load_dotenv
import openai
import os

def generate_response(prompt):
    """
    Generates a response using the OpenAI API based on the provided prompt.
    """
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use "gpt-4" or another available model if you prefer
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=150,
        temperature=0.7
    )
    
    return response.choices[0].message['content'].strip()
