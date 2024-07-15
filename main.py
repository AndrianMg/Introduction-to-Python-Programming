from product_monitor import add_product, get_product, list_products

def main():
    while True:
        print("\nProduct Monitoring System")
        print("1. Add Product")
        print("2. Get Product")
        print("3. List All Products")
        print("4. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                product_id = int(input("Enter Product ID: "))
                name = input("Enter Product Name: ")
                price = float(input("Enter Product Price: "))
                quantity = int(input("Enter Product Quantity: "))
                add_product(product_id, name, price, quantity)
                print("Product added successfully.")
            elif choice == '2':
                product_id = int(input("Enter Product ID: "))
                product = get_product(product_id)
                print(f"ID: {product_id}, Name: {product['name']}, Price: {product['price']}, Quantity: {product['quantity']}")
            elif choice == '3':
                products = list_products()
                for product_id, product in products.items():
                    print(f"ID: {product_id}, Name: {product['name']}, Price: {product['price']}, Quantity: {product['quantity']}")
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError as ve:
            print(f"ValueError: {ve}")
        except KeyError as ke:
            print(f"KeyError: {ke}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
