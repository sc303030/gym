from dotenv import load_dotenv
import os


def get_setting():
    load_dotenv()
    env = os.getenv("ENV_MODE")
    setting = "gym.settings.dev"
    if env == 'prod':
        setting = "gym.settings.prod"
    return setting
