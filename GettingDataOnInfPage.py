import pandas as pn
from bs4 import BeautifulSoup
import requests as request
import time
# #getting data on infifnity page
url='https://scrapingclub.com/exercise/list_infinite_scroll/'
result=request.get(url)
content=BeautifulSoup(result.text,'lxml')
starttime=time.time()
links=content.select("[href]:is(.page-link):not(.next-page)")
map,id={},0

for i in range(len(links)):
    result=request.get(url+links[i]['href'])
    content=BeautifulSoup(result.text,'lxml')
    cards=content.select(".card-body >.card-title")
    for j in range(len(cards)):
        map[id]={}
        map[id]['title']=cards[j].parent.select_one('h4 > a').text
        map[id]['price']=cards[j].parent.find('h5').text
        id+=1

results,id=[],0
for i in map.keys():
    results.append([])
    results[id].append(map[i]['title'])
    results[id].append(map[i]['price'])
    id+=1

print(pn.DataFrame(results))
print(time.time()-starttime)