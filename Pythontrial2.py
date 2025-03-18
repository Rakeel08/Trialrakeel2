# variables

greeting = 'Hello world'
print(greeting)

# example for me #

my_name = "Rachel Ruguru"
print(my_name)

greeting = "Hello"
print(greeting + my_name)

print(greeting)


name = input("What's your name? ")
age = input("How old are you? ")

# Convert age to an integer and calculate the year they turn 100
try:
    age = int(age)
    year_100 = 2024 + (100 - age)
    print(f"Hello, {name}! You will turn 100 years old in the year {year_100}.")
except ValueError:
    print("Oops! Please enter a valid number for your age.")


