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
	
def get_abilities(bsObj, data_name, level_datas):
	abilities = bsObj.find('script',text=re.compile('abilities.*')).get_text()
	abilities = abilities[14:-3].replace(',[','').split("]")
	for i in range(len(data_name)):
		level_datas[data_name[i]] = abilities[i]
	
def get_styles(bsObj, playing_style, player_skills, com_playing_styles):
	#获取风格信息
	table = bsObj.find('th',text = 'Playing Style').parent.parent.find_all('tr')
	styles = []
	for i in range(len(table)):
		styles.append(table[i].get_text())
	#获取索引
	playing_style_index = styles.index('Playing Style')
	player_skills_index = styles.index('Player Skills')
	com_playing_styles_index = styles.index('COM Playing Styles')
	#将风格信息切片
	playing_style_label = styles[playing_style_index + 1:player_skills_index]
	for i in playing_style_label:
		playing_style.append(i)
	player_skills_label = styles[player_skills_index + 1:com_playing_styles_index]
	for i in player_skills_label:
		player_skills.append(i)
	com_playing_styles_label = styles[com_playing_styles_index + 1:]
	for i in com_playing_styles_label:
		com_playing_styles.append(i)
		
def get_oterinfo(bsObj, other_info):	
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
	other_info_label = other_info1 + other_info2
	for i in other_info_label:
		other_info.append(i)
		
def getplayerinfo(player_urlid, player_name, data_name, level_datas, other_info, playing_style, player_skills, com_playing_styles):
	"""根据球员id获得球员信息"""
	print('正在获取：',player_name,'的信息')
	html = urlopen('http://pesdb.net/pes2018/' + player_urlid)
	bsObj = BeautifulSoup(html, "html.parser")
	print('正在处理')
	del other_info[:], playing_style[:], player_skills[:], com_playing_styles[:]
	#获取能力值
	get_abilities(bsObj, data_name, level_datas)
	
	#获取风格信息
	get_styles(bsObj, playing_style, player_skills, com_playing_styles)
	
	#获取其他基本信息
	get_oterinfo(bsObj, other_info)
	print('获取成功！')

