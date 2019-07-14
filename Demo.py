import sqlite3

# Open database connection
conn = sqlite3.connect('test.db')

# prepare a cursor object using cursor() method
c = conn.cursor()

'''
c.execute("DROP TABLE bgpstock")
c.execute('CREATE TABLE bgpstock(bldgrp TEXT,packet NUMBER)')
c.execute("DROP TABLE DonorInfo")
c.execute("DROP TABLE BuyerInfo")
c.execute('CREATE TABLE DonorInfo(dno INTEGER PRIMARY KEY AUTOINCREMENT,dname TEXT NOT NULL,age NUMBER,dgender TEXT,dcity TEXT,dbldgrp TEXT,date DATE)')
c.execute('CREATE TABLE BuyerInfo(bno INTEGER PRIMARY KEY AUTOINCREMENT,bname TEXT NOT NULL,age NUMBER,bgender TEXT,bcity TEXT,bbldgrp TEXT,date DATE)')
'''


c.execute("SELECT * FROM sqlite_master where type='table'")
result=c.fetchall()
for row in result:
   print(row)

'''
c.execute("INSERT INTO bgpstock VALUES('A',0)")
c.execute("INSERT INTO bgpstock VALUES('B',0)")
c.execute("INSERT INTO bgpstock VALUES('AB',0)")
c.execute("INSERT INTO bgpstock VALUES('O',0)")
c.execute("SELECT * FROM bgpstock")
'''
result=c.fetchall()
for r in result:
   print(r)
a="Sultan"
b="21"
d="Male"
f="Dapoli"
e="B"
#c.execute("INSERT INTO DonorInfo(dname,age,dgender,dcity,dbldgrp,ddate) VALUES('"+a+"',"+b+",'"+d+"','"+f+"','"+e+"',date('now'))")
c.execute("SELECT * FROM DonorInfo")
result=c.fetchall()
for r in result:
   print(r)

c.execute("SELECT * FROM BuyerInfo")
result=c.fetchall()
for r in result:
   print(r)



c.execute("SELECT packet FROM bgpstock WHERE bldgrp='"+e+"'")
res=c.fetchone()
print(res)
q=res[0]
print(q)
q+=1
q=str(q)
print(q)
#c.execute("UPDATE bgpstock SET packet="+q+" WHERE bldgrp='"+e+"'")
conn.commit()
c.close()
conn.close()


