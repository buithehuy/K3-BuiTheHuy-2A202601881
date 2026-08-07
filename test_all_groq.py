import sys
import os
from dotenv import load_dotenv
load_dotenv()
sys.path.insert(0, os.path.abspath('src'))
from google.adk.agents import llm_agent
import asyncio
from core.utils import chat_with_agent
from google.adk import runners

async def test():
    models_to_test = ["llama-3.1-8b-instant", "llama3-8b-8192", "mixtral-8x7b-32768", "gemma2-9b-it"]
    for model_name in models_to_test:
        try:
            agent = llm_agent.LlmAgent(name="test", model=f"groq/{model_name}", instruction="You are a helpful assistant")
            runner = runners.InMemoryRunner(agent=agent, app_name="test")
            res, _ = await chat_with_agent(agent, runner, "hello")
            print(f"Success with {model_name}!")
            return model_name
        except Exception as e:
            print(f"Error with {model_name}: {e}")

asyncio.run(test())
