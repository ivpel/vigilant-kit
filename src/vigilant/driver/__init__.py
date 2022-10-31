from dotenv import load_dotenv, find_dotenv

if find_dotenv('.vigilant.env'):
    load_dotenv('.vigilant.env')
else:
    print("Could not find .vigilant.env configuration file.")
    raise FileNotFoundError
