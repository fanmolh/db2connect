linux 下连接db2，并执行sql的二进制命令！

./db2 -h
  Options:
  -h, --help            show this help message and exit
  -i IP, --ip=IP        
  -p PORT, --port=PORT  DB2 port ,default 50000
  -u UID, --uid=UID     
  -P PWD, --pwd=PWD     
  -d DBNAME, --dbname=DBNAME
  -s SQL, --sql=SQL     
  -f FORMAT, --format=FORMAT
                        Py file for data formatting

./db2 -i 172.17.0.3 -u db2inst1 -P db.2.admin -s 'select * from emp limit 10' -f ./test.py

