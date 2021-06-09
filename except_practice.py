
import cx_Oracle # cx_Oracle 불러오기
​
def dept01_create(): # 테이블 생성 함수
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe") #계정 연결
        try:
            # Cursor())는 일련의 데이터에 순차적으로 액세스할 때 검색 및 "현재 위치"를 포함하는 데이터 요소
            cur = conn.cursor() # cursor 메소드 소환
            cur.execute('drop table dept01') # 테이블 drop 명령
            cur.execute('create table dept01 as select * from dept') # dept와 동일한 dept01 table 생성
            cur.execute('alter table dept01 add constraint dept01_uk_deptno unique(deptno)') # deptno가 중복되면 안된다는 제약조건 추가
        except Exception as e: # 예외처리
            print(e) # 에러 발생시 e 출력
        finally:
            cur.close()
            conn.close() # 메모리 반환
    except Exception as e: # 애초에 계정 연결이 되지 않았다면 예외 처리를 통해 e 출력
        print(e)
    
​
​# 아래부터는 위와 중복되는 문장에 대한 주석처리는 생략
def dept01_query(find_dname): 
    try:
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
        try:
            cur = conn.cursor()
            cur.execute("select * from dept01 where dname like :dname", dname=find_dname)
            # dept01_query 함수 실행시 넣어준 부서명과 같은 부터의 data들을 dept01 table에서 select
            rows = cur.fetchall() # fetchall method를 이용하여 조회한 data 모두를 가져온다.
            for row in rows:
                print(row)  # for문을 통해 rows에 저장된 data들을 하나씩 출력
        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()
    except Exception as e:
        print(e)
​
​
​
def dept01_insert(new_deptno, new_dname, new_loc): # data를 새로 추가하는 함수
    try:
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
        try:
            cur = conn.cursor()
            cur.execute("insert into dept01 values(:deptno, :dname, :loc)", deptno=new_deptno, dname=new_dname, loc=new_loc)
            # deptno, dname, loc에 새로운 값을 할당받아 dept01 테이블에 저장을 실행
            conn.commit() # commit을 통해 변경된 data를 테이블에 반영
            # COMMIT이 일어난 시점부터 다음의 COMMIT전까지의 작업이 하나의 트랜잭션이다.
        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()
    except Exception as e:
        print(e)
​
​
​
def dept01_update(deptno, new_dname, new_loc): # 기존의 data를 변경하는 update 함수
    try:
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
        try:
            cur = conn.cursor()
            cur.execute("update dept01 set dname=:dname, loc=:loc where deptno=:deptno", dname=new_dname, loc=new_loc, deptno=deptno)
            # deptno, dname, loc에 변경된 값을 할당받아 dept01 테이블에 저장을 실행
            conn.commit() # commit을 통해 변경된 data를 테이블에 반영
        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()
    except Exception as e:
        print(e)
​
​
​
def dept01_delete(deptno): # dept01 table의 특정 row를 삭제하는 함수
    try:
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
        try:
            cur = conn.cursor()
            cur.execute("delete from dept01 where deptno=:deptno", deptno=deptno)
            # 입력받은 deptno와 일치하는 data 행들의 값을 delete
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()
    except Exception as e:
        print(e)
​
​
if __name__ == '__main__': # 해당 조건문 밑에 직접 실행시켰을 때만 실행되는 명령들을 넣어준다.
    # dept01_create()
    dept01_insert(50, 'PD', '강남')
    dept01_query('%ING')
​
    dept01_update(50, 'Playdata','남터')
    dept01_query('%ING')  
​
    dept01_delete(50)
    dept01_query('%ING')
    # dept01_query()