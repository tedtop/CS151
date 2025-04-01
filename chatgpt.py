import openai
import os

# Set up the OpenAI API key
openai.api_key = "[OPENAI_API_KEY]"

# Function to ask ChatGPT a question
def ask_chatgpt(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ],
        max_tokens=150,
        temperature=0.7
    )
    return response.choices[0].message['content']

# Main program
if __name__ == "__main__":
    user_question = input("Please enter your question: ")
    answer = ask_chatgpt(user_question)
    print(f"ChatGPT: {answer}")