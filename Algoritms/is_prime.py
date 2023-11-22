def main():
    print(find_prime(12000))

def is_prime(x):
    if x < 1 or (x > 2 and x%2 == 0):
        return False
    i = 2
    while i < int(x**0.5):
        if x % i == 0:
            return False
        i+=1
    return True

def find_prime(x):
    return [ i for i in range(0,x) if is_prime(i)]

if __name__ == "__main__":
    main()