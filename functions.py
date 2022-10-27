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

x[1][0] = 15
students[0]['last_name'] = 'Brayan'

sports_directory['soccer'][0] = 'Andres'

z[0]['y'] = 30
print(z)

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

def iterateDictionary(students):
    for x in range(len(students)):
        for key, value in students[x].items():
            print(key + " - " + value + ", " + list(students[x].keys())[1] + " - " + students[x]['last_name'])
            break

iterateDictionary(students)


def iterateDictionary2(key_name, students):
    if key_name == '':
        return False
    elif key_name == 'first_name':
        for x in range(len(students)):
            print(students[x][key_name])
    elif key_name == 'last_name':
        for x in range(len(students)):
            print(students[x][key_name])

iterateDictionary2('last_name', students)


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dojo):
    count = 0
    for key, value in dojo.items():
        print(str(len(value)) + " " + key)
        for x in range(len(value)):
            print(dojo[key][x])
        count+=1

printInfo(dojo)






