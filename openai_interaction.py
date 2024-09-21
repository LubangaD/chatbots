import openai

def generate_response(prompt):
    """
    Generates a response using the OpenAI API based on the provided prompt.
    """
    openai.api_key = "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"  # Replace with your OpenAI API key
    
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
