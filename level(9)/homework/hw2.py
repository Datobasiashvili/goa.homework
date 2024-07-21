# 2) შექმენით დროში მოგზაურობის პროგრამა, რომელიც მომხმარებელს შეეკითხება მის ამჟამინდელ ასაკს, ამჟამინდელ წელს, რამდენი წლით სურს დროში მოგზაურობა, შემდეგ კი პროგრამა დაბეჭდავს დროში მოგზაურობის შემდეგ რომელი წელი იქნება და რამდენი წლის იქნება მომხმარებელი დროში მოგზაურობის შემდეგ

age = int(input("What is your age?: "))
year = int(input("What year is it now?: "))
time_travel = int(input("How many years do you want to travel in time?: "))

print("After time traveling, it will be year", year + time_travel + ", And you will be", age + time_travel, "years old!")
