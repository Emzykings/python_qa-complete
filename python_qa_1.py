#Given two integer numbers return their products only if the product is equal to or lower than 1000, else return their sum. 
#(Given 1: num_1 = 20 num_2 = 30 , Given 2: num_1 = 40 num_2 = 40)

num_1 = 20
num_2 = 30
num_product = num_1 * num_2
num_sum = num_1 + num_2
if num_product <= 1000:
    print(num_product)
else:
    print(num_sum)

num_1 = 40
num_2 = 30
num_product = num_1 * num_2
num_sum = num_1 + num_2
if num_product <= 1000:
    print(num_product)
else:
    print(num_sum)

