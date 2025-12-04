# product.py

def product_details(product_id, name, quantity, price):
   
    return (
        f"productID: {product_id}\n"
        f"productName: {name}\n"
        f"Quantity: {quantity}\n"
        f"Price: ${price}"
    )


if __name__ == "__main__":
   pid="P101"
   pname="laptop"
   qty=5
   pr=55000
    print(product_details(pid,pname,qty,pr))
