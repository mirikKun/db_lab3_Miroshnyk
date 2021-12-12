import psycopg2

username = 'postgres'
password = ''
database = 'postgres'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
cursor = conn.cursor()

tables = {
    "steam_sale(sale_id,appid, discount)": "C:/Users/AndreyNote/Desktop/lab_3/imports/steam_sale.csv",
}

import_table_from_csv = "COPY {} FROM '{}' DELIMITER ',' CSV HEADER;"
with conn:
    cur = conn.cursor()
    for table, path in tables.items():
        cur.execute(import_table_from_csv.format(table, path))