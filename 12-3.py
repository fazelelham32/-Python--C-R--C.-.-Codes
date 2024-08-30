
# Created by Hamidreza Talebi 
 
import sqlite3

def main():
    db=sqlite3.connect('test.db')
    db.execute('drop table if exists test')
    db.row_factory=sqlite3.Row
    db.execute('Create table test (t1 text, t2 int)')
    
    db.execute('insert into test(t1,t2) values(?,?)',('one',1))    
    db.execute('insert into test(t1,t2) values(?,?)',('two',2))
    db.execute('insert into test(t1,t2) values(?,?)',('three',3))    
    db.execute('insert into test(t1,t2) values(?,?)',('four',4)) 
    db.commit()
    
    cursor=db.execute('Select * from test order by t1')
    for row in cursor:
        print(dict(row))

if __name__ == "__main__": main()







