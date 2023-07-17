import pymysql

try:
    db = pymysql.connect(host="localhost", user="root", password="Thienesh8@", database="thienesh")

    cursor1 = db.cursor()
    # AES ENCRYPTION USING MYSQL DATABASE
    sql = """ SELECT AES_ENCRYPT('sowmiya', 'entrepreneur') """

    cursor1.execute(sql)

    result = cursor1.fetchall()
    print(result)

    db.close()

except Exception as e:
    print(e)