# 3) ამოირჩიეთ აქედან ერთერთი პროექტი რომელსაც თქვენი ჯგუფი გააკეთებს:  "ბანკის პროექტი" , "chatbot დიალოგი", "ჯეირანი"


# 4) შეამოწმეთ როგორი არის რიცხვი, ანუ დადებითია თუ უარყოფითი,და დააბრუნეთ საპირისპირო ნიშნის მქონე რიცხვი, ანუ თუ დადებითია დაპრინტეთ  უარყოფითი, ხოლო თუ უარყოფითია დაპრინტეთ დადებითი.

number = int(input("Enter any number: "))

if number < 0:
    number = number * (-1)
    print("You chose a negative number.")
    print("This number will be:", number, ", if you want it to be positive")
elif number > 0:
    number = number * (-1)
    print("You chose a positive number.")
    print("This number will be:", number,", if you want it to be negative ")
else:
    print("Number is equal to 0.")