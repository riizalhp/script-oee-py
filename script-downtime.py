# import mysql.connector
import psycopg2
import time
from datetime import datetime

# Konfigurasi koneksi ke database PostgreSQL
config = {
    'user': 'postgres',
    'password': '123',
    'host': 'localhost',
    'port': 5432,
    'database': 'oee_dashboard'
}

# Data yang ingin dimasukkan
data_list = [
    {
		"downtimeid" : "ST",
        "downtimedesc" : "Startup",
		"mulai" : "2024-08-01 12:00:00",
		"selesai" : "2024-08-01 12:03:00",
		"duration" : "3"
	},
	{
		"downtimeid": "ID",
        "downtimedesc" : "Downtime",
		"mulai" : "2024-08-01 12:11:00",
		"selesai" : "2024-08-01 12:15:00",
		"duration" : "4"
	}
]

try:
    cnx = psycopg2.connect(**config)
    cursor = cnx.cursor()

    insert_query = """
    	INSERT INTO downtimes (downtimeid, downtimedesc, mulai, selesai, duration, created_at, updated_at)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

    for data in data_list:
        mulai = datetime.strptime(data['mulai'], '%Y-%m-%d %H:%M:%S')
        current_time = datetime.now()
        delay_seconds = (mulai - current_time).total_seconds()
        if delay_seconds > 0:
            print(f"Waiting for {delay_seconds} seconds until {mulai} to insert downtime.")
            time.sleep(delay_seconds)
        cursor.execute(insert_query, (data['downtimeid'], data['downtimedesc'], data['mulai'], data['selesai'], data['duration'], current_time,current_time))
        cnx.commit()
        print(f"Data inserted: {data}")

# except mysql.connector.Error as err:
#     print(f"Error: {err}")
except psycopg2.Error as err:
     print(f"Error: {err}")

finally:
    cursor.close()
    cnx.close()

print("All Data has been inserted.")