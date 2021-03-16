import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()
database = os.environ.get("postgresql_db")
user = os.environ.get("postgresql_user")
password = os.environ.get("postgresql_pass")
host = os.environ.get("postgresql_host")
port = os.environ.get("postgresql_port")

def open_connection(database=database, user=user, password=password, host=host, port=port):
    conn = psycopg2.connect(
        database = database,
        user = user,
        password = password,
        host = host,
        port = port
        )
    return conn

def create_products_table_in_cafe_db():
    try:
        connection = open_connection()
        with connection.cursor() as cursor:
            postgresql = """CREATE TABLE IF NOT EXISTS products (
                            product_id SERIAL PRIMARY KEY NOT NULL,
                            product_name VARCHAR(100) NOT NULL,
                            product_price DECIMAL(6,2) NOT NULL
                            )"""
            cursor.execute(postgresql)
            connection.commit()
        connection.close()
    except Exception as e:
        print("An error occurred when attempting to create the products table: " + str(e))

def create_cafe_locations_table_in_cafe_db():
    try:
        connection = open_connection()
        with connection.cursor() as cursor:
            postgresql = """CREATE TABLE IF NOT EXISTS cafe_locations (
                            location_id SERIAL PRIMARY KEY NOT NULL,
                            location VARCHAR(100) NOT NULL
                            )"""
            cursor.execute(postgresql)
            connection.commit()
        connection.close()
    except Exception as e:
        print("An error occurred when attempting to create the cafe_locations table: " + str(e))

def create_orders_table_in_cafe_db():
    try:
        connection = open_connection()
        with connection.cursor() as cursor:
            postgresql = """CREATE TABLE IF NOT EXISTS orders (
                            order_id SERIAL PRIMARY KEY NOT NULL,
                            date DATE NOT NULL,
                            time TIME NOT NULL,
                            location_id INT NOT NULL REFERENCES cafe_locations,
                            order_price DECIMAL(6,2) NOT NULL
                            )"""
            cursor.execute(postgresql)
            connection.commit()
        connection.close()
    except Exception as e:
      print("An error occurred when attempting to create the orders table: " + str(e))

def create_products_in_orders_table_in_cafe_db():
    try:
        connection = open_connection()
        with connection.cursor() as cursor:
            postgresql = """CREATE TABLE IF NOT EXISTS products_in_orders (
                            order_id INT NOT NULL REFERENCES orders,
                            product_id INT NOT NULL REFERENCES products
                            )"""
            cursor.execute(postgresql)
            connection.commit()
        connection.close()
    except Exception as e:
        print("An error occurred when attempting to create the products_in_orders table: " + str(e))


create_products_table_in_cafe_db()
create_cafe_locations_table_in_cafe_db()
create_orders_table_in_cafe_db()
create_products_in_orders_table_in_cafe_db()