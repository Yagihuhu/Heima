from lib.db import DB

db = DB()  # 实例化一个数据库操作对象
# db.query("SELECT * FROM lucifer_risk where name='test'")
# db.query('select name from lucifer_user where id=1')
# db.check_user('hyjtest')
# db.del_user("update lucifer_user set is_deleted = 0 where name='hyjtest'")

# if db.check_user("APItest"):
#     db.del_user("APItest")

if db.check_condition('APItest'):
    db.del_condition('APItest')
