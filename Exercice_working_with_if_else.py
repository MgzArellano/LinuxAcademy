user = {'admin':True, 'active':True, 'name':'Marco'}

isAdmin= user['admin']
isActive = user['active']

if isAdmin:
    print("ADMIN "+user['name'])
else:
    print(user['name']+" is not admin")
if isActive:
    print("ACTIVE "+ user['name'])
else:
    print(user['name']+" is not active")
if isActive and isAdmin:
    print("ACTIVE - (ADMIN) "+user['name'])
else:
    print(user['name'])