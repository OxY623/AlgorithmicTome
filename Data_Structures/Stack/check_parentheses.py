def main():
    str_a = "({a}:(b:({c}:({d}:(1)))))"
    print(check_parentheses(str_a))

def check_parentheses(a_string):
    stack = []
    for x in a_string:
        if x == "(" or x == "{":
            stack.append(x)
        elif x ==")" or x == "}":
            if len(stack)==0:
                return False
            else:
                stack.pop()
    return len(stack) == 0


if __name__=="__main__":
    main()