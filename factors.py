# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

print("Please enter a positive integer:")
num1=int(input())
print("The factors of", num1, "are:")
for i in range(1,num1+1):
    if num1%i==0 and (num1/i)%2==0:
        print(i)
    elif i==num1:
        print(num1)
