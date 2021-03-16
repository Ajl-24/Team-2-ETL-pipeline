import os
import psycopg2
from dotenv import load_dotenv

def open_connection():
    load_dotenv()
    database = os.environ.get("postgresql_db")
    user = os.environ.get("postgresql_user")
    password = os.environ.get("postgresql_pass")
    host = os.environ.get("postgresql_host")
    port = os.environ.get("postgresql_port")
    
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
       
def fetch_location_data():
    new_list = []
    try:
        connection = open_connection()
        with connection.cursor() as cursor:
            postgresql = "SELECT * from cafe_locations"
            cursor.execute(postgresql)
            rows = cursor.fetchall()
            for row in rows:
                new_dict = {'location_id': int, 'location': str}
                new_dict['location_id'] = row[0]
                new_dict['location'] = row[1]
                new_list.append(new_dict)
            cursor.close()
    except Exception as e:
        print("An error occurred when attempting to fetch data from the cafe_locations table: " + str(e))

    return new_list

def fetch_product_data():                   ######   MORNING VIBE   #####
    pass
    # new_list = []
    # try:
    #     connection = open_connection()
    #     with connection.cursor() as cursor:
    #         postgresql = "SELECT * from products"
    #         cursor.execute(postgresql)
    #         rows = cursor.fetchall()
    #         for row in rows:
    #             new_dict = {'product_id': int, 'product': str}
    #             new_dict['product_id'] = row[0]
    #             new_dict['product'] = row[1]
    #             new_list.append(new_dict)
    #         cursor.close()
    # except Exception as e:
    #     print("An error occurred when attempting to fetch data from the products table: " + str(e))

    # return new_list

def load_into_cafe_locations_table(location):
    try:
        connection = open_connection()
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO cafe_locations (location) VALUES ('{}')".format(location))
            connection.commit()
        connection.close()
    except Exception as e:
        print("An error occurred when attempting to load data into the cafe_locations table: " + str(e))

def load_into_orders_table(iow_order_data):
    new_list = fetch_location_data()
    try:
        connection = open_connection()
        with connection.cursor() as cursor:
            for dictionary in iow_order_data:
                for new_dict in new_list:
                    if dictionary['location'] == new_dict['location']:
                        postgresql = "INSERT INTO orders (date, time, location_id, order_price) VALUES ('{}', '{}', '{}', '{}')".format(dictionary['date'], dictionary['time'], new_dict['location_id'], dictionary['total'])
                        cursor.execute(postgresql)
                        connection.commit()
        connection.close()
    except Exception as e:
        print("An error occurred when attempting to load data into the orders table: " + str(e))

def load_into_products_table(iow_order_data):
    unique_product_list = sorted(list(set((order_dict['product'], order_dict['product_price']) for order_dict in iow_order_data)))
    try:
        connection = open_connection()
        with connection.cursor() as cursor:
            for product in unique_product_list:
                cursor.execute("INSERT INTO products (product_name, product_price) VALUES ('{}', '{}')".format(product[0], product[1]))
                connection.commit()
        connection.close()
    except Exception as e:
        print("An error occurred when attempting to load data into the products table: " + str(e))

def load_into_orders_in_products_table(iow_order_data):
    unique_product_list = sorted(list(set((order_dict['product'], order_dict['product_price']) for order_dict in iow_order_data)))