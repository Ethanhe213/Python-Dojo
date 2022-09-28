#1 Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1-1 
x[1][0]=15
#1-2 
students[0]['last_name']='Bryant'
#1-3
sports_directory['soccer'][0]="Andres"
#1-4
z[0]['y']=30

#2 Iterate Through a List of Dictionaries

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(list):
    for a in list:
        for b,c in a.items():
            print(b+"-"+c)
           
iterateDictionary(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
#3 Get Values From A list of Dictionaries
def iterateDictionary2(key_name, some_list):
    for a in range(0,len(some_list)):
        f_name=some_list[a][key_name]
        print(f_name)
iterateDictionary2('last_name', students)
#4 Iterate Through a Dictoinary with List Values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dojo):
    for a,c in dojo.items():
        print(str(len(c))+" "+(a.upper()))
        for b in c:
            print(b)
            
printInfo(dojo)


