from collections import deque

pizza_orders = deque(int(x) for x in input().split(", "))
employees_stack = [int(x) for x in input().split(", ")]

total_pizzas = 0

while pizza_orders:
    if not employees_stack:
        break

    current_order = pizza_orders[0]
    current_employee = employees_stack[-1]

    if current_order > 10 or current_order <= 0:
        pizza_orders.popleft()
        continue

    if current_order <= current_employee:
        total_pizzas += current_order
        pizza_orders.popleft()
        employees_stack.pop()
    else:
        current_order -= current_employee
        pizza_orders[0] = current_order
        total_pizzas += current_employee
        employees_stack.pop()

if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
    print(f"Employees: {', '.join([str(x) for x in employees_stack])}")

if not employees_stack:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(x) for x in pizza_orders])}")

