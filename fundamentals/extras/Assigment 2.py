#1 Countdown
def countdown(num):
    list=[]
    while num>=0:
        list.append(num)
        num=num-1
    print(list)
countdown(20)       
#2 Print and Return
def print_and_return(arr):
    print(arr[0])
    return arr[1]
#3 First Plus Length
def first_plus_length(list):
    print(list[0]+len(list))
#4 Values Greater than Second
def values_greater_than_second(list1):

    if len(list1)>2:
        list2=[]
        for x in list1:
            if x>list1[1]:
                 list2.append(x)
        print(len(list2))
        return(list2)
    else: print("False")
#5 This length, That Value
def length_and_value(size, value):
    list3=[]
    for i in range(0,size):
        list3.append(value)
    print(list3)
length_and_value(4,7)

