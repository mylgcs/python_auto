def find_max_two(items):
    first, secnd = (items[0],items[1] if items[0] >= items[1] \
         else (items[1],items[0]))
    for index in range( 2, len(items)):
        if items[index] > first:
            secnd = first
            first = items[index]
        elif items[index] > secnd:
            secnd = items[index]
    return first,secnd

list1=[1,2,3,4,5]

print(find_max_two(list1))