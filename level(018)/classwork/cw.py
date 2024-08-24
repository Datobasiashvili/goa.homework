#1) მომხმარებელს შემოატანინოთ რიცხვი, შემდეგ კი დაბეჭდეთ ეს რიცხვი კენტია თუ ლუწი

number = int(input("Enter any number (integer only): "))

if number % 2 == 1:
    print("Your number is odd!")
else:
    print("Your number is even!")