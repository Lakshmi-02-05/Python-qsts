# Find the product with the highest price

products = [
    {"name": "Laptop", "price": 60000},
    {"name": "Phone", "price": 25000},
    {"name": "Tablet", "price": 35000},
    {"name": "Monitor", "price": 18000}
]

highest_price_product = max(products, key=lambda x: x["price"])
print(f" {highest_price_product['name']}: {highest_price_product['price']}.")