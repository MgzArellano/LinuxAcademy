print("this")
print('that')
print("double".find('e'))
print("pasar a mayúsculas".upper())
print("Todo a Minúsculas".lower())
print("concatenando "+"pass"+"word")
print("multiplicando cadenas x 4   " * 4)
print("tab\tdelimited")
print("*space\ndelimited*")
print("scape\\caracter(barra)")
print("'Single quotes' in the middle of double quotes")
print('"Double quotes" in the middle of single quotes')
print("\"double\" quotes in the middle of double quotes")

print("enteros "+str(5+6))
print("floats "+str(5.0+6))
print("float con muchos decimals "+str(5/3.0))
print("float con pocos decimals "+str(5//3.0))
print("parsing to int    "+str(int("1")))
print("parsing to float  "+str(float("1.0")))
print("parsing number to string  "+str(5.5)) # it is not important if the number is a float or a int

##################  DATA TYPES BOOLEANS AND NONE ####################
print("boolean".__contains__("cat"))
print(1>4)

## validar si un número es par o non
num = 7
if (num%2==0):
    print("par")
else:
    print("none")
## fin de la validación si es par o non
print("################# working with variables ##################")
print("")
a_word = "bacon"
print(a_word)
my_int = 3
print(my_int)
print("")
print("################# List and Tuples ##################")
my_list = [1, 'a', 2.0, True, False]
print(my_list[3])
print("the lenght of my list is "+str(len(my_list)))
print(my_list[-3])
my_list.append("nuevoElemento")
print(my_list)
my_list.append("OtroEl")
my_list.append(66)
my_list.append(None)
print(my_list)
print("---")
my_list[1:4]=[]
print(my_list)
my_list[-1]="NewElementInEnglish"
print(my_list)
my_list.remove("NewElementInEnglish")
print("new list")
print(my_list)
my_list.remove(my_list[2])
print(";;;;;")
print(my_list)
my_list.clear()
print(my_list)
print("//////////// new list //////////////")
new_list = [1,2,3,4,5]
print(new_list)
new_list.pop()
print(new_list.pop())
print(new_list)
print("################### Tuples ####################")
point = (2.0, 3.9)
print(point[0])
print("my name is %s " % " Keith")
print("Mi nombre es %s %s ans I am %s" % (" Marco", "Arellano", 33))
print("################### Dictionaries ####################")
ages = {'Marco':33,'Valeria':4, 'Julieta':3, 'Verónica':37}
print(ages['Marco'])
ages['Marco']=34
print(ages)
ages.pop('Marco')
print(ages)
print("printing keys")
print(ages.keys())
print("printing values")
print(ages.values())
print("printing items")
print(ages.items())
print("a dictionary can also by created as  following:   dictionario = dict('key'=value) // works only for numbers")
capitales = dict(Veracruz=10, Hidalgo=20, NuevoLeón=30, Coahuila=40, Tabasco=50)
print(capitales)

