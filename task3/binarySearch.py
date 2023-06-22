def binarySearch(list, value):
    steps = 0
    left = 0
    right = len(list) - 1

    while left <= right:
        steps += 1
        middle = (left+right) // 2

        if list[middle] == value:
            return f'Value found in {steps} steps, at position {middle}.'
        elif list[middle] > value:
            right = middle - 1
        else:
            left = middle + 1
    return 'Item not found'

# List with the different guests of la mente del hacker by Zepo
list = ['Andrés Prado','Enrique Rodríguez','José Luis Villanueva','Juan Carlos Galindo','Manuel Huerta','Raúl Guillén','Suko','Telmo Xavier','Yolanda Corral']
name = 'Suko'

'''
For the binary search to work correctly, our String list must be sorted in alphabetical order,
if the list is not provided in this way, we must sort it beforehand using list.sort().
'''
position = binarySearch(list,name)
print(position)