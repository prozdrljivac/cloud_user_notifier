import os

from dotenv import load_dotenv

load_dotenv()

# AWS Settings
AWS_COGNITO_USER_POOL_ID = os.getenv("AWS_COGNITO_USER_POOL_ID")
