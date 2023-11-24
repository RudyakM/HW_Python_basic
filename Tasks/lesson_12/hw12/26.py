def round_cost(x):
    total_cost = []
    for i in cost_order:
        i = round(i, 2)
        total_cost.append(i)
    order_cost = zip(order, total_cost)
    print(list(order_cost))
    return order_cost
    

contacts = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
    ]

order = []
amount = []
price = []

for i in contacts:
    order.append(i[0])
    amount.append(i[2])
    price.append(i[3])

cost_order = list(map(lambda x, y: x * y if x * y > 100 else x * y + 10, price, amount))
round_cost(x=cost_order)
