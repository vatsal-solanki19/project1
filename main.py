print("Welcome to the interactive persnol data collecter!")

name=input("Please enter your name: ")
age=int(input("Please enter your age: "))
highet=float(input("please enter your highet in meters: "))
number=int(input("Please enter your favourite number: "))

print("Thank you here is the information we collected:")


print(f"Name:{name}(type:{type (name)},memory address:{type(name)})",
      f"Name:{age}(type:{type (age)},memory address:{type(age)})",
      f"Name:{highet}(type:{type (highet)},memory address:{type(highet)})"
      f"Name:{number}(type:{type (number)},memory address:{type(number)})")

current_year=2026
birth_year=current_year-age
print(f"Your birth year is approximately: ",birth_year)
