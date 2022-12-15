import pyodbc

conn_str = ("Driver={SQL Server};"
            "Server=sqlserver\sqlinst1;"
            "Database=ClinicMaster;"
            "Trusted_Connection=yes;")
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
cursor.execute("SELECT TOP(1000) * FROM sometable")

for row in cursor:
    print(row)