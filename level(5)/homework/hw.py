# 1) გააკეთეთ 3 ცალი სწორი კოდი და 3 ცალი არასწორი კოდი და უნდა ახსნათ რატომ არის ეს კოდი სწორი და რატომ არის ეს კოდი არასწორი

#3 ცალი სწორი კოდი :
name = input("What is your name? : ")
print("Hello " + name)
hobby = "Coding"
print(name + " loves " + hobby + ".")

#3 ცალი არასწორი კოდი 

# item -> "pen" ცვლადს რომ მივანიჭოთ value საჭიროა ტოლობის ნიშანი.

age = 17
name = "Dato"
print(name + " is " + age + " years old.") # არ შეგვიძლია სტრინგისა და ინტეგერის მიმატება, age უნდა იყოს სტრინგი: str(age)


color = "Red"
print("color") #თუ კი გვსურს რომ დაიპრინტოს red, color უნდა ჩავწეროთ ბრჭყალების გარეშე - print(color)


# 2) ახსენით debugger-ი რაარის კომენტარებით და გააკეთეთ ასევე მაგალითებიც
#debugger არის კოდში დაშვებული შეცდომების პოვნა და შესწორება.


# 3) შექმენით ცვლადი რომელიც იქნება name და მინიჭებული იქნება თქვენი სახელი და უნდა დაპრინტოთ ეს ცვლადი სწორი გზით და არასწორი გზით და უნდა ახსნათ კომენტარებით რატომ არის ეს გზა სწორი და რატომ არ არის ეს გზა სწორი

name = "Dato"
print("name") #არასწორია, რადგან დაიპრინტება name და არა Dato.
print(name) #სწორია, რადგან დაიპრინტება Dato


# 4) დაპრინტეთ GOA is the best academy in georgia სწორი გზით და არასწორი გზით და ახსენით კომენტარებით რატომ არის ეკ გზა სწორი და რატომ არ არის მეორე გზა სწორი

print("GOA is the best academy in Georgia.") #სწორია
#print("GOA is the best academy in Georgia) არასწორია, რადგან საჭიროა მეორე ბრჭყალი.
       