import random
import sys 
  
  
sys.setrecursionlimit(10**6) 

def mergeshort(list):
    if len(list) > 1:
        half = len(list)//2
        left = list[:half]
        right = list[half:]

        # Recursive call in each half
        mergeshort(left)
        mergeshort(right)

        # First two list Iterators 
        i = 0
        j = 0
        # For main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1

            k += 1


        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1

    return list




if __name__ == "__main__":
    list_size = int(input("Size list:"))    
    list = [random.randint(0, 100) for i in range(list_size)]
    result = mergeshort(list)
    print(result)
    