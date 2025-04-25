number = int(input("Enter a number: "))
digit_sum = 0

while number > 0:
    digit = number % 10
    digit_sum += digit
    number = number // 10

print("Sum of digits:", digit_sum)
#6:mathematically,we can get the separate digits using 10 and the concept of int; the remainder of 10 removes the last digit and the division of ten removes the last digit.This process takes out a digit procedurally until the number is depleted