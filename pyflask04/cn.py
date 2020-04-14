from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

import time

url = 'http://www.jne.go.kr/board/list.jne?boardId=BBS_0000282&menuCd=DOM_000000102006001000&contentsSid=252&cpath='

response = urlopen(url)
soup = BeautifulSoup(response, 'html.parser')

sub_list = []
for i in soup.select("td.subjectEtc"):
    print(i.a.get('title','/'))
    sub = i.a.get('title','/')
    sub_list.append(str(sub))
    sub_list.append('<br>')

#
#
# sub_list = []
# ref_list = []
# for i in title:
#     #print(i.a.text)
#     #print("http://www.gen.go.kr/xboard/" + i.a['href'])
#
#     sub = i.a.text
#     #print(type(sub))
#     sub_list.append(str(sub))
#     sub_list.append('<br>')
#     ref = str("http://www.gen.go.kr/xboard/" + i.a['href'])
#     ref_list.append(str(ref))
# print(sub_list)
#print(ref_list)