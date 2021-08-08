import math
import sys

favourite_number = int(input("Enter your favourite number? "))

if favourite_number <= 1:
    print('It cannot be determined...... as 0 is not a natural number and rest are negative numbers.....')
    sys.exit(0)

count = 0

for i in range(int(math.sqrt(favourite_number))+1):
    if i == 1 or i == 0:
        continue
    if favourite_number % i == 0:
        count = count + 1
    if count == 1:
        break

if count == 1:
    print(favourite_number, 'is not a prime number')

else:
    print(favourite_number, 'is a prime number')
