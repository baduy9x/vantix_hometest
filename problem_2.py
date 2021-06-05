def find_best_investment(arr):
    if len(arr) < 2:
        return None, None

    current_min = arr[0]
    current_max_profit = -float("inf")
    result = (None, None)

    for item in arr[1:]:
        current_profit = item - current_min
        if current_profit > current_max_profit:
            current_max_profit = current_profit
            result = (current_min, item)
        if item < current_min:
            current_min = item
    return result

if __name__ == '__main__':
    print(find_best_investment([1, 2, -1, 4, 5, 6, 7]))