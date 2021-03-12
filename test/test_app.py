import sys
sys.path.append("..") # Goes back a level in the directory
import src.app as app
import src.transform as transform

"""
# Retired test for old requirement

def test_append_data():
    def mock_file():
        return ["2021-02-23 09:00:48","Isle of Wight","Morgan Berka","Large,Hot chocolate,2.9,Large,Chai latte,2.6,Large,Hot chocolate,2.9","CASH","8.40","None"]
    
    expected = ["2021-02-23 09:00:48","Isle of Wight","Morgan Berka","Large,Hot chocolate,2.9,Large,Chai latte,2.6,Large,Hot chocolate,2.9","CASH",8.40]
    actual = app.append_data(mock_file())
    
    assert actual == expected
"""
def test_append_to_list():

    def mock_reader():
        return [[('date_time', '2021-02-23 17:58:17'), ('location', 'Isle of Wight'), ('customer_name', 'Ramon Salters'), ('products', 'Regular,Americano,1.95,,Flat white,2.15,,Flavoured iced latte - Caramel,2.75'), ('payment_method', 'CASH'), ('total', '6.85'), ('card_details', 'None')], [('date_time', '2021-02-23 17:59:04'), ('location', 'Isle of Wight'), ('customer_name', 'Stanley Cordano'), ('products', ',Frappes - Coffee,2.75,,Speciality Tea - Darjeeling,1.3,,Smoothies - Berry Beautiful,2.0,Large,Latte,2.45'), ('payment_method', 'CASH'), ('total', '8.50'), ('card_details', 'None')]]
    def mock_cached_list():
        return []
    
    actual = app.append_to_list(mock_reader(), mock_cached_list())
    expected = [{'date_time': '2021-02-23 17:58:17', 'location': 'Isle of Wight', 'customer_name': 'Ramon Salters', 'products': 'Regular,Americano,1.95,,Flat white,2.15,,Flavoured iced latte - Caramel,2.75', 'payment_method': 'CASH', 'total': '6.85', 'card_details': 'None'}, {'date_time': '2021-02-23 17:59:04', 'location': 'Isle of Wight', 'customer_name': 'Stanley Cordano', 'products': ',Frappes - Coffee,2.75,,Speciality Tea - Darjeeling,1.3,,Smoothies - Berry Beautiful,2.0,Large,Latte,2.45', 'payment_method': 'CASH', 'total': '8.50', 'card_details': 'None'}]

    assert actual == expected

test_append_to_list()

def test_remove_names():
    def mock_data():
        return {'date_time': '2021-02-23 17:58:17', 'location': 'Isle of Wight', 'customer_name': 'Ramon Salters', 'products': 'Regular,Americano,1.95,,Flat white,2.15,,Flavoured iced latte - Caramel,2.75', 'payment_method': 'CASH', 'total': '6.85', 'card_details': 'None'}, {'date_time': '2021-02-23 17:59:04', 'location': 'Isle of Wight', 'customer_name': 'Stanley Cordano', 'products': ',Frappes - Coffee,2.75,,Speciality Tea - Darjeeling,1.3,,Smoothies - Berry Beautiful,2.0,Large,Latte,2.45', 'payment_method': 'CASH', 'total': '8.50', 'card_details': 'None'}

    mock_transform = transform.Transform(mock_data())
    
    mock_transform.remove_names()
    
    actual = mock_transform.data
    expected = {'date_time': '2021-02-23 17:58:17', 'location': 'Isle of Wight', 'products': 'Regular,Americano,1.95,,Flat white,2.15,,Flavoured iced latte - Caramel,2.75', 'payment_method': 'CASH', 'total': '6.85', 'card_details': 'None'}, {'date_time': '2021-02-23 17:59:04', 'location': 'Isle of Wight', 'products': ',Frappes - Coffee,2.75,,Speciality Tea - Darjeeling,1.3,,Smoothies - Berry Beautiful,2.0,Large,Latte,2.45', 'payment_method': 'CASH', 'total': '8.50', 'card_details': 'None'}
    
    assert actual == expected

test_remove_names()

def test_remove_payment_details():
    def mock_data():
        return {'date_time': '2021-02-23 17:58:17', 'location': 'Isle of Wight', 'customer_name': 'Ramon Salters', 'products': 'Regular,Americano,1.95,,Flat white,2.15,,Flavoured iced latte - Caramel,2.75', 'payment_method': 'CASH', 'total': '6.85', 'card_details': 'None'}, {'date_time': '2021-02-23 17:59:04', 'location': 'Isle of Wight', 'customer_name': 'Stanley Cordano', 'products': ',Frappes - Coffee,2.75,,Speciality Tea - Darjeeling,1.3,,Smoothies - Berry Beautiful,2.0,Large,Latte,2.45', 'payment_method': 'CASH', 'total': '8.50', 'card_details': 'None'}

    mock_transform = transform.Transform(mock_data())
    
    mock_transform.remove_payment_details()
    
    actual = mock_transform.data
    expected = {'date_time': '2021-02-23 17:58:17', 'location': 'Isle of Wight', 'customer_name': 'Ramon Salters', 'products': 'Regular,Americano,1.95,,Flat white,2.15,,Flavoured iced latte - Caramel,2.75', 'total': '6.85'}, {'date_time': '2021-02-23 17:59:04', 'location': 'Isle of Wight', 'customer_name': 'Stanley Cordano', 'products': ',Frappes - Coffee,2.75,,Speciality Tea - Darjeeling,1.3,,Smoothies - Berry Beautiful,2.0,Large,Latte,2.45', 'total': '8.50'}
    
    assert actual == expected

test_remove_payment_details()

def test_split_products():
    def mock_data():
        return [{'date_time': '2021-02-23 17:58:17', 'products': 'Regular,Americano,1.95,,Flat white,2.15,,Flavoured iced latte - Caramel,2.75', 'total': '6.85', 'card_details': 'None', 'id': 0}, {'date_time': '2021-02-23 17:59:04', 'products': ',Frappes - Coffee,2.75,,Speciality Tea - Darjeeling,1.3,,Smoothies - Berry Beautiful,2.0,Large,Latte,2.45', 'total': '8.50', 'id': 1}]

    mock_transform = transform.Transform(mock_data())
    
    mock_transform.split_products()
    
    actual = mock_transform.data
    expected = [{'date_time': '2021-02-23 17:58:17', 'products': 'Regular,Americano,1.95,', 'total': '6.85', 'id': 0 },
                {'date_time': '2021-02-23 17:58:17', 'products': 'Flat white,2.15', 'total': '6.85', 'id': 0},
                {'date_time': '2021-02-23 17:58:17', 'products': ',Flavoured iced latte - Caramel,2.75', 'total': '6.85', 'id': 0}, 
                {'date_time': '2021-02-23 17:59:04', 'products': ',Frappes - Coffee,2.75', 'total': '8.50', 'id': 1},
                {'date_time': '2021-02-23 17:59:04', 'products': ',Speciality Tea - Darjeeling,1.3', 'total': '8.50', 'id': 1}, 
                {'date_time': '2021-02-23 17:59:04', 'products': ',Smoothies - Berry Beautiful,2.0', 'total': '8.50', 'id': 1}, 
                {'date_time': '2021-02-23 17:59:04', 'products': ',Large,Latte,2.45', 'total': '8.50', 'id': 1}, 
                ]
    
    print(actual)
    print(expected)
    
    #assert actual == expected

test_split_products()
