import pymysql

#  create connection to database

try:
    db = pymysql.connect(host="localhost", user="root", password="Thienesh8@", database="thienesh")
    cursor1 = db.cursor()
    sql = """INSERT INTO food_name(id, food_name, country) VALUES("3", "BURGER", "AMERICA")"""

    cursor1.execute(sql)

    db.commit()
    print("Database: Table Updated Successfully")
    db.close()

except Exception as e:
    print(e)
