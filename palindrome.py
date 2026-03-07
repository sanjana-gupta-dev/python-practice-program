num = int(input("Enter your number :"))

temp = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev* 10 + digit
    num = num // 10

if temp == rev:
    print("Palindrome number")
else:
    print("not palindrome")