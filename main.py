from instagrapi import Client
import requests

# from instabot import Bot
# bot = Bot()
# bot.login(username="username", password="username")

data_0 = {"client_id": ,
          "redirect_uri": "http://",
          "scope": "user_profile",
          "response_type": "code"}

data = {"client_id": ,
        "client_secret": "",
        #"client_secret": "",
        "grant_type": "authorization_code",
        "redirect_uri": "http://",
        "code": ""}
#response = requests.post("https://api.instagram.com/oauth/access_token", data=data)
response = requests.get("")
print(response.content)


#x = requests.post("https://api.instagram.com/oauth/access_token")