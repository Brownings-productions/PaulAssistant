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
  stream = chat(
    model=Model,
    messages=messages + [{'role': 'user', 'content': user_input},],
    stream=True,
  )
  messages.append({'role': 'user', 'content': user_input})
  
  totalResponse = ' '

    # Add the response to the messages to maintain the history
  for chunk in stream:
    
    totalResponse += ' ' + chunk.message.content
        
    print(chunk.message.content, end='', flush=True)	
  messages.append({'role': 'assistant', 'content': totalResponse})
  print('\n')





