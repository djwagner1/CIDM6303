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