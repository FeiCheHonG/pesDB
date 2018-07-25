from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql  #导入 pymysql
		
def insert_baseinfo(base_info, player_num):
	"""向数据库中插入球员的基本信息"""
	sql_insert = "INSERT INTO players VALUES ('%s')"
	try:
		cur.execute(sql_insert % (base_info))
		cur.connection.commit()
	except Exception as e:
		cur.connection.rollback()
		print('插入：',player_name,'时出错')
		
def getpageinfo(page_num, players_urlid, players_name):
	"""获得页面中球员的姓名及urlid"""
	print("开始获取PAGE：",str(page_num),"球员三项基本信息")
	if page_num==1:
		html = urlopen('http://pesdb.net/pes2018/')
	else:
		html = urlopen('http://pesdb.net/pes2018/?page=' + str(page_num))
	bsObj = BeautifulSoup(html, "html.parser")
	for row in bsObj.table.find_all('a',{"href":re.compile("\.?id=.*")}):
		players_urlid.append(row.attrs['href'])
		players_name.append(row.get_text())
	print("获取成功！")
	
def getplayerinfo(player_urlid, player_name, data_name, level_data, other_info):
	"""根据球员id获得球员信息"""
	print('正在获取：',player_name,'的信息')
	html = urlopen('http://pesdb.net/pes2018/' + player_urlid)
	bsObj = BeautifulSoup(html, "html.parser")
	print('正在处理')
	#获取其他基本信息
	tds = bsObj.table.tr.td.table.find_all('td')
	other_info1 = []
	for i in range(len(tds)):
		other_info1.append(tds[i].get_text())
	other_info1 = other_info1[1:-2]
	tds = bsObj.table.tr.td.next_sibling.next_sibling.next_sibling.next_sibling.table.find_all('td')
	other_info2 = []
	for i in range(len(tds)):
		other_info2.append(tds[i].get_text())
	other_info2 = other_info2[8:-3]
	other_info_str = ''
	for i in range(len(other_info1)):
		other_info_str = other_info_str + "'" +other_info1[i] + "',"
	for i in range(len(other_info2)):
		other_info_str = other_info_str + other_info2[i] + ","
	other_info = other_info[:-1]
	print('other_info:',other_info)
	#获取能力值
	abilities = bsObj.find('script',text=re.compile('abilities.*')).get_text()
	abilities = abilities[14:-3].replace(',[','').split("]")
	for i in range(len(data_name)):
		level_data[data_name[i]] = abilities[i]
	print('获取成功！')

def insert_abilitys(table_name, leval_data, player_num, player_name):
	"""向数据库中插入球员的各项能力1-60级数据"""
	sql_insert = "INSERT INTO %s VALUES (%d,%s)"
	try:
		cur.execute(sql_insert % (table_name, player_num, leval_data))
		cur.connection.commit()
	except Exception as e:
		cur.connection.rollback()
		print('插入：',player_name,'能力值时出错')

#设置要获取的页面数
page_num = 1

#打开数据库连接
db= pymysql.connect(host="localhost",user="root",
			password="wangyihong",db="pesdb",port=3306)
cur = db.cursor()

data_name = ['攻击能力','控球','盘球','地面传球','空中传球','射门','定位球'
				,'弧度','头球','防守能力','抢球','脚下力量','速度','爆发力','身体平衡'
				,'协调性','跳跃','体力','守门','接球','解围','扑救反应','覆盖区域','整体评价']

players_urlid, players_name, players_num, level_data, other_info = [], [], [], {}, []
getpageinfo(page_num, players_urlid, players_name)
players_num = [((page_num-1) * len(players_urlid) + i + 1) for i in range(len(players_urlid))]

for i in range(len(players_urlid)):
	getplayerinfo(players_urlid[i][2:], players_name[i], data_name, level_data, other_info)
	base_info = str(players_num[i]) +",'"+ players_urlid[i] +"','"+ players_name[i] +"',"+ other_info
	print(base_info)
	print('正在存储')
	#insert_baseinfo(base_info, players_name[i])
	#for key, values in level_data.items():
	#	insert_abilitys(key, values, players_num[i], players_name[i])
	print('存储完毕!\n--------------------------------------')
	
#关闭数据库和光标
cur.close()
db.close()

