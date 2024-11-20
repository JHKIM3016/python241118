# db3.py
import sqlite3

#메모리상에 DB를 생성
#물리적인 파일로 변경
con=sqlite3.connect(r"c:\work\sample2.db")
#커서객체를 리턴, 커서:반환되는 결과값을 저장하는 메모리 공간
cur=con.cursor()
#검색
cur.execute("select * from Employee;")
print(cur.fetchall())

#연결 객체에서 commit() 호출

