#!/usr/bin/python3.5

#   FUNCTIONS ARE A GREAT WAY TO ORGANIZE YOUR CODE FOR REUSE AND CLARIFY. WRITE A SCRIPT THAT DOES THE FOLLOWING:

#   Prompts the user for a message to echo
#   Prompts the user for the number of times to repeat the message. If no response is given, then the count should default to 1.
#   Defines a function that takes a message and count, then prints the message that many times.

#   TO END THE SCRIPT, CALL THE FUNCTION WITH THE USER-DEFINED VALUES TO PRINT TO THE SCREEN.

message = input("\nPlease enter your message: ")
number = input("\nNumber of repeats [1]:" ).strip()

try:
    number = int(number)
except ValueError:
    number = int(1)


def multi_echo(message, number):
    for i in range(0,number) :
        print(message)

multi_echo(message, number)