import csv
import os
import src.db as db
import src.transform as transform

'''
birm_file = "/workspace/src/birmingham_23-03-2021_09-00-00.csv"
ches_file = "/workspace/src/chesterfield_23-03-2021_09-00-00.csv"

def read_file(file_name):
    data = []
    try:
        with open(file_name, mode = 'r') as file:
            # Opens the csv file of file_name
            field_names = ['date_time', 'location', 'customer_name', 'products', 'total', 'payment_method', 'card_details']
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

birm_data = read_file(birm_file)
ches_data = read_file(ches_file)
'''

def start_transformation(csv_data):

    birm_data = transform.Transform(csv_data)

    if __name__ == '__main__':
    
        db.create_products_table_in_cafe_db()
        db.create_cafe_locations_table_in_cafe_db()
        db.create_orders_table_in_cafe_db()
        db.create_products_in_orders_table_in_cafe_db()
        
        birm_data.remove_names()
        birm_data.remove_payment_details()
        birm_data.split_date_time()
        birm_data.reverse_date()
        birm_data.add_id()
        
        db.load_into_cafe_locations_table(birm_data.data)
        db.load_into_orders_table_and_update_local_ids(birm_data.data)
        
        birm_data.split_products()   
        birm_data.split_product_price()
        birm_data.sort_by_id()
        
        db.load_into_products_table(birm_data.data)
        db.load_into_products_in_orders_table(birm_data.data)
        
# start_transformation(birm_data)
# start_transformation(ches_data)