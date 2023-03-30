import os

def get_api_key():
    try:
        #get api key from environment variables
        KEY = os.getenv('WEATHERKEY')
        if KEY is not None:
            return KEY
        else:
            return False
    except Exception as e:
        print(f"Your error: {e}")