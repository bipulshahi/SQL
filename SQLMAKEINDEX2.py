import mysql.connector

mydb=mysql.connector.connect(host = 'localhost',
                             user='root',
                             password='725@Mysql',
                             database='db1')

cur = mydb.cursor()

curvalues = []     #place to store list of current index values (from book table)
print("Original book table")
sql = "SELECT * from book"
cur.execute(sql)

result = cur.fetchall()
for rec in result:
    curvalues.append((rec[1],rec[2]))   #pulls title and price to identify unique records
    print(rec)

print(curvalues)
print("_____________________________")

sql = "SELECT COUNT(*) from book"
cur.execute(sql)
result = cur.fetchone()
len = result[0]    #gets number of rows in book table
skuids = []
print(result)
print(len)

print("===========")

#print(type(skuids))
rowno = 1
while rowno <= len:
    skuids.append(rowno)
    rowno += 1     # built list with skuids - currently [1..6]

print(skuids)
print("===========")

#for each of our rows, assign sku_id to ski where it matches the title and price
for skid in skuids:
    print(skid)
    sql = "UPDATE book SET sku_id = "+str(skid)+" WHERE title = '"+curvalues[skid-1][0]+"' AND price = "+str(curvalues[skid-1][1])
    print(sql)
    cur.execute(sql)
    rowno += 1
    
mydb.commit()

print("Modified database")
sql = "SELECT * from book"
cur.execute(sql)
result = cur.fetchall()
for rec in result:
    print(rec)



