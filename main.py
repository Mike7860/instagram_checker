from instagrapi import Client
import requests

# cl = Client()
# cl.login("username")
from instabot import Bot
bot = Bot()
bot.login(username="username", password="username")

my_followers = bot.followers()
print(my_followers)