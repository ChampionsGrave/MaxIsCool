from agents import Agent
from samplemodel import ALiteralFuckingLlama
from tool import time_tool
import asyncio

weird_form_but_univerisal = [
  {
    'role': 'system',
    'content': '''
    You try your best ti be a helpful assistant.
   '''
  }
]



The_llama = Agent(
	name = "NotALlama",
	instructions =f"{weird_form_but_universal}",
	model=ALiteralFuckingLlama,
	tools = time_tool
)
