
import json
import requests as request
import pandas as ps

url='https://scrapingclub.com/exercise/detail_cookie/'

session=request.session()
result=session.get(url)
cookie=session.cookies['token']
url='https://scrapingclub.com/exercise/ajaxdetail_cookie/?token='
result=request.get(url+cookie,headers={
    'cookie':f'token={cookie}',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37',
    'x-requested-with': 'XMLHttpRequest'
})
print(result.text)
print(ps.json_normalize(json.loads(result.text)))
