import random


# generating up to 20 random numbers(0-100) so there's something to sort 
data = [random.randint(0, 100) for item in range(random.randrange(20))]
print(f'Generated {len(data)} random numbers: {data}')

def asc_sort(data):
    checker = 0
    if len(data) >= 2:
        while checker != (len(data) - 1): # sorting makes sense only if there is at least 2 elements
            for el in range(len(data)-1): # checking needed only up to second last element -it checks with last element
                index_1 = el # start comparing from index 0 (assign variable) and compare with index +1
                index_2 = el+1
                if data[index_1] > data[index_2]: # actual comparing and switching values
                    temp = data[index_1]
                    data[index_1] = data[index_2]
                    data[index_2] = temp
                    checker = 0
                else:
                    checker += 1 # checks if there is need for further comparing, if not returns sorted list
                    if checker == (len(data)-1):
                        return data
    else:
        return data


def desc_sort(data):
    checker = 0
    if len(data) >= 2:
        while checker != (len(data) - 1): # sorting makes sense only if there is at least 2 elements
            for el in range(len(data)-1): # checking needed only up to second last element -it checks with last element
                index_1 = el # start comparing from index 0 (assign variable) and compare with index +1
                index_2 = el+1
                if data[index_1] < data[index_2]: # actual comparing and switching values
                    temp = data[index_1]
                    data[index_1] = data[index_2]
                    data[index_2] = temp
                    checker = 0
                else:
                    checker += 1 # checks if there is need for further comparing, if not returns sorted list
                    if checker == (len(data)-1):
                        return data
    else:
        return data


print(f'Ascending Sort: {asc_sort(data)}')
print(f'Descending Sort: {desc_sort(data)}')