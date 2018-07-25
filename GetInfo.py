"""从HTML网页上获取信息"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def getpageinfo(page_num, players_urlid, players_name):
	"""获得页面中球员的姓名及urlid"""
	print("开始获取PAGE：", page_num, "球员姓名及urlid")
	if page_num==1:
		html = urlopen('http://pesdb.net/pes2018/')
	else:
		html = urlopen('http://pesdb.net/pes2018/?page=' + str(page_num))
	bsObj = BeautifulSoup(html, "html.parser")
	for row in bsObj.table.find_all('a',{"href":re.compile("\.?id=.*")}):
		players_urlid.append(row.attrs['href'])
		players_name.append(row.get_text())
	print("获取成功！")
	
def getplayerinfo(player_urlid, player_name, data_name, level_data):
	"""根据球员id获得球员信息"""
	print('正在获取：',player_name,'的信息')
	html = urlopen('http://pesdb.net/pes2018/' + player_urlid)
	bsObj = BeautifulSoup(html, "html.parser")
	print('正在处理')
	
	#获取能力值
	abilities = bsObj.find('script',text=re.compile('abilities.*')).get_text()
	abilities = abilities[14:-3].replace(',[','').split("]")
	for i in range(len(data_name)):
		level_data[data_name[i]] = abilities[i]
	print('获取成功！')
	
	#获取其他基本信息
	tds = bsObj.table.tr.td.table.find_all('td')
	other_info1 = []
	for i in range(len(tds)):
		other_info1.append(tds[i].get_text())
	other_info1 = other_info1[1:-2]
	if other_info1[0] == 'Free Agents':
		other_info1 = ['NULL']+other_info1
	tds = bsObj.table.tr.td.next_sibling.next_sibling.next_sibling.next_sibling.table.find_all('td')
	other_info2 = []
	for i in range(len(tds)):
		other_info2.append(tds[i].get_text())
	other_info2 = other_info2[8:-3]
	other_info = other_info1 + other_info2
	return other_info

