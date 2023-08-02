import openai
import os
import dotenv

dotenv.load_dotenv()

openai.api_key = os.environ.get('OPENAI_API_KEY')

role = '' # How you want to answer the question. example: 'I am a doctor'

prompt = '' # The question you want to ask. example: 'How many years the elephant lives?'

messages = [{ 'role' : 'system', 'content' : role },
           { 'role' : 'user', 'content' : prompt}]

# Change the model to your desired model. example: 'davinci'

# max_tokens = 200 # The maximum number of tokens to be generated. example: 100

response = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=messages, max_tokens=200)

#  It prints the generated answer and the number of tokens used.

print (str(response.choices[0].message.content), f'  Used Tokens : {str(response.usage.total_tokens)}')