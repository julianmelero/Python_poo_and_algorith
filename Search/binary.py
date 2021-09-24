import random



def binary(list,start, end, n):          

    if start > end:
        return False
    
    middle = (start + end)//2

    if list[middle] == n:
        return True
    elif list[middle] < n:
        return binary(list, middle + 1, end, n)
    else:
        return binary(list, 0, middle - 1, n)


if __name__ == "__main__":
    list_size = int(input("Size list:"))
    objetive = int(input("Number:"))
    list = sorted([random.randint(0, 100) for i in range(list_size)])
    is_in = binary(list, 0, len(list),objetive)
    print(list)
    print("Element {} is on the list {}".format(objetive, is_in))    