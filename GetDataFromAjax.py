import requests as request


#getting json ajax
url='https://scrapingclub.com/exercise/ajaxdetail/'
result=request.get(url)
print(result.text)





