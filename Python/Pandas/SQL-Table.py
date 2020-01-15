import sqlite3 as sql
from pandas import DataFrame
#Data it is 2 Columns and 5 Rows
data = {
    'Name':['huzifa','ajmed','jaber','salim','sam','Ye'], # NeedFul, Name list same name column at Database
    'Age':[20,30,32,17,19,22]  # Some Name at database
}
con = sql.connect('data.db')
# Delete Table if Founded
con.execute('DROP TABLE Data')
con.commit()
con.execute('CREATE TABLE Data (Name text, Age number)')
con.commit()
DF = DataFrame(data, columns=['Name','Age'])
#if_exists if data already add will delete him and add
DF.to_sql('Data', con,if_exists='replace', index=False)
# for show all data from Data Table
t = con.execute("SELECT * FROM Data")
for x in t.fetchall():
    print(x)
