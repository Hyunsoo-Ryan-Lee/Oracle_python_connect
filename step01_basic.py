import cx_Oracle # 오라클 DB를 쉽게 활용 가능하게 해주는 driver

# Connect as user "hr" with password "welcome" to the "orclpdb1" service running on this computer.
connection = cx_Oracle.connect(user="hr", password="hr", dsn="xe")
print('DB 접속 성공')

# 접속된 db에 sql 문장 실행 및 결과값 활용 가능하게 해주는 기능
cursor = connection.cursor()

# execute() : query(select, 질의) 문장 가능한 함수
cursor.execute("""
        SELECT first_name, last_name
        FROM employees
        WHERE department_id = :did AND employee_id > :eid""",
        did = 50,
        eid = 190)
for fname, lname in cursor:
    print("Values:", fname, lname)

cursor.close()
connection.close()