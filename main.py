from instagrapi import Client
import requests

# from instabot import Bot
# bot = Bot()
# bot.login(username="username", password="username")
query = {"client_id": ,
  "redirect_uri": "https://socialsizzle.herokuapp.com/auth/",
  "scope": "user_profile",
  "response_type": "code",
  "state": 1}
response = requests.get("https://api.instagram.com/oauth/authorize", params=query)
print(response.text)
