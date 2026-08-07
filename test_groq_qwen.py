import sys
import os
sys.path.insert(0, os.path.abspath('src'))
from google.adk.agents import llm_agent
import asyncio

async def test():
    try:
        agent = llm_agent.LlmAgent(name="test", model=f"groq/qwen/qwen3.6-27b", instruction="You are a helpful assistant")
        from core.utils import chat_with_agent
        from google.adk import runners
        runner = runners.InMemoryRunner(agent=agent, app_name="test")
        res, _ = await chat_with_agent(agent, runner, "hello")
        print(f"Success! {res[:20]}")
    except Exception as e:
        print(f"Error: {e}")

asyncio.run(test())
