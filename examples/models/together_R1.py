import asyncio
import os

from dotenv import load_dotenv
from langchain_together import ChatTogether
from pydantic import SecretStr

from browser_use import Agent

# dotenv
load_dotenv()

together_api_key = os.getenv('TOGETHER_API_KEY', '')
if not together_api_key:
	raise ValueError('TOGETHER_API_KEY is not set')


async def run_search():
	agent = Agent(
		task=('check score of most recent Golden State Warriors game'),
		llm=ChatTogether(
			model='meta-llama/Llama-3.3-70B-Instruct-Turbo',
			together_api_key=SecretStr(together_api_key),
		),
		use_vision=False,
		max_failures=2,
		max_actions_per_step=1,
	)

	await agent.run()


if __name__ == '__main__':
	asyncio.run(run_search())
