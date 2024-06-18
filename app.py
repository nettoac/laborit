from flask import Flask, request, render_template, jsonify
from src.database.get_schema import get_db_schema
from src.services.execute_service import execute_query
from src.services.text2sql_service import text_to_sql
import logging


app = Flask(__name__)


# Configuração do logger
logging.basicConfig(level=logging.INFO)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ask', methods=['POST'])
def ask():
    question = request.form['question']
    schema = get_db_schema()
    sql_query = text_to_sql(question, schema)
    logging.info(f"Generated SQL query: {sql_query}")
    results = execute_query(sql_query)
    if results is None:
        return jsonify({'error': "The query did not return any results at this time, please try again later."}), 400
    return jsonify({'results': results})


if __name__ == '__main__':
    app.run(debug=True)
