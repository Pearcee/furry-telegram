import csv
import psycopg2
from datetime import datetime


conn = psycopg2.connect('host=192.168.1.113 user=postgres  dbname=test')
cur = conn.cursor()

# Temprature & Humitity

def import_sensor(filename):
    """
    docstring
    """
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader) # Skip the header row.
        for row in reader:
            row[1] = row[1].replace('%','')
            print(row)
            cur.execute(
            "INSERT INTO temprature_sensor (sensor_no, temp, humidity, date, remark) VALUES (2, %s, %s, %s, %s)",
        )
    conn.commit()

# import_sensor('/www/data/sensor/2/log20201218.csv')

# Speed test

def import_speedtest(filename):
    """
    docstring
    """
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader) # Skip the header row.
        # row = next(reader)
        
        #row[1]  row[1].replace('%','')
        #print(row)
        #pass
        for row in reader:
            print(row)
            server_id   = row[0]
            sponsor     = row[1]
            servername  = row[2]
            timestamp   = row[3] # '2020-11-22T16:00:02.660837Z'
            distance    = row[4] # 93.51556710689445
            ping        = row[5] # 27.78
            download    = row[6] # 43295626.029542044
            upload      = row[7] # 10264680.2969267
            share       = '' 
            ipaddress   = row[9] # '86.156.227.38'
            cur.execute(''' 
                INSERT INTO temprature_speedtest 
                    (server_id, sponsor, servername, timestamp, distance, ping, download, upload, share, ipaddress)   
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''', 
                    (server_id, sponsor, servername, timestamp, distance, ping, download, upload, share, ipaddress)
            )
    conn.commit()

# import_speedtest('/www/data/speedtest/202011.csv')
'''
    server_id, sponsor, servername, timestamp, distance, ping, download, upload, share, ipaddress
    '4058', 'Wildcard Networks', 'Newcastle upon Tyne', '2020-11-22T16:00:02.660837Z', '93.51556710689445', '27.78', '43295626.029542044', '10264680.2969267', '', '86.156.227.38'
'''
''' INSERT INTO temprature_speedtest 
    (server_id, sponsor, servername, timestamp, distance, ping, download, upload, share, ipaddress)             
VALUES (%s,'%s','%s','%s','%s','%s','%s','%s','%s','%s')'''

# online

def import_online(filename):
    """
    docstring
    """
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader) # Skip the header row.
        for row in reader:
            # print(row)
            cur.execute(
            "INSERT INTO temprature_online (timestamp, ipaddress, name) VALUES (%s, %s, %s)", (row[0], row[1], row[2].replace('.holm',''))
        )
    conn.commit()

import_online('/www/data//online/202011.csv')
''' 
 Online(models.Model):
    timestamp, ipaddress, name
'''
