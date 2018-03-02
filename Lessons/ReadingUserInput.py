#!/bin/python

def gather_info():
    name = input("What is your name? ")
    birthdate = input("When is your birthday? ")
    age = input("What is your age? ")
    return (name, birthdate, age)


def print_info(name, birthdate, age):
    print("\nYour name is %s, your birthday date is %s, your age is %s " % (name, birthdate, age))



def calculo_imc():
    print("\nCálculo de tu IMC\n")
    peso = float(input("Ingresa tu peso: "))
    estatura = float(input("Indica tu estatura: "))
    imc = peso/(estatura**2)
    print("\nTu IMC de acuerdo a tu peso y estatura (%s kg y %s mts) es: %s" % (peso,estatura,round(imc,2)))


#executing the user name
name, birthday, age = gather_info()
print_info(name=name, birthdate=birthday, age=age)

#calling the calculo_imc function
calculo_imc()

