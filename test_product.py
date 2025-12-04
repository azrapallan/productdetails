test_product.py
from product import product_details

def test_product_details_output():
    result=product_details("p101","laptop",5,55000)
    expected=(
    "product_id : p101\n"
    "product_name :"Laptop\n"
    "quantity : 5\n"
   " price : 55000"
   )
   assert result == expected

