import sqlite3
con=sqlite3.Connection('PYthonBusProj.db')

cur=con.cursor()

cur.execute("""select * from bus""")
test=cur.fetchall()
print(test)
cur.execute("""select op.name,b.bus_type,r.seat_available,b.capacity,b.fare,b.bus_opid,st.stid ,ed.stid from operator as op,bus as b,route as st,route as ed,runs as r """)
#where r.runs_date='2022-12-17' and st.station_name='Guna' and ed.station_name='Jaipur')
res=cur.fetchall()
print('result',res)
