from bisect import bisect_left

def main():
    sorted_fruits = ['apple', 'banana', 'orange', 'plum']
    binary_search(sorted_fruits, 'apple')

def binary_search(_list, _x):
    start = 0
    end = len(_list) - 1

    while start <= end:
        middle = (start + end) // 2

        # Calculate the sum of ASCII values for the middle word
        middle_sum_ord = sum(ord(char) for char in _list[middle])

        if middle_sum_ord == sum(ord(char) for char in _x):
            print(f"Found {_x} at index {middle}")
            return True
        elif middle_sum_ord < sum(ord(char) for char in _x):
            start = middle + 1
        else:
            end = middle - 1

    print(f"{_x} not found in the list.")
    return False

if __name__ == "__main__":
    main()