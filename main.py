from re import T
from discord_webhook import DiscordWebhook, DiscordEmbed
from threading import Thread
from time import sleep
from sys import stdin
from random import shuffle, choice
from gc import collect


wh1 = ['https://discord.com/api/webhooks/955053453779038220/L5XNn4W2mNSuai4feCqFkN3ITzMGJEuCZj4bkjNPVR2baTVZ1HRf9XwaYZJ4tppOeob',
    'https://discord.com/api/webhooks/955061331097157643/v56sfNiJv2hFMGx5S1fSlIaL0EWSn3l0KKOTInn_1VvQbSgdXp55HOI3qL9FvWSOm3t']
wh2 = ['https://discord.com/api/webhooks/955065326196908032/QynkXhnYVUlehGmyvQ3SFs2n5mGLVHW1lMAg5t69aWSFT5-ErL8NqcOEu2_Xxs9Ytb3']
wh3 = ['https://discord.com/api/webhooks/955066600476803092/8Nl7y713UB6RFGmQ7Rux3NiXPnESszNUFX6nhEfuM9QIjdKXtC1dhpnVU9UaJMGgAFu',
    'https://discord.com/api/webhooks/955066675227672598/GR-u8UF003qKXTZ-YEqZluSe4eClT-SGXiVx2lRxgKeEM6B8VwX8yhlCyRA1Ep5Hfcu']

def shufled():
    global a
    while True:
        sleep(8)
        collect()
        f = "".join(a)
        webhook = DiscordWebhook(url=wh1, content=f, rate_limit_retry=True)
        webhook.execute()
        a = list(a)
        shuffle(a)


def aboba():
    while True:
        sleep(4)
        webhook = DiscordWebhook(url=wh2[0], rate_limit_retry=True)
        name = "c:/Users/mdddm/Downloads/" + choice(list('qwertyuiopasdfghjklzxcvbm')) + '.jpg'
        with open(name, "rb") as f:
            webhook.add_file(file=f.read(), filename='example.jpg')
        webhook.execute()


def ze():
    while True:
        sleep(4)
        collect()
        webhook = DiscordWebhook(url=wh3, rate_limit_retry=True)
        embed = DiscordEmbed(title='Политические рассуждения', description='Текст Текст Текст', color='9F329F')
        webhook.add_embed(embed)
        webhook.execute()


photos = []
a = "".join([line.strip() for line in list(stdin)])
threads = [Thread(target=aboba), Thread(target=shufled), Thread(target=ze)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
