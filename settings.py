import os
from dotenv import load_dotenv

load_dotenv()

# AWS configuration credentials
AWS_CONFIG = {
    "aws_access_key_id": os.getenv("ACCESS_KEY"),
    "aws_secret_access_key": os.getenv("SECRET_KEY"),
}
