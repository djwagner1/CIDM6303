# David Wagner MSFE - CIDM 6303
# Add your code here according to the instructions
# Chapter 4.1 Defining functions

def greet():
    print("Hi there")
    print("Welcome Aboard")
greet()
print("End Chapter 4.1 Defining Functions\n")

# Chapter 4.2 Arguments. This chapter demonstrate two arguments
# Note. You cannot have functions with the same name in the same file,
# which is why we change the name to greet2().

def greet2(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome Aboard")

greet2("Ada", "Lovelace") #Google who Ada Lovelace was
print("***End Chapter 4.2 Arguments\n")

#Chapter 4.3 Types of Functions
#Function of 'Do Tasks'
def greet3(name):
    print(f"Hi {name}")

print(greet3("Ada"))

# Function of 'return value'
def greet4(name):
    return(f"Hi {name}")

message = greet4("Sophie Wilson")
print(message)
message = greet4("Grace Hopper")
print(message)
message = greet4("Ida Rhodes")
print(message)
print("***End of Chapter 4.3 Types of Functions\n")

# Chapter 4.4 Keyword Arguments
def increment(number, by):
    return number + by

print(increment(2, by=1))
print("***End Chapter 4.4 Keyword Arguments\n")

# Chapter 4.5 Default Arguments
def increment_default(number, by=1):
    return number + by

print(increment_default(2,5))
print("***End of Chpater 4.5 Default Arguments\n")

#Chapter 4.5 Xargs
def mulitply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print(mulitply(2,3,4,5))
print(mulitply(55,87))
print(mulitply(100,98,77,4,-5,72,0.5))
print("***End Chapter 4.6 Xargs\n")


#Chapter 4.6 Xargs
def mulitply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print(mulitply(2,3,4,5))
print(mulitply(55,87))
print(mulitply(100,98,77,4,-5,72,0.5))
print("***End Chapter 4.6 Xargs\n")


#Chapter 4.7 xxargs
def save_user(**user):
    print(user["name"])

save_user(id=1,name="John", age=22)
print("***End of Chapter 4.7 xxargs\n")


#Chapter 4.8 Scope
message= "don't use global variables"

def greetings(name):
    global message
    message = "this is a local variable"

greetings("sean")    
print(message)
print("***End of Chapter 4.8 Scope\n")

#Chapter 4.9 Debugging
#Watch the video and learn how to debug. Nothing to code.

#Chapters 4.10 & 4.11 VSCode Coding Tricks
#Watch the video and learn how to debug. Nothing to code.


