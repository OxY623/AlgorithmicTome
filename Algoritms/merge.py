def main():
    list_a = [23,33,5,22,1,63,72,9,1]
    merge(list_a)

def merge(list_a):
    if len(list_a)>1:
        mid = len(list_a)//2
        left_half = list_a[:mid]
        right_half = list_a[mid:]
        merge(left_half)
        merge(right_half)

        left_ind = 0
        right_ind = 0
        alist_ind = 0

        while left_ind < len( left_half) and right_ind < len(right_half):
            if left_half[left_ind] <= right_half[right_ind]:
                list_a[alist_ind] = left_half[left_ind]
                left_ind += 1
            else:
                list_a[alist_ind] = right_half[right_ind]
                right_ind +=1
            alist_ind +=1
        while left_ind < len(left_half):
            list_a[alist_ind] = left_half[left_ind]
            left_ind +=1
            alist_ind +=1
        while right_ind < len(right_half):
            list_a[alist_ind]=right_half[right_ind]
            right_ind+=1
            alist_ind+=1