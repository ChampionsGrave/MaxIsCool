from agents import Agent, Runner
from samplemodel import ALiteralFuckingLlama
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
	model=ALiteralFuckingLlama
)
runner = Runner()
async def main():
	llama_thoughts = runner.run(The_llama, "What time is it, fool?"
	return llama_thoughts.final_output

asyncio.run(main()) 
