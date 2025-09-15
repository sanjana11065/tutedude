#task 1
num=int(input("enter the first number:"))
if num%2==0:
    print(num,'is an even number')
else:
    print(num,"is an odd number")



#task 2
total = 0
for i in range(1, 51):
    total += i

print(f"The sum of numbers from 1 to 50 is: {total}")

