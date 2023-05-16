from hashlib import md5
import requests as request

mysession=request.session()
htmldata=mysession.get("https://scrapingclub.com/exercise/detail_sign/")
token=str(mysession.cookies['token'])
codedtoken=md5(token.encode('utf-8'))

result=mysession.get(f'https://scrapingclub.com/exercise/ajaxdetail_sign/?sign={codedtoken.hexdigest()}',headers={
    'cookie':f'token={token}',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37',
    'x-requested-with': 'XMLHttpRequest'
})
print(result.content)
