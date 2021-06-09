from camera_info import Camera
import cx_Oracle

def look_all():
    connection = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
    cur = connection.cursor()
    cur.execute('select * from camera')

    for i in cur:
        print(*i)

    connection.commit()
    cur.close()
    connection.close()


def c_insert(cams):
    connection = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
    cur = connection.cursor()
    cur.execute("insert into camera values (:a, :b, :c,:d)",\
        a=cams.getBrand(), b=cams.getModel(), c=cams.getPrice(), d=cams.getFormat())

    connection.commit()
    cur.close()
    connection.close()

def c_update(cams):
    connection = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
    cur = connection.cursor()
    cur.execute("update camera set model=:b, price=:c, format=:d where brand=:a"\
        ,b=cams.getModel(), c=cams.getPrice(), d=cams.getFormat(), a=cams.getBrand())

    connection.commit()
    cur.close()
    connection.close()

def c_delete(cams):
    connection = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
    cur = connection.cursor()
    cur.execute("delete from camera where brand=:a",a=cams.getBrand())

    connection.commit()
    cur.close()
    connection.close()


if __name__ == '__main__':
    # look_all()
    # c_insert(Camera('Zenit','ET',10,135))
    # c_update(Camera('Zenit','TTL',15,135))
    # c_delete(Camera('Zenit','sdf',132,23))

    c = Camera('펜탁스','미슈퍼',20,135)

    print(c.setFormat(110))
    print(c.getFormat())
    