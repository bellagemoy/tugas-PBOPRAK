import psycopg2

conn = psycopg2.connect(
    user="postgres",
    password="postgres",
    host="localhost",
    database="pbop12-3"
)

cur = conn.cursor()

cur.execute("INSERT INTO gaji VALUES('Januari','TABIA HANURAL',17,0,1,0,5,1000000)")
cur.execute("INSERT INTO gaji VALUES('Juni','ARHAN PRATAMA',11,4,2,3,5,750000)")
cur.execute("INSERT INTO gaji VALUES('Desember','SADDIL RAMDANI',10,2,4,3,1,500000)")

conn.commit()
cur.close()
conn.close()