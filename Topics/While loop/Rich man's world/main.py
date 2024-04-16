DEPOSIT_LIMIT = 700000
INTEREST_RATE = 0.071

deposit = float(input())
years = 0
while deposit < DEPOSIT_LIMIT:
    interest = deposit * INTEREST_RATE
    deposit += interest
    years += 1

print(years)
