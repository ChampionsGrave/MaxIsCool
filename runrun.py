from agents import Runner
import asyncio


runner = Runner()


async def main():
	llama_thoughts = runner.run(The_llama, "What time is it, fool?")
	return llama_thoughts.final_output

asyncio.run(main()) 
