from dotenv import load_dotenv
import os


def load_env():
    load_dotenv()
    mode = os.getenv("ENV_MODE")
    load_dotenv(f".env.{mode}")
