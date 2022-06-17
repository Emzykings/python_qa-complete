# Print multiplication table form 1 to 10.

print("\t\t\tMultiplication Tables\n")
for i in range (1,11):
    for j in range(1,11):
        print(i * j, end = "\t")
    print("\n")