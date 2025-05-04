

def sort_array():
    
    array = input("Enter values for the array separeted by spaces: ").split()
    array = [int(value) for value in array]
    
    ascending = sorted(array)
    descending = sorted(array, reverse=True)
    

    print("Array in ascending order:", ascending)
    print("Array in descending order:", descending)


sort_array()
