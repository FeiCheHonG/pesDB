"""对pesDB进行操作的函数"""
import MySQL
def insert_baseinfo(cur, player_num, player_urlid, player_name, other_info, playing_style, player_skills, com_playing_styles):
	"""向数据库中插入球员的基本信息"""
	print('正在存储', player_num, '号球员', player_name,'的基本信息:')
	if type(player_num) != int:
		print('参数错误！球员号应为整形')
	elif type(player_urlid) !=str:
		print('参数错误！球员urlid应为字符串类型')
	elif type(player_name) !=str:
		print('参数错误！球员名应为字符串类型')
	elif type(other_info) != list:
		print('参数错误！其他信息应为列表')
	else:
		base_info_head = "%d,'%s','%s',%s,'%s','%s','%s','%s',%s,%s,%s,'%s','%s','%s',%s,%s,%s,%s"
		base_info_head = base_info_head % (player_num,player_urlid,player_name,other_info[0],
								other_info[1],other_info[2],other_info[3],other_info[4],
								other_info[5],other_info[6],other_info[7],other_info[8],
								other_info[9],other_info[10],other_info[11],other_info[12],
								other_info[13],other_info[14])
		playing_style_str = ['NULL']
		player_skills_str = ['NULL','NULL','NULL','NULL','NULL','NULL','NULL','NULL','NULL','NULL','NULL','NULL','NULL','NULL','NULL']
		com_playing_styles_str = ['NULL','NULL','NULL','NULL','NULL','NULL','NULL']
		for i in range(len(playing_style)):
			playing_style_str[i] = "'" + playing_style[i] + "'"
		for i in range(len(player_skills)):
			player_skills_str[i] = "'" + player_skills[i] + "'"
		for i in range(len(com_playing_styles)):
			com_playing_styles_str[i] = "'" + com_playing_styles[i] + "'"
		base_info_last = ",%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" 
		base_info_last = base_info_last % (playing_style_str[0],player_skills_str[0],player_skills_str[1],
			player_skills_str[2],player_skills_str[3],player_skills_str[4],player_skills_str[5],player_skills_str[6],
			player_skills_str[7],player_skills_str[8],player_skills_str[9],player_skills_str[10],player_skills_str[11],
			player_skills_str[12],player_skills_str[13],player_skills_str[14],com_playing_styles_str[0],
			com_playing_styles_str[1],com_playing_styles_str[2],com_playing_styles_str[3],
			com_playing_styles_str[4],com_playing_styles_str[5],com_playing_styles_str[6])
		base_info = base_info_head + base_info_last
		print(base_info)
		print(MySQL.insert(cur, 'players', base_info))

def insert_abilitys(cur, table_name, player_num, player_name, leval_data):
	"""向数据库中插入球员的各项能力1-60级数据"""
	print('正在存储', player_num, '号球员', player_name,'的能力信息:')
	if type(player_num) != int:
		print('参数错误！球员号应为整形')
	elif type(player_name) !=str:
		print('参数错误！球员名应为字符串类型')
	elif type(leval_data) != str:
		print('参数错误！等级数据应为字符串类型')
	else:
		values = "%d,%s" % (player_num, leval_data)
		print(MySQL.insert(cur, table_name, values))
