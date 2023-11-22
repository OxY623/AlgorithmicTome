def main():
    an_array = [1,2,3,4,5,6,7,8,9]
    result = first_even_then_2(an_array)
    print(result)
# The first method
def first_even_then(an_array):
    list_a = [i for i in an_array if i%2==0]
    list_b = [i for i in an_array if i not in list_a]
    return (list_a + list_b)

#The second method
def first_even_then_2(an_array):
    index_x=0
    
    for index, n in enumerate(an_array):
        value = an_array[index] 
        if is_even(n):
            an_array[index_x], an_array[index]=n,an_array[index_x]
            index_x+=1
    return an_array
        

def is_even(n):
    return not n & 1

if __name__ == "__main__":
    main()