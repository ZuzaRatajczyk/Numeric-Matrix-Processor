def object_with_beautiful_identity():  # function that returns an object whose identity ends with 888
    for i in range(10_000):
        if id(i) % 1000 == 888:
            return i
    return None

