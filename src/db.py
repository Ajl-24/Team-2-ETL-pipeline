import os
import psycopg2
# from dotenv import load_dotenv ?

def create_orders_table_in_cafe_db():
    try:
        connection = psycopg2.connect(database='cafe_db', user='root', password='password', host='172.21.0.3', port='5432')
        with connection.cursor() as cursor:
            postgresql = """
            CREATE TABLE IF NOT EXISTS orders (
            order_id SMALLSERIAL PRIMARY KEY NOT NULL,
            date_id INT NOT NULL,
            time TIME NOT NULL,
            location_id INT NOT NULL,
            payment_type_id INT NOT NULL
            )
            """
            cursor.execute(postgresql)
            connection.commit()
        connection.close()
    except Exception as e:
      print("An error occurred when attempting to create the orders table: " + str(e))

def create_products_table_in_cafe_db():
    try:
        connection = psycopg2.connect(database='cafe_db', user='root', password='password', host='172.21.0.3', port='5432')
        with connection.cursor() as cursor:
            postgresql = """
            CREATE TABLE IF NOT EXISTS products (
            product_id SMALLSERIAL PRIMARY KEY NOT NULL,
            product_name VARCHAR(100) NOT NULL,
            price DECIMAL(6,2) NOT NULL
            )
            """
            cursor.execute(postgresql)
            connection.commit()
        connection.close()
    except Exception as e:
        print("An error occurred when attempting to create the products table: " + str(e))

def create_dates_table_in_cafe_db():
    try:
        connection = psycopg2.connect(database='cafe_db', user='root', password='password', host='172.21.0.3', port='5432')
        with connection.cursor() as cursor:
            postgresql = """
            CREATE TABLE IF NOT EXISTS dates (
            date_id SMALLSERIAL PRIMARY KEY NOT NULL,
            date DATE NOT NULL
            )
            """
            cursor.execute(postgresql)
            connection.commit()
        connection.close()
    except Exception as e:
        print("An error occurred when attempting to create the dates table: " + str(e))

def create_cafe_locations_table_in_cafe_db():
    try:
        connection = psycopg2.connect(database='cafe_db', user='root', password='password', host='172.21.0.3', port='5432')
        with connection.cursor() as cursor:
            postgresql = """
            CREATE TABLE IF NOT EXISTS cafe_locations (
            location_id SMALLSERIAL PRIMARY KEY NOT NULL,
            location VARCHAR(100) NOT NULL,
            )
            """
            cursor.execute(postgresql)
            connection.commit()
        connection.close()
    except Exception as e:
        print("An error occurred when attempting to create the cafe_locations table: " + str(e))

def create_payments_table_in_cafe_db(): # ???
    try:
        connection = psycopg2.connect(database='cafe_db', user='root', password='password', host='172.21.0.3', port='5432')
        with connection.cursor() as cursor:
            postgresql = """
            CREATE TABLE IF NOT EXISTS payments (
            payment_id SMALLSERIAL PRIMARY KEY NOT NULL,
            payment_method VARCHAR(10) NOT NULL
            )
            """
            cursor.execute(postgresql)
            connection.commit()
        connection.close()
    except Exception as e:
        print("An error occurred when attempting to create the payments table: " + str(e))

def create_products_in_orders_table_in_cafe_db():
    try:
        connection = psycopg2.connect(database='cafe_db', user='root', password='password', host='172.21.0.3', port='5432')
        with connection.cursor() as cursor:
            postgresql = """
            CREATE TABLE IF NOT EXISTS products_in_orders (
            order_id INT NOT NULL,
            product_id INT NOT NULL
            )
            """
            cursor.execute(postgresql)
            connection.commit()
        connection.close()
    except Exception as e:
        print("An error occurred when attempting to create the products_in_orders table: " + str(e))

def create_order_totals_table_in_cafe_db(): # name order_price_totals?
    try:
        connection = psycopg2.connect(database='cafe_db', user='root', password='password', host='172.21.0.3', port='5432')
        with connection.cursor() as cursor:
            postgresql = """
            CREATE TABLE IF NOT EXISTS order_totals (
            order_id INT NOT NULL,
            total_price DECIMAL(6,2) NOT NULL
            )
            """
            cursor.execute(postgresql)
            connection.commit()
        connection.close()
    except Exception as e:
        print("An error occurred when attempting to create the order_totals table: " + str(e))


create_orders_table_in_cafe_db()
create_products_table_in_cafe_db()
create_dates_table_in_cafe_db()
create_cafe_locations_table_in_cafe_db
create_payments_table_in_cafe_db()
create_products_in_orders_table_in_cafe_db()
create_order_totals_table_in_cafe_db()

# FOREIGN KEYS? Create clean data table to add FK?