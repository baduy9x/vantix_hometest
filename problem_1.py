def find_mode(arr):
    if len(arr) == 1:
        return arr

    last_item = None
    count = 1
    max_appear = 0
    result = []

    for item in arr:
        if item == last_item:
            count += 1
        else:
            if count > max_appear:
                result = [last_item]
                max_appear = count
            elif count == max_appear:
                result.append(last_item)
            count = 1
            last_item = item

    if count > max_appear:
        result = [last_item]
    elif count == max_appear:
        result.append(last_item)

    return result


if __name__ == "__main__":
    arr = [1,2,3,3,3,3,4,4,5,5,6,6,6,6]
    print(find_mode(arr))
