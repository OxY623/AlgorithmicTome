def main():
    str_a = "I am a self-taught programmer looking for a job as a programmer"
    result = delete_repeated_words(str_a)
    print(result)

def delete_repeated_words(a_string):
    a_dict = {}
    list_a = a_string.split()
    for word in list_a:
        if word in a_dict:
            a_dict[word] += 1
        else:
            a_dict[word] = 1
    result_str = " ".join([key for key, val in a_dict.items() if val == 1])
    return result_str

if __name__ == "__main__":
    main()