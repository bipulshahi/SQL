import pandas as pd
import mysql.connector

df = pd.read_csv('/Users/bipulkumar/Downloads/Maternal Health Risk Data Set.xls')

#Coonection with server and database
connection = mysql.connector.connect(host="localhost",
                                     user="root",
                                     password="725@Mysql",
                                     database="idb2");

#defining cursr to execute command
cursor = connection.cursor()

for index,row in df.iterrows():
    query = "insert into mt_risk values (%s,%s,%s,%s,%s,%s,%s)"
    value = (row['Age'],row['SystolicBP'],row['DiastolicBP'],row['BS'],row['BodyTemp'],row['HeartRate'],row['RiskLevel'])
    cursor.execute(query,value)
    #print(value , type(value))
    #print(f"Row {index} added")
    
connection.commit()
connection.close()


