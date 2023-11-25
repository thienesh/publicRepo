import pymysql

#  create connection to database thienesh

try:
    db = pymysql.connect(host="localhost", user="root", password="Thienesh8@", database="thienesh")
    cursor1 = db.cursor()
    sql = """CREATE TABLE food_name(id INT, food_name VARCHAR(30), country VARCHAR(30))"""
    cursor1.execute(sql)
    print("Database: Table Created Successfully")
    db.close()

except Exception as e:
    print(e)
