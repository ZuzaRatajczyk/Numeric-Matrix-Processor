def final_deposit_amount(*interest, amount=1000):
    for rate in interest:
        rate = rate / 100
        profit = amount * rate
        amount += profit
    return round(amount, 2)
