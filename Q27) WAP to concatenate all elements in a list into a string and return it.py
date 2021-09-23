def concatenate_list(list):
    result = ''
    for element in list:
        result += str(element)
    return result

print(concatenate_list([1,2,3,4,5]))