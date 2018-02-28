#!/usr/bin/python

print("\nExecuting shell commands from Within Python\n")

#import os commands

import subprocess

code = subprocess.call(['ls', '-la'])
if code == 0:
    print("Command executed successfylly...")
else:
    print("\n\nFailed with code: %i\n\n" % code)

print("\n\n**** Capturando la salida de un comando ****\n\n")

output = subprocess.check_output(['ls','-l'])
print('Salida = %s\n' % output)


print("\n\n**** Manejando los errores ****\n\n")



try:
    salida = subprocess.check_output(
        "ls fake.txt",
        stderr=subprocess.STDOUT
    )
except OSError as err:
    salida = err
except subprocess.CalledProcessError as err:
    print("Caught CalledProcessError")
    salida = err

print('---'+str(salida))