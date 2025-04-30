#The filter() function
#The filter() function filters elements from an iterable
# based on a specified condition.
# It only keeps elements for which the function returns True.


#Syntax

#   filter(function, iterable)
# function: The function to use as the condition, returning True or False.
# iterable: The collection of items to filter.



# Filtering out even numbers from a list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


# Key Differences:
# map(): Transforms each element of the iterable based on the
# given function.

# filter(): Selects only those elements that satisfy a given condition
# (i.e., when the function returns True).