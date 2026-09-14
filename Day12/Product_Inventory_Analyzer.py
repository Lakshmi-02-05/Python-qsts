# Product Inventory Analyzer
# 1. Total inventory value for each product (price × stock)
# 2. The product with the highest inventory value
# 3. The total value of all inventory
# 4. The product with the lowest stock
# 5. Products whose stock is below 5


products = {
    "laptop": {"price": 60000, "stock": 5},
    "phone": {"price": 25000, "stock": 10},
    "tablet": {"price": 30000, "stock": 3},
    "headphones": {"price": 5000, "stock": 20}
}

values = []
grand_total = 0
highest_value = 0
highest_product = ""
lowest_stock = float("inf")
lowest_stock_product = ""

for product, details in products.items():

    # 1. Inventory value
    total_value = details["price"] * details["stock"]
    values.append(total_value)

    print(f"Total inventory value for {product}: {total_value}")

    # 2. Highest inventory value
    if total_value > highest_value:
        highest_value = total_value
        highest_product = product

    # 3. Total inventory value
    grand_total += total_value

    # 4. Lowest stock
    if details["stock"] < lowest_stock:
        lowest_stock = details["stock"]
        lowest_stock_product = product

    # 5. Stock below 5
    if details["stock"] < 5:
        print(f"Stock below 5: {product}")


print("Highest inventory value:", highest_product, highest_value)
print("Total value of all inventory:", grand_total)
print("Lowest stock:", lowest_stock_product, lowest_stock)




#  My Code
# products = {
#     "laptop": {"price": 60000, "stock": 5},
#     "phone": {"price": 25000, "stock": 10},
#     "tablet": {"price": 30000, "stock": 3},
#     "headphones": {"price": 5000, "stock": 20}
# }
# values =[]

# # 1. Total inventory value for each product (price × stock)
# for product,details in products.items():
#     total_value = details["price"] * details["stock"]
#     grand_total += total_value
#     values.append(total_value)
#     print(f"Total inventory value for {product}: {total_value}")

#     if details["stock"] < 5:
#         print(f"Stock below 5: {product}")

# print(total_value)
# print(grand_total)
# print(max(values))
# print(min(values))