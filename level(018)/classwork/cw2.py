#2) მომხმარებელს შემომატანინეთ რიცხვი და შემდეგ დაბეჭდეთ მომხმარებლის შემოტანილი რიცხვი არის თუ არა ხუთის ჯერადი

num = int(input("Enter any number: "))

if num % 5 == 0:
    print("შენი რიცხვი არის 5-ის ჯერადი")
else:
    print("შენი რიცხვი არ არის 5-ის ჯერადი")

# there are several ways of controling the flow in python:
# sequencing : თანმიმდევრობით არჩევა (კოდი იკითხება ზემოდან ქვემოთ);
#  iteration :  იტერაცია, მრავალჯერ კოდის გამეორება (loops)
# selection : სელექცია.

# algorithm : ალგორითმი არის ნაბიჯ ნაბიჯ ინსტრუქცია, რომელიც მიზნამდე მიგვიყვანს.\
# flowchart : ალგორითმის ვიზუალიზაცია.