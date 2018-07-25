from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql  #导入 pymysql
print('1')
html = urlopen('http://pesdb.net/pes2018/?id=4522')
bsObj = BeautifulSoup(html, "html.parser")
print('1')
tds = bsObj.table.tr.td.table.find_all('td')
other_info = []
for i in range(len(tds)):
	other_info.append(tds[i].get_text())
other_info = other_info[1:-2]
tds = bsObj.table.tr.td.next_sibling.next_sibling.next_sibling.next_sibling.table.find_all('td')
temp = []
for i in range(len(tds)):
	temp.append(tds[i].get_text())
temp = temp[8:-3]
other_info = other_info + temp
print(other_info)
