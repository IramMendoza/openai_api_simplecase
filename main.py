import openai
import os
import dotenv

dotenv.load_dotenv()

openai.api_key = os.environ.get('OPENAI_API_KEY')

messages = [{ 'role' : 'system', 'content' : 'Eres un desarrollador senior'},
           { 'role' : 'user', 'content' : '¿Es cierto que python es un lenguaje relativamente lento?'}]

response = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=messages, max_tokens=200)

print (str(response.choices[0].message.content), f'  Tokens utilizados : {str(response.usage.total_tokens)}')