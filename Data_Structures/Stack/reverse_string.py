def reverse_string(a_string):
    stack = []
    string = ""
    for x in a_string:
        stack.append(x)
    for i in a_string:
        string +=stack.pop()

    return string

def main():
    s = "super"
    print(reverse_string(s))

if __name__ == "__main__":
    main()
