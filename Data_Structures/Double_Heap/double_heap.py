from heapq import heapify, heappop

a_list = ["R", "C", "T", "H", "E", "D", "L"]
heapify(a_list)
print(a_list)
heappop(a_list)
print("After poping")
print(a_list)