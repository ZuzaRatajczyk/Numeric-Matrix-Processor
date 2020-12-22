import math

value = int(input())
log_base = int(input())

if log_base <= 1:
    log_of_value = math.log(value)
    print(round(log_of_value, 2))
else:
    log_of_value = math.log(value, log_base)
    print(round(log_of_value, 2))
