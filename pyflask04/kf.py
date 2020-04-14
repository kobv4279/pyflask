from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

import time

url = 'http://www.gen.go.kr/xboard/board.php?mode=list&tbnum=32&addUrlQuery=&sCat='

response = urlopen(url)
soup = BeautifulSoup(response, 'html.parser')

title = soup.findAll('td', attrs={'class':'left subject'})


sub_list = []
ref_list = []
for i in title:
    #print(i.a.text)
    #print("http://www.gen.go.kr/xboard/" + i.a['href'])

    sub = i.a.text
    #print(type(sub))
    sub_list.append(str(sub))
    sub_list.append('\t')
    ref = str("http://www.gen.go.kr/xboard/" + i.a['href'])
    ref_list.append(str(ref))
print(sub_list)
print(ref_list)
