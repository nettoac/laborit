import pymysql
from config import db_config


def get_db_schema():
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()

    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()

    schema = {}
    for (table,) in tables:
        cursor.execute(f"SHOW COLUMNS FROM {table}")
        columns = cursor.fetchall()
        schema[table] = [column[0] for column in columns]

    cursor.close()
    connection.close()

    return schema