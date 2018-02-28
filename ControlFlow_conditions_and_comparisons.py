print(1<2)
print(3.0>=3)

if True:
    print("Es verdadero")

name = 'Marko'
if len(name) >= 5:
    print("name is long")
elif len(name)==4:
    print("name is average")
else:
    print("name is short")



print("################ Control flow ################")
go = True
while go:
    print("We're going")
    go = False

count = 0
while count < 10:
    if count % 2 ==0:
        print(count)
    count = count + 1

colors = ['green','purple','gray','black','orange','brown']
for color in colors:
    print(color)

ages = {'Marco':33, 'Julieta':3, 'Valeria':4, 'Veronica':37}
for key, value in ages.items():
    print(value)