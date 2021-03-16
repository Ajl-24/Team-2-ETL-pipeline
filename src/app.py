import csv 
import src.transform as transform
import src.db as db

file_name = "/workspace/src/2021-02-23-isle-of-wight.csv"

def read_file(file_name = file_name):
    data = []
    try:
        with open(file_name, mode = 'r') as file:
            # Opens the csv file of file_name
            field_names = ['date_time', 'location', 'customer_name', 'products', 'payment_method', 'total', 'card_details']
            reader = csv.DictReader(file, fieldnames = field_names)
            data = append_to_list(reader,data)
    except Exception as e:
        print('An error occurred when attempting to read the csv file ' + str(e))
        return
    return data

def append_to_list(reader,cached_list):
    for line in reader:
        cached_list.append(dict(line))    
    return cached_list

csv_data = read_file()

iow_data = transform.Transform(csv_data)

if __name__ == '__main__':

    db.create_products_table_in_cafe_db()
    db.create_cafe_locations_table_in_cafe_db()
    db.create_orders_table_in_cafe_db()
    db.create_products_in_orders_table_in_cafe_db()
    
    iow_data.remove_names()
    iow_data.remove_payment_details()
    iow_data.split_date_time()

    iow_order_data = iow_data.data.copy()

    db.load_into_cafe_locations_table(iow_order_data[0]['location'])
    db.load_into_orders_table(iow_order_data)
    
    iow_data.add_id()
    iow_data.split_products()   
    iow_data.split_product_price()
    iow_data.sort_by_id()

    db.load_into_products_table(iow_data.data)
    # db.load_into_orders_in_products_table()