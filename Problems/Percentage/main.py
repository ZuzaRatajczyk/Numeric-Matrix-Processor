def get_percentage(num, round_digits=None):
    if round_digits:
        return f"{round(num * 100, round_digits)}%"
    else:
        return f"{round(num * 100)}%"
