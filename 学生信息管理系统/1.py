import mysql.connector

# 创建数据库连接
db = mysql.connector.connect(
    host="127.0.0.1",  # MySQL服务器地址
    user="root",   # 用户名
    password="1234567890",  # 密码
    database="sys"  # 数据库名称
)

# 创建游标对象，用于执行SQL查询
cursor = db.cursor()

