from random import randrange, randint


# generating up to 20 random numbers(0-100) so there's something to sort
data = [randint(0, 100) for item in range(randrange(20))]
print(f'Generated {len(data)} random numbers: {data}')


def quicksort(data):
    if len(data) <= 1:  # checking if list to be sorted is at least 2 elements long
        return data
    else:
        quicksorter(data, 0, len(data) - 1)


def quicksorter(list, start, end):
    if start >= end:
        return

    pivot_index = randrange(start, end + 1)  # assigning value of random index to pivot variable
    pivot_element = list[pivot_index]

    list[end], list[pivot_index] = list[pivot_index], list[end]  # switching values
    less_than_pointer = start

    for el in range(start, end):  # checking values in list and swapping them if no t in order
        if list[el] < pivot_element:
            list[el], list[less_than_pointer] = list[less_than_pointer], list[el]
            less_than_pointer += 1

    list[end], list[less_than_pointer] = list[less_than_pointer], list[end]  # assigning new parameters for recursion

    quicksorter(list, start, less_than_pointer - 1)  # recurring
    quicksorter(list, less_than_pointer + 1, end)


quicksort(data)
print(f"Result: {data}")
