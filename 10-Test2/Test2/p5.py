def f(shopping_cart, price_list, customer_wallet):
    endprice = 0
    for item in shopping_cart:
        if item in price_list:
            endprice += shopping_cart[item]*price_list[item]
    return customer_wallet > endprice


if __name__ == "__main__":
    cart = {'juice': 3, 'bread': 1, 'milk': 2}
    prices = {'milk': 1.49, 'butter': 2.09, 'juice': 1.19, 'bread': 1.99}
    print(f(cart, prices, 10))
    print(f(cart, prices, 8))