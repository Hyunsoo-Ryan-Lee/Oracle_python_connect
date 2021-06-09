from book_info import Book
import cx_Oracle
'''
화면을 통해 book 정보 등록
-> data 획득 및 book 객체 생성 -> db에 저장
'''

# Oracle DB에 insert
def book_insert(book):
    connection = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
    cur = connection.cursor()

    print(cur)
    cur.execute("insert into book values\
        (seq_book_no.nextval, :a, :b, :price)"\
        ,a=book.getTitle(), b=book.getAuthor(),price=book.getPrice())
    connection.commit()

    cur.close()
    connection.close()


def book_update(book):
    connection = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
    cur = connection.cursor()

    # cur.execute("update book set title = 'HTML/CCS' where substr(title,1,2)='Py'")
    cur.execute("update book set author = :author, price = :price where title = :title",\
        author=book.getAuthor(), price=book.getPrice(), title=book.getTitle())
    
    connection.commit()
    cur.close()
    connection.close()



if __name__ == '__main__':
    # book_insert(Book('가나다','마바사',40))
    # book_insert(Book('JAVA script','Java Team',2500))
    book_update(Book('JAVA','JavaTeam01',2100))
