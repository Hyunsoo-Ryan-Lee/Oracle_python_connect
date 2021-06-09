# 오라클 드라이버 모듈 사용 선언
from typing import final
import cx_Oracle

# connection = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
# cur = connection.cursor()

# cur.execute('drop tabel emp01')
# cur.execute('create table emp01 as select empno,ename from emp')

# cur.close()
# connection.close()


# emp01 테이블 생성
# create empno, ename from emp01
# table 생성 명령을 함수 내부에 넣으려면 예외처리를 적용해야함.
def table_create(table):
    connection = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
    cur = connection.cursor()
    cur.execute('select * from :y', y=table)
    # 테이블이나 컬럼명을 변수로 넣으면 변경될 위험이 크기 때문에
    # 오라클 자체에서 실행이 안되게 막음
    for i in cur:
        print(i)

    cur.close()
    connection.close()


def emp01_create():
    connection = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
    cur = connection.cursor()
    try:
        cur.execute('drop tabel emp01')
        cur.execute('create table emp02 as select empno,ename from emp')
    except Exception as e:
        print('예외 발생!')
    finally:
        print("예외발생 여부와 무관하게 100퍼 실행되는 영역!")
    cur.close()
    connection.close()


# emp01 query - all select / one select ...
def emp01_query():
    connection = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
    cur = connection.cursor()
    cur.execute('select * from emp01')
    rows = cur.fetchall()

    for i in rows:
        print(i)

    cur.close()
    connection.close()


# empno로 해당하는 사원의 이름을 검색
def emp01_query_one(empno):
    connection = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
    cur = connection.cursor()
    cur.execute('select ename from emp01 where empno= :empno', empno=empno)
    row = cur.fetchone()
    print(row)
    cur.close()
    connection.close()


# emp01 insert
# insert into emp01 values ()
'''
def emp01_insert(new_empno, new_ename):
    connection = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
    cur = connection.cursor()

    # cur.execute("insert into emp01 values(:new_empno, :new_ename)",\
    #     new_empno=1212,new_ename='강하늘')

    cur.execute("insert into emp01 values(:new_empno, :new_ename)"\
        ,new_empno=new_empno,new_ename=new_ename) #뒤에 선언한 변수에 꼭 값을 넣어주어야 함. 자기사진일지라도
        #values 뒤에 있는 binding변수 = 함수에서 선언된 변수
    connection.commit()

    cur.close()
    connection.close()



#emp01 update
#update emp01 set ename = ? where empno = ?
def emp01_update(empno, u_ename): #사번은 수정되지 않으니 그대로 적용
    connection = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
    cur = connection.cursor()
    # cur.execute("update emp01 set ename='스미스' where empno=7369")
    cur.execute("update emp01 set ename = :u_ename where empno = :empno"\
        ,u_ename=u_ename,empno=empno)
    
    connection.commit()
    cur.close()
    connection.close()


#emp01 delete
#delete from emp01 where empno = ?
def emp01_delete(empno):
    connection = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
    cur = connection.cursor()
    cur.execute("delete from emp01 where empno= :empno",empno=empno)
    
    connection.commit()
    cur.close()
    connection.close()
'''
# 참고 : 현업에서 DDL 문장은 가급적 프로그램 코드로 하지 않고 sql 문장으로 작업 권장
# table 구조 변경은 최소화

# Python에서 실행 순서에 대한 제어 또는 python 파일을 독립적으로 실행할 때 필요한 코드
# 호출 순서 : table 생성 >> 검색 >> data 저장 >> 검색 >> 수정 >> 검색 >> 삭제 >> 검색

if __name__ == "__main__":
    # emp01_insert(1212,'강하늘')
    # emp01_update(7369,'스미스')
    # emp01_delete(1111)
    # emp01_query_one(7844)
    emp01_query()
    # table_create('emp')
