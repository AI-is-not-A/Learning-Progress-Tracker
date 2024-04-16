initial_quantity = int(input())
final_quantity = int(input())

rest_quantity = initial_quantity
number_of_days = 0

while rest_quantity > final_quantity:
    number_of_days += 12
    rest_quantity /= 2

print(number_of_days)
