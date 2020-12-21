import psycopg2
from datetime import datetime

# conn = psycopg2.connect('dbname=test')

conn = psycopg2.connect('host=192.168.1.113 user=postgres  dbname=test')
cur = conn.cursor()

i = 1

def get_all(db):
    query = "SELECT * FROM " +  db
    cur.execute(query, )
    return cur.fetchall()

def add_sensor(temp, humidity, date, remark):
    query = """
    INSERT INTO
        temprature_sensor (temp, humidity, date, remark)
    VALUES
        (%s, %s, %s, %s)
    """
    values = (temp, humidity, date, remark)
    cur.execute(query, values)
    conn.commit()

# add_sensor(0.1, 0.2, datetime.now(), 'remark')

results = get_all('temprature_sensor')

for result in results:
    i += 1
    print(result)

'''
SELECT id, temp, humidity, date, remark
	FROM public.temprature_sensor;

    \\P110\www\data\sensor\1
'''