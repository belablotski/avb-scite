import cx_Oracle
import os

#Get Oracle Instant Client (coherent with Oracle Server) from http://www.oracle.com/technetwork/database/features/instant-client/index-097480.html
#Get cx_Oracle (coherent with Oracle Instant Client and Python) from http://cx-oracle.sourceforge.net/
#set path=C:\Programs\ora_instantclient_11_2;%path%
#Configure TNS, if used
#See Python DB API 2.0 spec here http://www.python.org/dev/peps/pep-0249/

connstr = 'hr/hr@ORCL_VM1'
#connstr = 'SYSTEM/sql@EVBYMINSD0438:1521/orcl438.minsk.epam.com'
#connstr = 'BCRUAML_ST31/BCRUAML_ST3@EVBYMINSD0633:1521/BCRUAML'
#print cx_Oracle.version
conn = cx_Oracle.Connection(connstr)
curs = conn.cursor()

curs.execute('select * from DUAL')
print curs.description
for row in curs:
    print row
conn.close()