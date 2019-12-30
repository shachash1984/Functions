#!/usr/bin/python
import copy


def my_func(my_number):
    # print number
    print_number(my_number)
    # add 4 to number
    my_number = divide_number(my_number, 2)
    # add to number
    my_number = add_number(my_number, 4)
    # print number again
    print_number(my_number)
    # return the new number
    return my_number


def print_number(my_number):
    print(my_number)


def divide_number(my_number, divide_by):
    if divide_by == 0 or type(my_number) != int or type(divide_by) != int:
        return None
    return int(my_number/divide_by)


def add_number(my_number, num_to_add):
    if type(my_number) != int or type(num_to_add) != int:
        return  None
    return my_number+num_to_add

### TODO



my_func(20)

# TODO
# add a new function which returns
# True if the number passed is even
# and False otherwise


def is_even(num):
    return num % 2 == 0


print("7 is an even number: " + str(is_even(7)))
print("44 is an even number: " + str(is_even(44)))

# TODO
# create a function which receives
# a list of 1...100 and add 5 to all elements in the list


def add_to_list_by_ref(list_of_nums, add_param=5):
    for i in range(0, len(list_of_nums)):
        list_of_nums[i] += add_param


def add_to_list_by_copy(list_of_nums, add_param=5):
    list_clone = copy.deepcopy(list_of_nums)
    for i in range(0, len(list_of_nums)):
        list_clone[i] += add_param
    return list_clone


list_1_100 = list(range(1, 101))
print("original:")
print(list_1_100)
add_to_list_by_ref(list_1_100, 5)
print("changed:")
print(list_1_100)

list_1_100 = list(range(1, 101))
print("original:")
print(list_1_100)
list_1_to_100_clone = add_to_list_by_copy(list_1_100, 5)
print("changed:")
print(list_1_100)
print("clone:")
print(list_1_to_100_clone)


def count_even_and_odd(list_of_nums):
    counter_even = 0
    counter_odd = 0
    for item in list_of_nums:
        if item % 2 == 0:
            counter_even +=  1
        else:
            counter_odd += 1
    return counter_even, counter_odd


evens, odds = count_even_and_odd(list_1_to_100_clone)
print(evens)
print(odds)

# TODO
# create a function which received a number n
# and returns (n/2)! and (n+1/2)! (factorial)


def get_fact_and_inc_fact(n):
    n_by2_fact = fact(int(n/2))
    n_inc_by2_fact = fact(int((n+1)/2))
    return n_by2_fact, n_inc_by2_fact


def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num*fact(num-1)


print(fact(5))

answers = get_fact_and_inc_fact(5)
print(answers)
