import requests  
import json
import os 
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")
API_KEY = os.getenv("API_Key")

API_Key = "AIzaSyDIe1ZkIfv1mKyOYnbmZwDGsdWNB8Mv3Hw"
Channel_Handle = "MrBeast"

def get_playlist_id():

    try :

        url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={Channel_Handle}&key={API_Key}"

        response = requests.get(url)
        
        response.raise_for_status()
        
        print(response)
        
        data = response.json() 

        # print(json.dumps(data,indent = 4))

        Channel_items = data ['items'] [0] 

        Channel_playlist_id = Channel_items ['contentDetails']['relatedPlaylists']['uploads']

        print(Channel_playlist_id)


    except requests.exceptions.RequestException as e :
        raise e 


if __name__ == "__main__" :
    get_playlist_id()
