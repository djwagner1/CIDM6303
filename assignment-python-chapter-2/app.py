#Chapter 2.1 and 2.2 Variables
students_count = 1000
rating = 4.99
is_published = True
course_name = "Python Programming"
print(students_count)
print(rating, is_published, course_name)
print("." * 10)

#Chapter 2.3 Strings
course = "Python Programming"
print(len(course))
print(course[0])
print(course[-1])
print(course[0:3])
print(course[0:]) 
print(course[:3])
print(course[:])
print("." * 10)

#Chapter 2.4 Escape Sequences
#\"
course = "Python \ Programming"
print(course)
# \'
course = "Python \ Programming"
print(course)
# \\
course = "Python \ Programming"
print(course)
print("." * 10)

#Chapter 2.5 Formatted Strings
first = "Sean"
last = "Humphrey's"
full = f"{len(first)} {2 + 2}"
print(full)
print("." * 10)

#Chapter 2.6 String Methods
print("Chapter 2.6 String Methods")
course= "python programming"
print(course.upper())
print(course.lower())
print(course.title())
print(course.rstrip())
print(course.find("Pro"))
print(course.replace("p", "j"))
print("pro" in course)
print("swift" not in course_name)
print("." * 10)

#Chapter 2.7 Numbers"
print("Chapter 2.7 Numbers")
x = 1 #integer
x = 1.1 #float nubmer with decimals
print(10+3)
print(10-3)
print(10*3)
print(10/3)
print(10//3)
print(10%3) #modulous or mod
print(10 ** 3) #exponent

x=10
x=x+3
print(x)
x=10
x+=3 #augmented operator add
print(x)

y=20
y-=3 #augmeted operator subtract
print(y)

z=30
z*=3 #augmented operator multiply
print(z)

#Chapter 2.8 Working with Numbers
print("Chapter 2.8 Working with Numbers")
import math

print(round(2.9))
print(abs(-2.0))
print(math.ceil(2.2))
print("." *10)

#Chapter 2.9 Type Conversion
x = input("Enter a value for x:")
y = int(x) + 1
print(f"x: {x}, y: {y}" )
print("." * 10)

rate = input("Enter a value for x: ")
rate = float(rate)#may reuse the same 
#three different ways to output a number variable with text
print("Borrower does not qualify at {rate}")#string interpolation
print("Borrower does not qualify at ", rate)
print("Borrower does not qualify at " + str(rate))#covnert to string
#Dr. Humphreys likes string interpolation the best!
#\

card_nubmer = "xxx8974"
date = "9/7/2020" 
cookies_cost = 3.15

chips_cost = 4.58
salsa_cost = 5.10
total_cost = cookies_cost + chips_cost + salsa_cost

print("*" * 20)
print("Receipt")
print("Date:", date)
print("$",cookies_cost)
print("$", chips_cost) 
print("$", salsa_cost)
print("")
print("Total:", total_cost)
print("*" * 20)