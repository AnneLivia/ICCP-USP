def merge_sort(lista):
    # base case for merge sort
    if len(lista) <= 1: # it's already sorted, it has reached its base case
        return lista # return the list so that we can make the merge with other one
    # otherwise, it has not achieved the base case yet, then:
    middle = len(lista) // 2
    list_left = merge_sort(lista[:middle]) #list that goes from 0 to middle - 1
    list_right = merge_sort(lista[middle:]) # list that goes from midle to the lenth of the list 

    #when it has finished the list_left and list_right, it's time to merge them, so:
    return merge(list_left, list_right)

def merge(list_left, list_right):
    #base case of the function is:
    if(not list_left): # if list left is empty, return list right
        return list_right
    if(not list_right):
        return list_left 
    #otherwise, sort them recursively
    if(list_left[0] < list_right[0]):
        return [list_left[0]] + merge(list_left[1:], list_right)
    else:
        return [list_right[0]] + merge(list_left, list_right[1:])

def main():
    lista = [1,2,12,66,43,6,32,23]
    print("Unsorted: ", lista) 
    print("Sorted: ", merge_sort(lista)) 

main()