# 1) მომხმარებელს შემოატანინეთ ორი რიცხვი, შემდეგ კი შეადარეთ ეს ორი რიცხვი ერთმენთს, მიღებული მნიშვნელობა შეინახეთ ცვლადში და შემდეგ დაბეჭდეთ მისი მონაცემთა ტიპი და მნიშვნელობა.

num1 = int(input("Enter any number: "))
num2 = int(input("Enter second number: "))

comparison = num1 > num2
print(comparison)
print(type(comparison))   #boolean
