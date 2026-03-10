from agents import AsyncOpenAI, OpenAIChatCompletionsModel, AsyncOpenAI
from dotenv import load_dotenv
import os


ollama_base = os.getenv("OLLAMA_BASE_URL")
ollama_key = os.getenv("OLLAMA_API_KEY")
ollama_model = os.getenv("OLLAMA_DEFAULT_MODEL")



ALiteralFuckingLlama = OpenAIChatCompletionsModel( 
    model=ollama_model,
    openai_client=AsyncOpenAI(base_url=ollama_base, api_key=ollama_key)
)
