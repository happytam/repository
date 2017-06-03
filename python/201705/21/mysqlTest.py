import pymysql
conn = pymysql.connect(host='127.0.0.1',unix_socket='/tmp/mysql.sock',user='root',passwd='combaecos',db='mysql')
cur = conn.cursor()
cur.execute("show databases")
print(cur.fetchone())
cur.close()
conn.close()
