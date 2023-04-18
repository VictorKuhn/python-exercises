def remove_duplicatas(list):
    new_list = []
    for indice in list:
        if indice not in new_list:
            new_list.append(indice)
    return new_list

print(remove_duplicatas([1,2,5,2,1,5,1,2,5,1,7,7,5,23,23,19,19,99,91,92,92]))