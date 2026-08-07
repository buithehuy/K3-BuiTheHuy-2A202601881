import sys
import os
sys.path.insert(0, os.path.abspath('src'))
from google.adk.agents import llm_agent
import asyncio

async def test():
    for model_name in ["gemma2-9b-it", "mixtral-8x7b-32768", "llama-3.1-8b-instant"]:
        try:
            agent = llm_agent.LlmAgent(name="test", model=f"groq/{model_name}", instruction="You are a helpful assistant")
            from core.utils import chat_with_agent
            from google.adk import runners
            runner = runners.InMemoryRunner(agent=agent, app_name="test")
            res, _ = await chat_with_agent(agent, runner, "hello")
            print(f"Success with {model_name}: {res[:20]}")
        except Exception as e:
            print(f"Error with {model_name}: {e}")

asyncio.run(test())
