#import libraries
from ollama import chat
from ollama import ChatResponse 
from ollama import pull
import json

#Memory storage
messages = [{"role": "user", "content": "You are a helpfull assistant named Paul. you will opperate like the assistent "
"jarvis from the iron man movie's. ceep it brief and smooth. dont overdo it"}, 
{"role": "assistant", "content": "Hello, how can I help you today?"},]

#define model
Model = 'llama3.2'

#Downloads repository model from ollama
pull(Model)

while True:
  user_input = input()
  response = chat(
    model=Model,
    messages=messages + [{'role': 'user', 'content': user_input},],
  )
  # Add the response to the messages to maintain the history
  messages.append({'role': 'user', 'content': user_input})
  messages.append({'role': 'assistant', 'content': response.message.content})
  
  print(response.message.content + '\n')