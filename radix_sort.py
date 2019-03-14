from random import randrange, randint


# generating up to 20 random numbers(0-1000) so there's something to sort
data = [randint(0, 1000) for item in range(randrange(20))]
print(f'Generated {len(data)} random numbers: {data}')


def radix_sort(data):
    for exponent in range(len(str(max(data)))):
        index = -(exponent + 1)
        digits = [[] for digit in range(10)]

        for number in data:  # Takes numbers in an input list.
            try:
                digit = str(number)[index]  # Passes through each digit in those numbers, from least to most significant
                digit = int(digit)  # Looks at the values of those digits.
            except IndexError:
                digit = 0

            digits[digit].append(number)  # Buckets the input list according to those digits.

        data = []
        for numeral in digits:  # Renders the results from that bucketing.
            data.extend(numeral)
    # ^Repeats this process until the list is sorted (until the first for loop stops iterating).
    return data

print(f' sorted: {radix_sort(data)}')
