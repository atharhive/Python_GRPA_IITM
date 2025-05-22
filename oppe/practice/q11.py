### Q11: Create a dictionary where categories are keys and the total price of all items in that category is the value.

grocery_data = [
    {"item": "Apple", "category": "Fruit", "price": 2.5, "quantity": 10, "expiry_days": 7},
    {"item": "Milk", "category": "Dairy", "price": 3.0, "quantity": 5, "expiry_days": 5},
    {"item": "Bread", "category": "Bakery", "price": 2.0, "quantity": 8, "expiry_days": 4},
    {"item": "Carrot", "category": "Vegetable", "price": 1.2, "quantity": 15, "expiry_days": 10},
    {"item": "Chicken", "category": "Meat", "price": 7.5, "quantity": 3, "expiry_days": 3},
    {"item": "Rice", "category": "Grains", "price": 5.0, "quantity": 20, "expiry_days": 180},
    {"item": "Eggs", "category": "Dairy", "price": 4.0, "quantity": 12, "expiry_days": 14},
    {"item": "Orange", "category": "Fruit", "price": 3.2, "quantity": 10, "expiry_days": 10},
    {"item": "Butter", "category": "Dairy", "price": 6.0, "quantity": 4, "expiry_days": 30},
    {"item": "Potato", "category": "Vegetable", "price": 0.9, "quantity": 25, "expiry_days": 20},
    {"item": "Fish", "category": "Meat", "price": 8.0, "quantity": 2, "expiry_days": 2},
    {"item": "Pasta", "category": "Grains", "price": 4.5, "quantity": 10, "expiry_days": 365}
]

x = {}
for item in grocery_data:
    cat = item["category"]
    price = item["price"]
    quantity = item["quantity"]
    total = price * quantity

    if cat in x:
        x[cat] += total
    else:
        x[cat] = total

print(x)




# print(grocery_data[1]["price"] * grocery_data[1]["quantity"])

# print(grocery_data[2])
# print(grocery_data[0]["item"])
# print(grocery_data[item])
