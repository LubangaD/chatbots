import cohere
from dotenv import load_dotenv
import os

def generate_response(prompt):
    """
    Generates a response using the Cohere API based on the provided prompt.
    """
    cohere_client = cohere.Client(os.getenv("COHERE_API_KEY"))
    response = cohere_client.generate(
        model='command-r-plus-08-2024',  # Specify the model you want to use, e.g., 'xlarge'
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,
        k=0,
        stop_sequences=["--"]
    )
    
    return response.generations[0].text.strip()
