
#PREDICT THE FUNCTIONS OUTPUT

#1
# This code would print five cuz the function return is 5.
# def number_of_groups():
#     return 5
# print(number_of_groups())

# 2
# This code would error cuz number_of_days_in_a_week is not defined.
# def number_of_military_branches():
#     return 5
# print(number_of_days_in_a_week() + number_of_military_branches)

# 3
# This code would print 5, cuz a function could only return one thing.
# def number_of_books_on_hold():
#     return 5
#     return 10
# print(number_of_books_on_hold())

# 4
# This function would print 5, cuz a function is finished once it returned something.
# def number_of_fingers():
#     return 5
#     print(10)
# print(number_of_fingers())

# 5
# This function would print 5 and none, cuz we have one print statement inside the function which has the value 5 and cuz the function is not returning anything to the caller it prints none as the value of x. 
# def number_of_great_lakes():
#     print(5)
# x = number_of_great_lakes()
# print(x)

# 6
# This function would print 3 and 5 and error. cuz the function is not returning anything so its non and can't add nons.
# def add(b,c):
#     print(b+c)
# print(add(1,2) + add(2,3))

# 7
# This function would print 25, cuz we used the str method which concatenates the 2 and 5 from int to string.
# def concate(b,c):
#     return str(b) + str(c)
# print(concate(2,5))

# 8
# This function would print 100, 10. The return block inside the if block or else block will cause the function to exit and return value. The return 7 will never be executed as the function has already returned the value 10.
# def number():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(number())

# 9
# The first function call, would print 7, cuz the condition is true.
# The second function call would print 14, cuz the if condition is false and else would run.
# The third function call would 21, cuz the first function call if is true which would return 7 and second call else is true which will return 14 and at the end in the print statement the could would add both returns and print the result which is 21.
# return 3, would never run.
# def number_of_weeks(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(number_of_weeks(2,3))
# print(number_of_weeks(5,3))
# print(number_of_weeks(2,3) + number_of_weeks(5,3))

# 10
# When the code runs it will first print 500.
# Second step, prints 500 again cuz the print statement is before the function call
# third step, function is called, and would print 300.
# last step would print 500 again.
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
# print(b)
# foobar()
# print(b)

# 11
# This function would return 8, and the last return would never run.
# def addition(a,b):
#     return a+b
#     return 10
# print(addition(3,5))

# 12
#this code would print 1, 3, 5 and 10
# def foo():
#     print(1)
#     x = bar()
#     print(x)
#     return 10
# def bar():
#     print(3)
#     return 5
# y = foo()
# print(y)

