import random

def bubble(list):
    new_arr = []
    for index, element in enumerate(list):
        print(element, index)
        if element > list[index + 1]:
            element = list[index + 1]
            list[index + 1] = element
        
        



if __name__ == "__main__":
    list_size = int(input("Size list:"))    
    list = [random.randint(0, 100) for i in range(list_size)]
    bubble(list)