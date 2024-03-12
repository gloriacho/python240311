import sqlite3

#연결 인스턴스
#con = sqlite3.connect(":memory:")
con = sqlite3.connect("c:\\work\\demo.db")
cur = con.cursor()
cur.execute("create table if not exists PhoneBook (name text, phoneNum text);")

cur.execute("insert into PhoneBook values ('홍길동','010-222');")

name = "박문수"
phoneNum = "010-123"
cur.execute("insert into PhoneBook values (?,?);",(name, phoneNum))

datalist = (("tom","010-333"),("ddd","010-444"))
cur.executemany("insert into PhoneBook values (?,?);",datalist)
cur.execute("select * from PhoneBook")

for row in cur:
    print(row)