from dotenv import load_dotenv
import os


def get_setting():
    load_dotenv()
    env = os.getenv("ENV_MODE")
    setting = "gym.settings.dev"
    if env == 'prod':
        setting = "gym.settings.prod"
    return setting


def load_env():
    load_dotenv()
    mode = os.getenv("ENV_MODE")
    load_dotenv(f".env.{mode}")
