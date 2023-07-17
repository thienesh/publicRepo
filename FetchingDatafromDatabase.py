import pymysql

try:
    db = pymysql.connect(host="localhost", user="root", password="Thienesh8@", database="thienesh")

    cursor1 = db.cursor()

    sql = """ SELECT*FROM food_name """

    cursor1.execute(sql)

    result = cursor1.fetchall()

    for rows in result:
        id = rows[0]
        food_name = rows[1]
        country = rows[2]

        print(id, food_name, country)

    db.close()

except Exception as e:
    print(e)