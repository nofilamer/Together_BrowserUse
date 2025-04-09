from dotenv import load_dotenv
from together import Together

# Load environment variables from .env file
load_dotenv()

# Initialize the Together client
client = Together()

# Define a simple user message
user_message = {'role': 'user', 'content': 'Who is the president of Pakistan?'}

# Create a chat completion request
stream = client.chat.completions.create(
	model='meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo',
	messages=[user_message],
	stream=True,
)

# Print the response from the model
for chunk in stream:
	print(chunk.choices[0].delta.content or '', end='', flush=True)

# hello this is a test to check commit\
