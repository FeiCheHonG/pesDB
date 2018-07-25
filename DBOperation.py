"""对pesDB进行操作的函数"""
import MySQL

def insert_baseinfo(cur, player_num, player_urlid, player_name, other_info):
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
		base_info = "%d,'%s','%s',%s,'%s','%s','%s','%s',%s,%s,%s,'%s','%s','%s',%s,%s,%s,%s"
		base_info = base_info % (player_num,player_urlid,player_name,other_info[0],
								other_info[1],other_info[2],other_info[3],other_info[4],
								other_info[5],other_info[6],other_info[7],other_info[8],
								other_info[9],other_info[10],other_info[11],other_info[12],
								other_info[13],other_info[14])
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
