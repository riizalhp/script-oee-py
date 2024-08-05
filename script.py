# import mysql.connector
import psycopg2
import time
from datetime import datetime

# Konfigurasi koneksi ke database MySQL
# config = {
#     'user': 'root',
#     'password': '',
#     'host': 'localhost',
#     'database': 'oee_dashboard'
# }

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
		"line_produksi" : "A01",
		"nama_line" : "Assy Line A",
		"tgl_produksi" : "2024-08-01",
		"shift_produksi" : "1",
		"tipe_barang" : "AAH",
		"timestamp_capture" : "2024-08-01 12:06:00"
	},
	{
		"line_produksi" : "A01",
		"nama_line" : "Assy Line A",
		"tgl_produksi" : "2024-08-01",
		"shift_produksi" : "1",
		"tipe_barang" : "AAH",
		"timestamp_capture" : "2024-08-01 12:10:00"
	},
	{
		"line_produksi" : "A01",
		"nama_line" : "Assy Line A",
		"tgl_produksi" : "2024-08-01",
		"shift_produksi" : "1",
		"tipe_barang" : "AAH",
		"timestamp_capture" : "2024-08-01 12:20:00"
	},
	{
		"line_produksi" : "A01",
		"nama_line" : "Assy Line A",
		"tgl_produksi" : "2024-08-01",
		"shift_produksi" : "1",
		"tipe_barang" : "AAH",
		"timestamp_capture" : "2024-08-01 12:26:00"
	},
	{
		"line_produksi" : "A01",
		"nama_line" : "Assy Line A",
		"tgl_produksi" : "2024-08-01",
		"shift_produksi" : "1",
		"tipe_barang" : "AAH",
		"timestamp_capture" : "2024-08-01 12:29:00"
	},
	{
		"line_produksi" : "A01",
		"nama_line" : "Assy Line A",
		"tgl_produksi" : "2024-08-01",
		"shift_produksi" : "1",
		"tipe_barang" : "AAH",
		"timestamp_capture" : "2024-08-01 12:32:00"
	},
	{
		"line_produksi" : "A01",
		"nama_line" : "Assy Line A",
		"tgl_produksi" : "2024-08-01",
		"shift_produksi" : "1",
		"tipe_barang" : "AAH",
		"timestamp_capture" : "2024-08-01 12:35:00"
	},
	{
		"line_produksi" : "A01",
		"nama_line" : "Assy Line A",
		"tgl_produksi" : "2024-08-01",
		"shift_produksi" : "1",
		"tipe_barang" : "AAH",
		"timestamp_capture" : "2024-08-01 12:40:00"
	},
	{
		"line_produksi" : "A01",
		"nama_line" : "Assy Line A",
		"tgl_produksi" : "2024-08-01",
		"shift_produksi" : "1",
		"tipe_barang" : "AAH",
		"timestamp_capture" : "2024-08-01 12:43:00"
	},
	{
		"line_produksi" : "A01",
		"nama_line" : "Assy Line A",
		"tgl_produksi" : "2024-08-01",
		"shift_produksi" : "1",
		"tipe_barang" : "AAH",
		"timestamp_capture" : "2024-08-01 12:46:00"
	},
	{
		"line_produksi" : "A01",
		"nama_line" : "Assy Line A",
		"tgl_produksi" : "2024-08-01",
		"shift_produksi" : "1",
		"tipe_barang" : "AAH",
		"timestamp_capture" : "2024-08-01 12:51:00"
	},
	{
		"line_produksi" : "A01",
		"nama_line" : "Assy Line A",
		"tgl_produksi" : "2024-08-01",
		"shift_produksi" : "1",
		"tipe_barang" : "AAH",
		"timestamp_capture" : "2024-08-01 12:55:00"
	},
	{
		"line_produksi" : "A01",
		"nama_line" : "Assy Line A",
		"tgl_produksi" : "2024-08-01",
		"shift_produksi" : "1",
		"tipe_barang" : "AAH",
		"timestamp_capture" : "2024-08-01 13:00:00"
	},
]

try:
    # Membuat koneksi ke database
    # cnx = mysql.connector.connect(**config)
    cnx = psycopg2.connect(**config)
    cursor = cnx.cursor()

    # Query untuk memasukkan data
    # insert_query = ("INSERT INTO productions "
    #                 "(line_produksi, nama_line, tgl_produksi, shift_produksi, tipe_barang, timestamp_capture) "
    #                 "VALUES (%s, %s, %s, %s, %s, %s)")
    insert_query = """
    	INSERT INTO productions (line_produksi, nama_line, tgl_produksi, shift_produksi, tipe_barang, timestamp_capture, created_at, updated_at)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

    # Memasukkan data datu per satu setiap 1 menit
    # for data in data_list:
    #     cursor.execute(insert_query, (data['line_produksi'], data['nama_line'], data['tgl_produksi'], data['shift_produksi'], data['tipe_barang'], data['timestamp_capture']))
    #     cnx.commit()
    #     print(f"Data Inserted: {data}")
    #     time.sleep(120)
    for data in data_list:
        timestamp_capture = datetime.strptime(data['timestamp_capture'], '%Y-%m-%d %H:%M:%S')
        current_time = datetime.now()
        delay_seconds = (timestamp_capture - current_time).total_seconds()
        if delay_seconds > 0:
            print(f"Waiting for {delay_seconds} seconds until {timestamp_capture} to insert data.")
            time.sleep(delay_seconds)
        cursor.execute(insert_query, (data['line_produksi'], data['nama_line'], data['tgl_produksi'], data['shift_produksi'], data['tipe_barang'], data['timestamp_capture'], current_time, current_time))
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