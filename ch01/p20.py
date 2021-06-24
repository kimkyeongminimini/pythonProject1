import sqlite3
from libs.db.dba import getConn

class Db:
    # 클래스 변수
    conn = getConn('c:/test/phone.db')  # 커넥션을 가지고 옵니다.
    cur  = conn.cursor()                # 커넥션을 이용해서 커서를 생성합니다.

    def createtable(self):              # 테이블 생성
        Db.cur.execute('''
        create table tell(name text, no text)
        ''')

    def insert(self):
        self.name = input('이름?')
        self.no = input('전화번호?')
        self.sql = '''
        insert into tell values(?,?)
        '''
        Db.cur.execute(self.sql,
                       (self.name, self.no))

    def select(self):
        self.sql = 'select * from tell'
        Db.cur.execute(self.sql)
        rs = Db.cur.fetchall()
        print('*****데이터출력*****')

        for k, v in rs:
            print(k, v)

    def delete(self):
        self.name = input('이름?')
        self.sql = 'delete from tell where name=?'
        Db.cur.execute(self.sql, (self.name,))

    def update(self):
        self.name = input('이름?')
        self.no = input('번호?')
        self.sql = 'update tell set no=? where name=?'
        Db.cur.execute(self.sql, (self.no,self.name))

def main():
    d = Db()  # 클래스 객체 생성

    while True:
        n = input('''a.테이블생성 1.입력 2.조회 3.삭제 4.수정 0.종료:''')

        if n=='a':
            d.createtable()
        if n=='1':
            d.insert()
        if n=='2':
            d.select()
        if n=='3':
            d.delete()
        if n=='4':
            d.update()
        if n=='0':
            d.conn.commit()
            d.conn.close()
            break
    print('프로그램을 종료합니다.')

if __name__=='__main__':
    main()