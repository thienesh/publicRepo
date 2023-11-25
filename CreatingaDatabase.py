import pymysql

#  create connection to database thienesh

try:
    db = pymysql.connect(host="localhost", user="root", password="Thienesh8")
    cursor1 = db.cursor()
    sql = """CREATE DATABASE Sowmiya"""
    cursor1.execute(sql)
    print("Database Created Successfully")
    db.close()

except Exception as e:
    print(e)
