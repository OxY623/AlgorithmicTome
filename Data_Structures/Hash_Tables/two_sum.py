def two_sum(a_list, target):
    a_dict = {}
    for i, num in enumerate(a_list):
        rem = target - num
        if rem in a_dict:
            return i, a_dict[rem]
        else:
            a_dict[num] = i


a_list = [1,2,3,4,5]
index, b = two_sum(a_list, 6)
print(index)
print(b)