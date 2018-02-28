print("Exercice : Iterating Over Lists\n\n")

user = { 'admin': False, 'active': False, 'name': 'Kevin' }
isAdmin=False
isActive=False
userName='X'

for key, value in user.items():

    if key == 'active' and value == True:
        isActive=True

    if key == 'admin' and value == True:
        isAdmin=True
    if key == 'name':
        userName = value


if isActive and isAdmin:
    print("ACTIVE - (ADMIN) : %s" % userName )
elif isActive and isAdmin==False:
    print("ACTIVE %s" % userName)
elif isAdmin and isActive==False:
    print("ADMIN %s " % userName)
else:
    print(userName)

print("\n############### USERS LIST #################\n")

users = [
    { 'admin': True, 'active': True, 'name': 'Kevin' },
    { 'admin': True, 'active': False, 'name': 'Elisabeth' },
    { 'admin': False, 'active': True, 'name': 'Josh' },
    { 'admin': False, 'active': False, 'name': 'Kim' },
    { 'admin': True, 'active': True, 'name': 'Marco' },
]

line = 1

for user in users:
    if user['admin'] and user['active']:
        print("%s ACTIVE - (ADMIN) %s" % (line, user['name']))
    elif user['admin']:
        print("%s (ADMIN) %s" % (line, user['name']))
    elif user['active']:
        print("%s ACTIVE - %s" % (line, user['name']))
    else:
        print("%s %s" % (line, user['name']))
    line+=line