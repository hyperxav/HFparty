from huggingface_hub import login
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get token from environment variable
token = os.getenv("HUGGINGFACE_TOKEN")
if not token:
    raise ValueError("Please set HUGGINGFACE_TOKEN environment variable")

login(token=token) 