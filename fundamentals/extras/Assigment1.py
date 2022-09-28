#1.Basic
for a in range(0,151):  
    print (a)
#2.Multiples of Five
for x in range(5,1001,5):
    print(x)

#3.Counting, the Dojo Way
for i in range(1,101):
    if i%10==0:
        print("Coding Dojo")
    elif i%5==0:
        print("Coding")
    else: print(i)
#4.Whoa. That Sucker's Huge
sum=0
for b in range(0,500001):
    if b%2==1:
        sum=sum+b
    print(sum)
#5 Countdown by Fours
for c in range(2018,0,-4):
    print(c)

#6 Felxible Counter
lowNum=2
highNum=9
mult=3
for d in range(lowNum,highNum+1):
    if d%mult==0:
        print(d)