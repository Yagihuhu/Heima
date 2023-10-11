import pymysql
import sys
sys.path.append('..')  # 提升一级到项目更目录下
from config.config import *  # 从项目根目录下导入

class DB:
    def __init__(self): #封装连接数据库、建立游标
        self.conn = pymysql.connect(host=db_host,
                                    port=db_port,
                                    user=db_user,
                                    passwd=db_passwd,  # passwd 不是 password
                                    db=db,
                                    charset='utf8')
        self.cur = self.conn.cursor()  # 建立游标


    def __del__(self):  # 析构函数，实例删除时触发
        self.cur.close()   #关闭游标
        self.conn.close()  #断开连接

    def query(self, sql):
        self.cur.execute(sql)
        # return self.cur.fetchall()
        result = self.cur.fetchall()
        print(result)


    def exec(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            logging.debug(str(e))

    def change_db(self,sql):
            self.cur.execute(sql)  # 执行sql
            self.conn.commit()  # 提交更改

    def check_user(self, name):
        self.cur.execute("SELECT * FROM lucifer_user where name='{}' and is_deleted=0".format(name))  #查询敏感数据(数据条件)
        result = self.cur.fetchall()  # 获取所有查询结果
        return True if result else False

    def del_user(self, name):    #软删除用户
        try:
            self.cur.execute("UPDATE lucifer_user SET is_deleted = 1 WHERE name='{}'".format(name))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            logging.debug(str(e))

    def check_condition(self, name):
        self.cur.execute("SELECT * FROM lucifer_condition where name='{}' and is_deleted=0".format(name))  #查询敏感数据(数据条件)
        result = self.cur.fetchall()  # 获取所有查询结果
        return True if result else False

    def del_condition(self, name):    #软删除敏感数据(数据条件)
        try:
            self.cur.execute("UPDATE lucifer_condition SET is_deleted = 1 WHERE name='{}'".format(name))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            logging.debug(str(e))

    def fetch_condition_id(self):
        self.cur.execute("SELECT uid FROM lucifer_condition WHERE is_deleted = 0")  # 查询敏感数据(数据条件)
        # uid = ''.join(self.cur.fetchone())  # 获取所有查询结果
        uid = self.cur.fetchone()
        return uid  # 接收uid
