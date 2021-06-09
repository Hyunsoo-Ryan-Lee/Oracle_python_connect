import cx_Oracle # 오라클 DB를 쉽게 활용 가능하게 해주는 driver

connection = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
print('1---',connection)
print("Database version:", connection.version) # Database version: 11.2.0.2.0
cur = connection.cursor()
print('2---',cur)

# for row in cur.execute("""select * from dept"""):
#     print(row, type(row)) # 튜플 형태로 반환!

# cur = connection.cursor()
# cur.execute("select * from dept")
# while True:
#     row = cur.fetchone() # row 하나씩 출력
#     print(1)
#     if row is None:
#         break
#     print(row)

# cur = connection.cursor()
# cur.execute("select * from dept")
# num_rows = 3
# while True:
#     rows = cur.fetchmany(num_rows) # num_rows 수 만큼 잘라서 출력
#     print(1)
#     if not rows:
#         break
#     for row in rows:
#         print(row)


cur = connection.cursor()
cur.execute("select * from dept")
rows = cur.fetchall()
for row in rows:
    print(row)


cur.close()
connection.close()

