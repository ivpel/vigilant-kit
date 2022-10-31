from dotenv import load_dotenv, find_dotenv

try:
    if find_dotenv('.vigilant.env'):
        load_dotenv('.vigilant.env')
except FileNotFoundError:
    print("Could not find .vigilant.env file.")
