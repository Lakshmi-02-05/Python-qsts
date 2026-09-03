#Common Elements

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
def common_el(list1,list2):
    result = list(set(list1).intersection(list2))
    print(result)
common_el(list1, list2)