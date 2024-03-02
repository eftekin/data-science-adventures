import pandas as pd

visits = pd.read_csv("./csv/visits.csv", parse_dates=[1])
cart = pd.read_csv("./csv/cart.csv", parse_dates=[1])
checkout = pd.read_csv("./csv/checkout.csv", parse_dates=[1])
purchase = pd.read_csv("./csv/purchase.csv", parse_dates=[1])

print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())

visits_cart = pd.merge(visits, cart, how="left")

total_visit = len(visits_cart)
print(total_visit)


null_cart_times = len(visits_cart[visits_cart.cart_time.isnull()])
print(null_cart_times)


visited_not_cart = float(null_cart_times) / float(total_visit)
print(visited_not_cart)


cart_checkout = cart.merge(checkout, how="left")
print(cart_checkout.head())

null_checkout_times = len(cart_checkout[cart_checkout.checkout_time.isnull()])
cart_not_checkout = float(null_checkout_times) / float(len(cart))

print("Cart but not checkout:", cart_not_checkout)


all_data = visits_cart.merge(cart_checkout, how="left").merge(purchase, how="left")
print(all_data.head())

reached_checkout = all_data[~all_data.checkout_time.isnull()]
checkout_not_purchase = all_data[
    (all_data.purchase_time.isnull()) & (~all_data.checkout_time.isnull())
]
checkout_not_purchase_percent = float(len(checkout_not_purchase)) / float(
    len(reached_checkout)
)
print(
    "% of users who got to checkout but did not purchase:",
    checkout_not_purchase_percent,
)

print(
    "{} percent of users who visited the page did not add a t-shirt to their cart".format(
        round(visited_not_cart * 100, 2)
    )
)
print(
    "{} percent of users who added a t-shirt to their cart did not checkout".format(
        round(cart_not_checkout * 100, 2)
    )
)
print(
    "{} percent of users who made it to checkout  did not purchase a shirt".format(
        round(checkout_not_purchase_percent * 100, 2)
    )
)

all_data["time_to_purchase"] = all_data.purchase_time - all_data.visit_time
print(all_data.time_to_purchase)

print(all_data.time_to_purchase.mean())
