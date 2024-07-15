# Global products Dictionary: Stores product details with product ID as the key
products = {} 

def add_product(product_id, name, price, quantity):
                                                        
    if product_id in products:  
        raise ValueError(f"Product with ID {product_id} already exists.")
    products[product_id] = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

def get_product(product_id):
    if product_id not in products:
        raise KeyError(f"Product with ID {product_id} not found.")
    return products[product_id]

def list_products():
    if not products:
        raise ValueError("No products available.")
    return products

