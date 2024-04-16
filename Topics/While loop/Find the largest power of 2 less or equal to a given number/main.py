# Importing the necessary math library
import math

# Function to find the largest power of 2 less than or equal to 'n'
def largestPower(n):
    # Start coding here
    i = 0
    while 2 ** i < n:
        i += 1        
    return 2 ** (i - 1)
        
# Take the input n
n = int(input())

print(largestPower(n))
