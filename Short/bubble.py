import random

def bubble(list):    
    """while(True):
        changes = 0
        for index, element in enumerate(list):        
            if index + 1 == len(list):
                break
            if  element > list[index + 1]:
                changes +=1
                a = list[index + 1]                                
                list[index + 1] = element
                list[index] = a
            else:                
                list[index] = element
        if changes ==0:
            break 
    
    """
    n = len(list)

    for i in range(n):
        for j in range(0, n - i - 1): # O(n) * O(n) = O(n * n) = O(n**2)

            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

    
    print(list)
        



if __name__ == "__main__":
    list_size = int(input("Size list:"))    
    list = [random.randint(0, 100) for i in range(list_size)]
    bubble(list)