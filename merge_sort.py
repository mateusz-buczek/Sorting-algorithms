import random


# generating up to 20 random numbers(0-100) so there's something to sort
data = [random.randint(0, 100) for item in range(random.randrange(20))]
print(f'Generated {len(data)} random numbers: {data}')

# divide list into smaller pieces (recursively)
# sort pieces individually
# merge smaller pieces into one list comparing which is greater/smaller


def merge_sort(items, order):  # additional parameter to enhance functionality - choose sorting order with '+' or '-'
    if len(items) <= 1:
        return items
    else:  # splitting list in halves until they're 2 elements long
        split_index = len(items) // 2
        l_split = items[:split_index]
        r_split = items[split_index:]

        l_sorted = merge_sort(l_split, order)
        r_sorted = merge_sort(r_split, order)

    return merge(l_sorted, r_sorted, order)  # calling merging function


def merge(left, right, order):
    result = []  # creating new list for result
    while left and right:
        if order == '+':  # executing chosen sorting order
            if left[0] <= right[0]:
                result.append(left[0])
                left.pop(0)
            else:
                result.append(right[0])
                right.pop(0)
        elif order == '-':  # executing chosen sorting order
            if left[0] >= right[0]:
                result.append(left[0])
                left.pop(0)
            else:
                result.append(right[0])
                right.pop(0)

    if left:  # adding leftovers
        result += left
    if right:
        result += right

    return result

print(f"Ascending Sort: {merge_sort(data, '+')}")
print(f"Descending Sort: {merge_sort(data,'-')}")