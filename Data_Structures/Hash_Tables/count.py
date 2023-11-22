def count(a_string):
    a_dict = {}
    for char in a_string:
        if char in a_dict:
            a_dict[char]+=1
        elif char == " ":
            continue
            
        else:
            a_dict[char] = 1
    print(a_dict)


a_str="I am workind there"
count(a_str)