from instagrapi import Client
import requests

# from instabot import Bot
# bot = Bot()
# bot.login(username="username", password="username")
access_token = "access_token="
response = requests.get("https://graph.facebook.com/v9.0/me/accounts?")
print(response.text)
