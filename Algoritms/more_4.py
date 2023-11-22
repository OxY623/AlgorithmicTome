def main():
    list_a = ["selftaught",
"code", "sit", "eat", "programming", "dinner", "one", "two", "coding",
"a", "tech"]
    
    list_b = [x for x in list_a if len(x)>4]
    print(list_b)

if __name__ == "__main__":
    main()