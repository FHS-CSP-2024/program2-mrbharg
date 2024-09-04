# Information from the user #
#**Learning objectives**
#
#After this section:
#
#* You will know how to write a program which uses input from the user
#* You will know how to use variables to store input and print it out
#* You will be able to combine strings



## Live Demo ##
#
# Input from user
#name = input("What is your name? ")
#print("Hi there, " + name)
#
# Talk about Variables
#   * Note python is untyped and loose
#
# Reference a Var
#name = input("What is your name? ")
#print("Hi, ")
#print(name)
#print("!")
#print(name + " is quite a nice name.")
#
# Concat w/ +
#name = input("What is your name? ")
#print("Hi " + name + "! Let me make sure: your name is " + name + "?")
#
# Multiple Input
#name = input("What is your name? ")
#email = input("What is your email address? ")
#nickname = input("What is your nickname? ")
#print("Let's make sure we got this right")
#print("Your name: " + name)
#print("Your email address: " + email)
#print("Your nickname: " + nickname)
#
# Overriding Input
#name = input("What is your name? ")
#print(name)
#name = input("What is another name? ")
#print(name)



## Problem 1 ##
#Please write a script that: 
# - Asks for the user's name and then prints it twice, on two consecutive lines.

name = input("What is your name? ")
print("Hello " + name)
print("Nice to meet you " + name)



## Problem 2 ##
#Please write a script that: 
# - Asks for the user's name
# - Prints it out twice on a single line so that there is an exclamation mark at the beginning of the line, 
# - another between the two names and a third one at the end of the line.

name2 = input("What is your name? ")
print("!" + name2 + "!" + name2 + "!")
print("Lebron James, Drake, " + name2 + ", Ryan Reynolds")


## Problem 3 ##
#Please write a script that: 
# - Asks for the user's name and address. 
# - The program should also print out the given information, as follows:
#   - Sample output
#   - First name: Steve
#   - Last name: Sanders
#   - Street address: 91 Station Road
#   - City and postal code: Folsom CA, 95630

name3 = input("What is your name? ")
last_name = input("What is your last name? ")
address = input("What is your street address? ")
city = input("What city do you live in? ")
postal_code = input("What is your postal code? ")

print("First Name: " + name3)
print("Last Name: " + last_name)
print("Street Address: " + address)
print("City and postal code: " + city + ", " + postal_code)

## Problem 4 ##
#Please write a script that: 
# - Asks for 3 words 
# - Puts the words together with dashes and prints that out

word = input("List one word? ")
word2 = input("List one word? ")
word3 = input("List one word? ")

print(word + ", " + word2 + ", " + word3)

## Problem 5 ##
#Please write a script that: 
# - Asks for a name and a year
# - Prints out a short story that uses that information
# Sample output:
#Please type in a name: Mary
#Please type in a year: 1572
# ----------------------------------------------
#Mary is a valiant knight, born in the year 1572. 
#One morning Mary woke up to an awful racket: a dragon was approaching the village. 
#Only Mary could save the village's residents.

name4 = input("What is your name? ")
year = input("What year is it? ")
print(name4 + " is a time traveler coming back to the year " + year + ".")
print("One day " + name4 + " got stuck in the grips of time, floating through space alone.")
print("Only the time machine could save " + name4 + " now!")