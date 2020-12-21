import csv
import psycopg2
conn = psycopg2.connect('host=192.168.1.113 user=postgres  dbname=test')
cur = conn.cursor()
with open('/www/data/sensor/2/log20201218.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        row[1] = row[1].replace('%','')
        print(row)
        cur.execute(
        "INSERT INTO temprature_sensor (sensor_no, temp, humidity, date, remark) VALUES (2, %s, %s, %s, %s)",
        row
    )
conn.commit()