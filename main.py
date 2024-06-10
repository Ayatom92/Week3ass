#1
list = [1, 2, 3, 6, 10]

my_tuple = tuple(list)
print(my_tuple)


#2
tuple1 = (1, 2)
tuple2 = (3, 4)

tuple3 = tuple1 + tuple2
print(tuple3)


#3
def reverse_tulpe(input):
    return tuple(reversed(input))

input_tuple = (1, 2, 3, 4)
reversed_tuple = reverse_tulpe(input_tuple)
print(reversed_tuple)


#4
def tuple_length(tuple):
    return len(tuple)

tuple = (1, 2, 3, 4)
print(tuple_length(tuple))


#5
tuple = (10, 20, 30)
a, b, c = tuple
print(a, b, c)



#6
def dicts(dict1, dict2):
    dicts = dict1.copy()
    dicts.update(dict2)
    return dicts

dict1 = {"a":1, "b":2}
dict2 = {"c":3, "d":4}
print(dicts(dict1, dict2))    


#7
dicts = {'a':1, "b":2}
key_value = dicts['b']
print(key_value)


#8
def dicts_key(dict, key):
    return key in dict1

dict = {'a': 1, 'b': 2, 'c': 3}
check_key = 'b'


if dicts_key(dict, check_key):
    print(f" The key {check_key} exists in dict")

else:
    print(f"The key {check_key} does not exist in dict")


#9
dict ={'a':1, 'b':2}
for key, value in dict.items():
    print(f"Key: {key}, Value: {value}")


#10
def swap_key_values(dicts):
    return {v: k for k, v in dicts.items()}
dicts = {'a':1, 'b':2}
print(swap_key_values(dicts))


#11
def divided_number(a, b):

    try:
        return a/b
    except ZeroDivisionError:
        return "Division by zero is not allowed"
a=10 
b=0   
print(divided_number(a, b))


#12
def multiple_exceptions(a, b):
    try:
        return a/b
    except (ZeroDivisionError, TypeError) as c:
        return f"An error occured: {c}"
a=10
b=0   
print(multiple_exceptions(a, b))    
print(multiple_exceptions(10, c))


#13
class PositiveIntegerError(Exception):
    pass

def positive_integer(n):
    if not isinstance(n, int) or n <= 0:
        raise PositiveIntegerError("The input is not a positive integer")
    return True

try:
    n = int(input(">"))
    positive_integer(n)
    print('This is positive integer')
except PositiveIntegerError as e:
    print('Error:', e)    


#14
def access_safe(dict, key, default=None):
    return dict.get(key, default)

dict = {'a':1, 'b':2}  
check_key = 'c'
default_value = 0  
print(access_safe(dict, 'c', 'default_value'))


#15
def lastly():
    try:
        print("Try block")
    except Exception as e:
        print(f"Exception: {e}")    
    finally:
        print("This block always excutes")    


lastly()