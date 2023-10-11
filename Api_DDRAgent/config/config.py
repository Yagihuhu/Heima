# -*- coding: utf-8 -*-
import logging
import os

# 项目路径
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 当前文件的上一级的上一级目录（增加一级）
data_path = os.path.join(prj_path, 'data')  # 数据目录
test_path = os.path.join(prj_path, 'test')   # 用例目录
log_file = os.path.join(prj_path, 'log', 'log.txt')  # 更改路径到log目录下
report_file = os.path.join(prj_path, 'report', 'report.html')  # 更改路径到report目录下
data_file = os.path.join(prj_path, 'data', 'test_user_data.xls')  #测试用例数据
token_path = os.path.join(prj_path,'config','token')
com_id_path = os.path.join(prj_path,'config', 'Company')
#
# log配置
logging.basicConfig(level=logging.DEBUG,  # log level
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename=log_file,  # 日志输出文件
                    filemode='a')  # 追加模式

# 邮件配置
smtp_server = 'smtp.qq.com'
smtp_user = '2196900073@qq.com'
smtp_password = 'jpnyandojetxdjgi'

sender = smtp_user  # 发件人
receiver = '1047783724@qq.com'  # 收件人
subject = '接口测试报告'  # 邮件主题



#开发环境IP
# IP = 'https://192.168.89.26:8443/qzh/api/v1/agent/device/c6917da3-be7d-4f49-819d-a00bdf125cae'
#测试环境IP
IP: str = 'https://192.168.89.32:8443/qzh/api/v1/agent/device/bae4f6c4-249e-44bf-ad7c-0b8c683e385d'

#获取token
with open(token_path) as f:
    content = f.read()
token = 'Token {}'.format(content)
print(token)

#获取commany_id
with open(com_id_path) as f:
    Company_id = f.read()
print(Company_id)

#获取开发环境header(使用双引号）
headers1 = {
    "Authorization": token,
    "Content-Type": "application/json",
    "X-CS-Header-Company":Company_id,
    "X-CS-Header-App": "qzh",
}



# # 开发环境数据库配置
# db_host = '192.168.89.26'   # 自己的服务器地址
# db_port = 13306
# db_user = 'qzh'
# db_passwd = 'z0WX0KvWqCr3Ti1G'
# db = 'lucifer'
# 测试环境数据库配置
db_host = '192.168.89.32'   # 自己的服务器地址
db_port = 13306
db_user = 'qzh'
db_passwd = 'z0WX0KvWqCr3Ti1G'
db = 'lucifer'

if __name__ == '__main__':
    logging.info("hello")