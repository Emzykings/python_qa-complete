# Create a new list from a two list using the following condition.
# Given a two list of numbers, write a program to create a new list such that the new list should contain,
# odd numbers from the first list and even numbers from the second list.

list_1 = [10, 20, 25, 30, 35]
list_2 = [40, 45, 60, 75, 90]
list_3 = [num for num in list_1 if num%2]+[num for num in list_2 if not num%2]
print(list_3)