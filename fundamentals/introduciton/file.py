num1 = 42#variable declaration
num2 = 2.3#variable declaration
boolean = True # Boolean
string = 'Hello World'#variable declaration
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #- List 

person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}#Dictionary
fruit = ('blueberry', 'strawberry', 'banana')#Tuples
print(type(fruit)) #log statement
print(pizza_toppings[1])# #log statement
pizza_toppings.append('Mushrooms')# - list-add value
print(person['name']) #Dictionary  - access value
person['name'] = 'George'#Dictionary  - change value
person['eye_color'] = 'blue'#Dictionary  - add value
print(fruit[2]) #Tuples- access value

if num1 > 45:#- conditional
             #- if
             #- else if
             #- else
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5): #for loop start
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0 
while(x < 5):#white loop start
    print(x)
    x += 1

pizza_toppings.pop()#- List delete value
pizza_toppings.pop(1)#- List delete value

print(person) #- log statement
person.pop('eye_color')#Dictionary delete value
print(person)#- log statement

for topping in pizza_toppings:#for loop
    if topping == 'Pepperoni':#if statement
        continue#for loop continue
    print('After 1st if statement')#log
    if topping == 'Olives':
        break#for loop  break

def print_hello_ten_times():#function
    for num in range(10):#for loop
        print('Hello')#log statement

print_hello_ten_times() #call function

def print_hello_x_times(x):#function
    for num in range(x):#for loop
        print('Hello')#log statement

print_hello_x_times(4)#call function

def print_hello_x_or_ten_times(x = 10):#function
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)#call function


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)