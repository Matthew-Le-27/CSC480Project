import openai
import dotenv
import os

dotenv.load_dotenv() 
openai.api_key = os.getenv("OPEN_API_KEY")

chat_history = []

def chat_with_AI(prompt):
    response = openai.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")

        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Chatbot: Goodbye!")
            break

        response = chat_with_AI(user_input)
        print("Chatbot: ", response)

# ADDITIONAL COMMENTS
# - On line #20, the "You: " inside of the 'input()' command should be changed to whoever the bot is talking to in the terminal.