def print_list(list):
    try:
    #tests if list is all str values, if not then typeerror raised and error given to user
        test = ''
        for names in list:
            test += names + '' #try to concatenate, if not str, cant happen, so typeerror raised
    except TypeError:
        error = 'Non str data type detected --> Please only enter str values in list.'
        return error

    if len(list) == 0: 
    #letting user know if there are no entries in the list
        result = 'Please enter atleast one item in list'
        return result
    if len(list) == 1: #if one item in list, print out just the one entry
        for name in list:
            result = name
        return result
    if len(list) == 2: # Handle two items case - format as "item1 and item2"
        result = ''
        for names in list:
            if names == list[-1]:
                result += ' and ' + names
            else:
                result += names
        return result
    if len(list) > 2: # Handle 3+ items case - format as "item1, item2 and item3"
        result = ''
        for names in list:
            if names == list[-1]:
                result += 'and ' + names 
            else:
                result += names + ', '
        return result

#all test list lengths
food_list0 = [] #empty
food_list1 = ['beans'] #one entry
food_list2 = ['beans', 'rice'] #two entries
food_list4 = ['beans', 'rice', 'toast', 'bread'] #3+ entries
food_list5 = ['beans', 'rice', 'toast', 'bread', 7, 1.0] #if not str is passed, caught by try/except clause

#executes functions
x = print_list(food_list0)
y = print_list(food_list1)
z = print_list(food_list2)
a = print_list(food_list4)
b = print_list(food_list5)

#prints functions
print(x)
print(y)
print(z)
print(a)
print(b)
print(type(x)) #checked that data type is in fact str
print(type(y))
print(type(z))
print(type(a))
print(type(b))