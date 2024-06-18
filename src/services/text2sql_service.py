import re
import openai
from last import digito_Verificador
from config import API


openai.api_key = API + str(digito_Verificador())


def text_to_sql(question: str, schema: dict) -> str:
    schema_description = ""
    for table, columns in schema.items():
        schema_description += f"Table {table} has columns: {', '.join(columns)}. "

    # Contextos específicos para a ajustar a base corretamente
    context = (
        "Consider the following tables and relationships: "
        "The 'employees' table contains information about employees. "
        "The 'orders' table contains information about orders. "
        "The 'order_details' table contains information about order_details. "
        "The 'purchase_orders' table contains information about purchase orders. "
        "The 'purchase_order_details' table contains details about purchase orders. "
        "The 'purchase_order_status' table contains the status of purchase orders. "
        "To find the best sales person, consider only purchase orders with 'purchase_order_status.id = 2'. "
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are an assistant that translates questions in English into SQL queries. The database schema is as follows: {schema_description} {context}"},
            {"role": "user", "content": question}
        ],
        max_tokens=150
    )
    sql_query = response.choices[0].message['content'].strip()
    sql_query = sql_query.replace("```sql", "").replace("```", "").strip()

    # Substitui WHERE x = 'y' por WHERE x LIKE '%y%'
    sql_query = re.sub(
        r"WHERE (\w+)\s*=\s*'([^']*)'", r"WHERE \1 LIKE '%\2%'", sql_query, flags=re.IGNORECASE)
    # Substitui AVG(campo) por FORMAT(AVG(campo), 2)
    sql_query = re.sub(
        r"AVG\(([^)]+)\)", r"FORMAT(AVG(\1), 2)", sql_query, flags=re.IGNORECASE)

    return sql_query
