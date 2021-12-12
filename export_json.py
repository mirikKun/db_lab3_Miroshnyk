import json
import psycopg2

username = 'postgres'
password = ''
database = 'postgres'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(user=username, password=password, dbname=database)
cursor = conn.cursor()


get_all_tables_query = '''
SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
              AND table_type = 'BASE TABLE'
'''


def json_export():
    cursor.execute(get_all_tables_query)
    tables = []

    for row in cursor:
        tables.append(str(row[0]))

    jsonData = {}
    path = 'exports/data.json'

    for table in tables:
        cursor.execute('SELECT * FROM ' + table)
        headers = [x[0] for x in cursor.description]
        rows = []
        for row in cursor:
            rows.append(dict(zip(headers, row)))
            jsonData[table] = rows

    with open(path, 'w') as file:
        json.dump(jsonData, file, default=str)

json_export()