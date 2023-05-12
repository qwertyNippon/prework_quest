#Orlando Henry
# Question 1:
# Write a function to print “hello_USERNAME!” USERNAME is 
#the input of the function. The first line of the code has 
#been defined as below.

user_name = 'username'

def hello_name(user_name):
	print('hello_' + '(user_name)'.upper() + '!')

hello_name(user_name)

#Question 2
#Write a python function, first_odds that prints the odd
# numbers from 1-100 and returns nothing

def first_odds():
    for num in range(1, 100, 1):
        if num % 2 == 1:
            print('Odd numbers are', num )

first_odds()

#Question 3
#Please write a Python function, max_num_in_list to return
# the max number of a given list. The first line of the code
#  has been defined as below.

num_in_list = [1,2,3,6,5,4,7,8,9]

def max_num_in_list(a_list):
    max =num_in_list [0]
    for i in num_in_list:
        if i > max:
            max = i
            
    print(' out of loop' , max)
            
max_num_in_list(num_in_list)



#Question 4
#Write a function to return if the given year is a leap
# year. A leap year is divisible by 4, but not divisible
# by 100, unless it is also divisible by 400. The return
# should be boolean Type (true/false).


a_year = False

def is_leap_year(a_year):
    if a_year % 4 == 0:
    	a_year = True, print('Is a Leap Year')
    else:
         a_year = False
         print('Not a Leap Year')

is_leap_year(2024)
print(type(a_year))

#Below is where I used to test my code, I'm not sure 
#about the use of improper tabs.
print('https://www.w3schools.com/python/trypython.asp?filename=demo_ref_range')


#Question 5
#Write a function to check to see if all numbers in list
# are consecutive numbers. For example, [2,3,4,5,6,7] are
# consecutive numbers, but [1,2,4,5] are not consecutive
# numbers. The return should be boolean Type.


def is_consecutive(a_list):