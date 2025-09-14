def print_list(items):
    if len(items) == 0: 
    #letting user know if there are no entries in the list
        result = 'Please enter atleast one item in list'
        return result
    if len(items) == 1: #if one item in list, print out just the one entry
        for name in items:
            result = name
        return result
    if len(items) == 2: # Handle two items case - format as "item1 and item2"
        result = ''
        for names in items:
            if names == items[-1]:
                result += ' and ' + str(names)
            else:
                result += str(names)
        return result
    if len(items) > 2: # Handle 3+ items case - format as "item1, item2 and item3"
        result = ''
        for names in items:
            if names == items[-1]:
                result += 'and ' + str(names) 
            else:
                result += str(names) + ', '
        return result

#all test list lengths
food_list0 = [] #empty
food_list1 = ['beans'] #one entry
food_list2 = ['beans', 'rice'] #two entries
food_list4 = ['beans', 'rice', 'toast', 'bread'] #3+ entries
food_list5 = ['beans', 'rice', 'toast', 'bread', 7, 1.0] #3+ entries + int + float

#prints functions
print(print_list(food_list0))
print(print_list(food_list1))
print(print_list(food_list2))
print(print_list(food_list4))
print(print_list(food_list5))

# print(type(x)) #checked that data type is in fact str
# print(type(y))
# print(type(z))
# print(type(a))
# print(type(b))