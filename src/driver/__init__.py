from dotenv import load_dotenv, find_dotenv

try:
    if find_dotenv('.src.env'):
        load_dotenv('.src.env')
except FileNotFoundError:
    print("Could not find .src.env file.")
