


def morral(size, weights, values, n):
    if n == 0 or size == 0:
        return 0

    if weights[n - 1] > size:
        return morral(size, weights, values, n - 1)

    return max(values[n - 1] + morral(size - weights[n-1], weights, values, n- 1), morral(size, weights, values, n - 1))





if __name__ == "__main__":
    values = [60,100, 120]
    weights = [10,20,30]
    size = 50
    n = len(values)
    result = morral(size, weights, values, n)
    print(result)

