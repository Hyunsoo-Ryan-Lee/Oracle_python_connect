import cx_Oracle # 오라클 DB를 쉽게 활용 가능하게 해주는 driver

# 접속 객체
connection = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
print('1---',connection)

# 커서 객체
cursor = connection.cursor()
print('2---',cursor)

#select한 결과값을 ResultSet이라 표현
cursor.execute("""select * from dept""")

for deptno, dname, loc in cursor:
    print(deptno, dname, loc)

cursor.close()
connection.close()

