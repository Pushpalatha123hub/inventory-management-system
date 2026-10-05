import psycopg2


def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="inventory_db",
        user="postgres",
        password="Pushpa@2702",
        port="5432"
    )