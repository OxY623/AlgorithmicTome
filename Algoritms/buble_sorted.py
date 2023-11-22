def main():
    list_n = [2,5,12,101,32,1,9,6,0]
    print(inserts(list_n))

def inserts(a_list):
    for i in range(1, len(a_list)):
        value = a_list[i]
        while i > 0 and a_list[i-1] > value:
            a_list[i] = a_list[i-1]
            i = i -1
        a_list[i] = value
    return a_list

def buble(prompt):
    i = len(prompt)
    while i > 0:
        no_swaps = True
        for x in range(0, i-1):
            if prompt[x] > prompt[x+1]:
                prompt[x], prompt[x+1] = prompt[x+1], prompt[x]
                no_swaps = False
        if no_swaps:
            return prompt    
        i-=1
    return prompt

if __name__ == "__main__":
    main()