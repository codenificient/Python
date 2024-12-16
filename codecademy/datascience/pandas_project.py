import codecademylib3
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])


print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())

visits_cart = visits.merge(cart, how="left")
print(visits_cart.head())

total_len = len(visits_cart)
print(total_len)

null_cart_times = len(visits_cart[visits_cart.cart_time.isnull()])
print(null_cart_times)

only_visited = null_cart_times / total_len * 100
print(only_visited)

cart_checkout_df = cart.merge(checkout, how="left")
print(cart_checkout_df.head())

has_cart_item = cart_checkout_df[~cart_checkout_df.cart_time.isnull()]
print(len(has_cart_item))

print(has_cart_item.head())

did_not_checkout = has_cart_item[has_cart_item.checkout_time.isnull()]
print(did_not_checkout.head())

percentage_wanted =  len(did_not_checkout) /  len(has_cart_item) * 100
print(percentage_wanted )

all_data = visits_cart.merge(checkout, how="left").merge(purchase, how="left")
print(all_data.head())


checkout_customers = all_data[~all_data.checkout_time.isnull()]
print(len(checkout_customers))


checkout_no_purchase = checkout_customers[checkout_customers.purchase_time.isnull()]
print(len(checkout_no_purchase))


percentage = len(checkout_no_purchase) / len(checkout_customers) * 100
print(percentage)

print("Only visited " + str(only_visited) + "% ===> " + " Cart no checkout " + str(round(percentage_wanted,2)) + "% ===>" + " Checkout but no purchase " + str(round(percentage,2)) + "%" )

all_data["time_to_purchase"] = all_data["purchase_time"] - all_data["visit_time"]
print(all_data.time_to_purchase)
print(all_data.time_to_purchase.mean())

