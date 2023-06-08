# Возведение a в степень b
def exponentiation(a, b):
    if b == 0:
        return 1
    return a * exponentiation(a, b - 1)

# Сума a и b (только +1 -1)
def rec_sum(a, b):
    if b == 0:
        return a
    return 1 + rec_sum(a, b - 1)
