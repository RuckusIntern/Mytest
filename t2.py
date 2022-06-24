import pymysql

# 資料庫設定
db_settings = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "1",
    "db": "test",
    "charset": "utf8"
}
try:
   # 建立Connection物件
    conn = pymysql.connect(**db_settings)
    # 建立Cursor物件
    with conn.cursor() as cursor:
         # 查詢資料SQL語法
        command = "SELECT * FROM users"
        # 執行指令
        cursor.execute(command)
        # 取得所有資料
        result = cursor.fetchall()
        print(result)
except Exception as ex:
    print(ex)