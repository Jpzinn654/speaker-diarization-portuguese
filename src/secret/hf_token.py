import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), "../../../config", ".env")

load_dotenv(dotenv_path=dotenv_path)

hf_token_api = os.getenv("HF_TOKEN_API")