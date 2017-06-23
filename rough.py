__author__ = 'user'
from connection import con,cur
import datetime
import cx_Oracle
import getpass
import sys
import msvcrt



"""try:
    sql = "insert into rgh values (1000000)"
    cur.execute(sql)
    con.commit()
except cx_Oracle.DatabaseError as e:
    print(e)
    print("Sorry something went wrong")"""

def a(p):
    print(p)

p = getpass.getpass("Enter pwd")
a(p)

#print(p)
#sql = "select months_between(opened_on,sysdate+35) from accounts where account_no = 2"
#sql = "select add_months(sysdate,1) from dual"
#cur.execute(sql)
#res = cur.fetchall()
#date = res[0][0].strftime("%d-%b-%Y")
#aa = res[0][0].strftime("%d-%b-%Y")
#print(aa)
#print(date)
#curr_date = datetime.datetime.now().strftime("%d-%b-%Y")
#print(curr_date-date)