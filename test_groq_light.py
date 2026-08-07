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
    models_to_test = ["allam-2-7b", "canopylabs/orpheus-v1-english"]
    for model_name in models_to_test:
        try:
            agent = llm_agent.LlmAgent(name="test", model=f"groq/{model_name}", instruction="You are a helpful assistant")
            runner = runners.InMemoryRunner(agent=agent, app_name="test")
            res, _ = await chat_with_agent(agent, runner, "hello")
            print(f"Success with {model_name}: {res[:20]}")
        except Exception as e:
            print(f"Error with {model_name}: {e}")

asyncio.run(test())
