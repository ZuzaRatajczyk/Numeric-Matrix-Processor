u_input = input()
list_of_digits = [int(digit) for digit in u_input]
list_of_sums = [sum(list_of_digits[:i+1]) for i in range(len(list_of_digits))]
print(list_of_sums)
