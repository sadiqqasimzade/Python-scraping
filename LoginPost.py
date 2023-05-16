from unittest import result
import requests as request
from bs4 import BeautifulSoup
url='https://scrapingclub.com/exercise/basic_login/'
client=request.session()
result=client.get(url)
token=client.cookies['csrftoken']
result=client.post(url,headers={
    'cookie': f'csrftoken={token};',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37',
    'referer':'https://scrapingclub.com/exercise/basic_login/'
},data={
    'name':'scrapingclub',
    'password':'scrapingclub',
    'csrfmiddlewaretoken': f'{token}'
})

content=BeautifulSoup(result.content,'lxml')
print(content)

