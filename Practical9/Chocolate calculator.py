def chocolate_calculator(total_money,price):
    n = total_money // price
    change = total_money - n*price
    return n,change
total_money = 100
price = 7
n, change = chocolate_calculator(total_money,price)
print(f'You can buy {n} chocolate and the change is {change}')