import sys
sys.path.append("..") # Goes back a level in the directory

import src.app as app

def test_append_data():
    def mock_file():
        return ["2021-02-23 09:00:48","Isle of Wight","Morgan Berka","Large,Hot chocolate,2.9,Large,Chai latte,2.6,Large,Hot chocolate,2.9","CASH","8.40","None"]
    
    expected = ["2021-02-23 09:00:48","Isle of Wight","Morgan Berka","Large,Hot chocolate,2.9,Large,Chai latte,2.6,Large,Hot chocolate,2.9","CASH",8.40]
    actual = app.append_data(mock_file())
    
    assert actual == expected
    
test_append_data()
