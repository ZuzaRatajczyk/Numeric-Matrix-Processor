def range_sum(numbers, start, end):
    sum_of_range = 0
    for number in numbers:
        if int(start) <= int(number) <= int(end):
            sum_of_range += int(number)
    return sum_of_range


input_numbers = input().split()
a, b = input().split()
print(range_sum(input_numbers, a, b))