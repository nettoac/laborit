from config import db_config
import logging
import pymysql


def execute_query(query):
    logging.info(f"Executando a consulta: {query}")
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    try:
        cursor.execute(query)
        results = cursor.fetchall()

        # Arredonda valores numéricos para duas casas decimais
        for row in results:
            for key, value in row.items():
                if isinstance(value, float):
                    row[key] = f"{value:.2f}"
    except pymysql.MySQLError as e:
        logging.error(f"Error executing query: {e}")
        results = None
    cursor.close()
    connection.close()
    return results
