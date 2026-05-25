from langchain_ollama import ChatOllama
import os
from dotenv import load_dotenv

load_dotenv()


# Using Ollama cloud API
api_key = os.getenv("OLLAMA_API_KEY")
base_url = os.getenv("OLLAMA_BASE_URL")

def model():
    model = ChatOllama(
        model="gemma4:31b-cloud",
        temperature=0,
        base_url=base_url,
        api_key=api_key
    )
    return model

