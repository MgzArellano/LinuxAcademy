#!/usr/bin/python

# Exercise: Creating and Using Functions
#
#Functions are a great way to organize your code for reuse and clarity. Write a script that does the following:

    #Prompts the user for a message to echo
    #Prompts the user for the number of times to repeat the message. If no response is given, then the count should default to 1.
    #Defines a function that takes a message and count, then prints the message that many times.

#To end the script, call the function with the user-defined values to print to the screen.

mensaje = input("\nPor favor ingresa un mensaje: ")
num_repeticiones = input("\nNúmero de repeticiones [ Default 1 ]: ")

try:
    num_repeticiones=int(num_repeticiones)
except ValueError:
    num_repeticiones = 1


def multi_msj(mensaje, num_repeticiones):
    while num_repeticiones > 0:
        print(mensaje)
        num_repeticiones -= 1

multi_msj(mensaje, num_repeticiones)