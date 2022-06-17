# write a program to check if the given number is a palindrome number.
# A palindrome number is a number that is the same after reverse. For example 545, is a palindrome number.

num=int(input("Enter a number: "))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")

