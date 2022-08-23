def shopping_list(budget, **kwargs):
    basket = []
    basket_limit = 5
    if budget < 100:
        return "You do not have enough budget."

    for key, value in kwargs.items():
        if len(basket) >= basket_limit:
            break
        item = key
        price = float(value[0])
        quantity = int(value[1])
        amount = price * quantity
        if amount <= budget:
            basket.append(f"You bought {item} for {amount:.2f} leva.")
            budget -= amount
    return '\n'.join(basket)


print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))


