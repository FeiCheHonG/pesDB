import pymysql  #导入 pymysql
import DBOperation as db_o
import GetInfo as gi

#设置要获取的页面号
page_num = 1

data_name = ['攻击能力','控球','盘球','地面传球','空中传球','射门','定位球'
				,'弧度','头球','防守能力','抢球','脚下力量','速度','爆发力','身体平衡'
				,'协调性','跳跃','体力','守门','接球','解围','扑救反应','覆盖区域','整体评价']
players_urlid, players_name, players_num, level_datas, other_info = [], [], [], {}, []
playing_style, player_skills, com_playing_styles = [], [], []
#打开数据库连接
db= pymysql.connect(host="localhost",user="root",
			password="wangyihong",db="pesdb",port=3306)
cur = db.cursor()

gi.getpageinfo(page_num, players_urlid, players_name)
players_num = [((page_num-1) * len(players_urlid) + i + 1) for i in range(len(players_urlid))]

for i in range(len(players_urlid)):
	gi.getplayerinfo(players_urlid[i][2:], players_name[i], data_name, level_datas, other_info, playing_style, player_skills, com_playing_styles)
	
	print(playing_style,'\n',player_skills,'\n',com_playing_styles)
	
	db_o.insert_baseinfo(cur, players_num[i], players_urlid[i], players_name[i], other_info, playing_style, player_skills, com_playing_styles)
	#for table_name, leval_data in level_datas.items():
	#	db_o.insert_abilitys(cur, table_name, players_num[i], players_name[i], leval_data)
	print('--------------------------------------')
	
#关闭数据库和光标
cur.close()
db.close()


