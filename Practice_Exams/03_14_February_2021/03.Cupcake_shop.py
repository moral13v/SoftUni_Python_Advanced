def stock_availability(*args):
    from collections import deque

    inventory = deque(args[0])
    command = args[1]

    if command == "delivery":
        for item in args[2:]:
            inventory.append(item)
    elif command == "sell":
        if len(args) == 2:
            inventory.popleft()
        elif type(args[2]) == int:
            for _ in range(args[2]):
                inventory.popleft()
        else:
            for item in args[2:]:
                while item in inventory:
                    inventory.remove(item)

    return list(inventory)


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))


