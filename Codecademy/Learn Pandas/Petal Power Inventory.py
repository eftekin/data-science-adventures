import pandas as pd

inventory = pd.read_csv("inventory.csv")
# print(inventory.head(10))

staten_island = inventory.iloc[0:10]
# print(staten_island)

product_request = staten_island["product_description"]
# print(product_request)

seed_request = inventory[
    (inventory["location"] == "Brooklyn") & (inventory["product_type"] == "seeds")
]
# print(seed_request)

check_stock = lambda x: True if x["quantity"] > 0 else False
inventory["in_stock"] = inventory.apply(check_stock, axis=1)
# print(inventory)

check_value = lambda x: x["price"] * x["quantity"]
inventory["total_value"] = inventory.apply(check_value, axis=1)
# print(inventory)

combine_lambda = lambda row: "{} - {}".format(row.product_type, row.product_description)
inventory["full_description"] = inventory.apply(combine_lambda, axis=1)
print(inventory)
