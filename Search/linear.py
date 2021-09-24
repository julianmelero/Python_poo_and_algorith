import random
def linear_search(list, n):
    match = False

    for elemento in list:
        if elemento == n:
            match = True
            break
    return match        


if __name__ == "__main__":
    list_size = int(input("Size list:"))
    objetive = int(input("Number:"))
    list = [random.randint(0, 100) for i in range(list_size)]
    is_in = linear_search(list, objetive)
    print(list)
    print("Element {} is on the list {}".format(objetive, is_in))