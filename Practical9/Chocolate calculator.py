def chocolate_calculator(total_money,price):
    n = total_money // price
    change = total_money - n*price
    return n,change
total_money = 100
price = 7
print(chocolate_calculator(total_money,price))