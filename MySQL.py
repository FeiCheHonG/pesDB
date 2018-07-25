"""用于的数据库进行操作的底层函数,函数不关闭光标，在使用过后请自行关闭光标"""
import pymysql  #导入 pymysql

def insert(cur,table_name, values):
	"""插入，参数分别是光标,表名，及values括号中的字符串，返回函数执行信息"""
	if type(values) != str:
		return ("参数错误！values应为字符串类型")
	elif type(table_name) != str:
		return ("参数错误！table_name应为字符串类型")
	else:
		sql_insert ="""insert into %s values(%s)"""
		try:
			cur.execute(sql_insert % (table_name, values))
			#提交
			cur.connection.commit()
		except Exception as e:
			#错误回滚
			cur.connection.rollback() 
			return ('存储错误！SQL语句未正常执行')
		else:
			return ('存储成功！')
