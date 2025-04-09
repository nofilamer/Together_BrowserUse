"""
Simple try of the agent using Together.ai and Meta-Llama 3.

@dev You need to add TOGETHER_API_KEY to your environment variables.
"""

import os
import sys
import asyncio
from dotenv import load_dotenv

# Setup Python path to import browser_use.Agent
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Load .env variables
load_dotenv()

from langchain_community.chat_models import ChatTogether
from browser_use import Agent  # Your custom Agent class

# Load API key from environment
TOGETHER_API_KEY = os.getenv('TOGETHER_API_KEY')

# Initialize the LLM
llm = ChatTogether(
	model='meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo',
	temperature=0.7,
	max_tokens=1024,
	together_api_key=TOGETHER_API_KEY,
)

# Create the agent
agent = Agent(
	task='Check the score of most recent Golden State Warriors game',
	llm=llm,
)


# Define main async function
async def main():
	await agent.run(max_steps=10)
	input('Press Enter to continue...')


# Run the agent
asyncio.run(main())
