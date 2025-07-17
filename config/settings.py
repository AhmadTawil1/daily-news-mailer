import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Now you can safely read variables
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
