#write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.

previous_num = 0
for x in range(1,11):
    sum = previous_num + x
    print(f'The sum of Current number {x} Previous Number {previous_num} is {sum}')
    previous_num = x