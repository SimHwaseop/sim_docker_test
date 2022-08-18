import requests
from datetime import datetime
from bs4 import BeautifulSoup

def discord(content):
    discord_api_url = "https://discord.com/api/webhooks/1006217824051679292/_-YmsFjXtukmJkh5x2J5tqbcxLlN6XrfPvtOyyTYMnpkEzl6mMLEwusqLPDFn36d_9x2"
    headers = {
        'Content-Type': 'application/json',
    }
    date = '{"content":"%s"}' %(content) #.encode('utf-8')
    #print(date)
    requests.post(discord_api_url,headers=headers,data=date.encode('utf-8'))

discord(str(datetime.today()))