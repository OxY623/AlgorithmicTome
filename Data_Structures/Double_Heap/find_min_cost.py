from heapq import heappush, heapop, heapify 

def find_min_cost(ropes):
    heapify(ropes)
    cost = 0
    while len(ropes) > 1:
        sum = heapop(ropes) + heapop(ropes)
        heappush(ropes, sum)
        cost += sum
    return cost
        