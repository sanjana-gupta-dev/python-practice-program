num = int(input("Enter your number:"))

temp = num
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit ** 3
    num = num // 10

if temp == sum:
    print("Armstrong number")
else:
    print("Not Armstrong number")

