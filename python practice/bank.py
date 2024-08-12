print("Hello, Welcome to Dato's Bank.")
print("                                                                                               ")
answer = input("Do you have account? (Yes/No): ")

has_account = True
if answer == "no" or answer == "No":
    answer_to_create = input("Would you like to create one? (Yes/No): ")
    if answer_to_create == "Yes" or answer_to_create == "yes":
        user_name = input("Enter your name: ")
        password = input("Enter your password: ")
        reenter_password = input("Reenter your password: ")

        if reenter_password == password:
                print("Congratulations! You've craeted an account.")
                balance = int(input("What is your balance?: "))
                balance_course = input("GEL or USD (₾ / $) : ")
                if balance_course == "₾":
                    print("Your balance is", str(balance) + balance_course)
                elif balance_course == "$":
                    print("Your balance is", str(balance) + balance_course)
                else:
                    print("Invalid answer, Enter ₾ or $.")

        while reenter_password != password:
            print("Invalid password")
            reenter_password = input("Reenter your password: ")
            if reenter_password == password:
                print("Congratulations! You've craeted an account.")
                balance = int(input("What is your balance?: "))
                balance_course = input("GEL or USD (₾ / $) : ")
                if balance_course == "₾":
                    print("Your balance is", str(balance) + balance_course)
                    print("                                                                                           ")
                elif balance_course == "$":
                    print("Your balance is", str(balance) + balance_course)
                    print("                                                                                           ")
                while balance_course != "₾" and balance_course != "$":
                    print("Invalid answer, Enter GEL or USD (₾ / $)")
                    balance_course = input("GEL or USD (₾ / $) : ")
                    if balance_course == "₾" or balance_course == "$":
                        print("                                                                                        ")
                        print("Your balance is", str(balance) + balance_course)
                        break
                break
    elif answer_to_create == "No" or answer_to_create == "no":
        print("Exit.")

elif answer =="yes" or answer == "Yes" or answer =="YES":
    print("Amazing!")
    while True:
        try:
            balance = int(input("Enter your balance (Integer only) : "))
            break 
        except ValueError:
            print("That's not an integer. Please try again.")

    balance_course = input("GEL or USD (₾ / $) : ")

    if balance_course == "₾":
        print("                                                                                           ")
        print("Your balance is", str(balance) + balance_course)
        print("                                                                                           ")
    elif balance_course == "$":
        print("                                                                                           ")
        print("Your balance is", str(balance) + balance_course)
        print("                                                                                           ")

    while balance_course != "₾" and balance_course != "$":
        print("Invalid answer, Enter GEL or USD (₾ / $)")
        print("                                                                                           ")
        balance_course = input("GEL or USD (₾ / $) : ")
        if balance_course == "₾" or balance_course == "$":
            print("Your balance is", str(balance) + balance_course)
            break
        
else: 
    print("Invalid answer.")

bank_friends = ["Mom", "Dad", "Brother", "Sister", "Friend", "Grandmother", "GrandFather"]

first_operation = "1. Withdrawal of money"
second_operation = "2. Depositing money"
third_operation = "3. Money Transfer"
fourth_operation = "4. Transfer money to another exchange rate (GEL/USD)"
fifth_operation = "5. Friends"
sixth_operation = "6. Check balance"
seventh_operation ="7. Exit"

while has_account == True:
    print("                                                                                           ")
    print(first_operation)
    print(second_operation)
    print(third_operation)
    print(fourth_operation)
    print(fifth_operation)
    print(sixth_operation)
    print("                                                                                           ")
    user_input = int(input("Which operation would you like to do: "))


    if user_input == 1:
        print("You've chosen the first operation")
        print("                                                                                           ")
        widthrawal_of_money = int(input("How much money do you want to withdraw: "))
        withdraw_course = input("What course do you want to withdraw? (₾ / $): ")

        if widthrawal_of_money > balance and withdraw_course == balance_course:
            print("You don't have that much money on your account!")

        elif widthrawal_of_money < balance and withdraw_course == balance_course:
            balance = balance - widthrawal_of_money
            print("Now your balance is:", str(balance) + balance_course)

        elif withdraw_course == "$" and balance_course =="₾":
            dollar_withdraw_of_money = int(widthrawal_of_money * 2.72)
            if dollar_withdraw_of_money > balance:
                print("                                                                                           ")
                print("You withdraw", str(widthrawal_of_money) + withdraw_course, "and in", balance_course, "it is", str(lari_withdraw_of_money) + balance_course, ".")
                print("You don't have that much money on your account.")
            else:
                balance = balance - dollar_withdraw_of_money
                print("                                                                                           ")
                print("You withdraw", str(widthrawal_of_money) + withdraw_course, "and in", balance_course, "it is", str(dollar_withdraw_of_money) + balance_course)
                print("Now your balance is:", str(balance) + balance_course)    

        elif withdraw_course == "₾" and balance_course =="$":
            lari_withdraw_of_money = int(widthrawal_of_money / 2.72)
            if lari_withdraw_of_money > balance:
                print("                                                                                           ")
                print("You withdraw", str(widthrawal_of_money) + withdraw_course, "and in", balance_course, "it is", str(lari_withdraw_of_money) + balance_course, ".")
                print("You don't have that much money on your account.")
            else:
                balance = balance - lari_withdraw_of_money
                print("                                                                                           ")
                print("You withdraw", str(widthrawal_of_money) + withdraw_course, "and in", balance_course, "it is", str(lari_withdraw_of_money) + balance_course)
                print("Now your balance is:", str(balance) + balance_course)  

 
    elif user_input == 2:
        print("You've chosen the second operation")
        print("                                                                                           ")

        depositing_money = int(input("How much money do you want to deposit?: "))
        depositing_money_course = input("GEL or USD (₾ / $) : ")

        if depositing_money_course == "₾" or depositing_money_course == "$":

            if depositing_money_course == "₾" and balance_course == "$":
                depositing_money = int(depositing_money / 2.72)
                print("You're depositing money in" + " " + depositing_money_course + ". Balance course is in", balance_course +". So your depositing money in", balance_course,"will be", str(depositing_money) + balance_course + ".")
                balance = depositing_money + balance
                print("After this operation, Your balance is :", str(balance) + balance_course)
            elif depositing_money_course == "$" and balance_course == "₾":
                depositing_money = depositing_money * 2.72
                print("You're depositing money in" + depositing_money_course + ". Balance course is in", balance_course +".So your depositing money in", balance_course,"will be", str(depositing_money) + balance_course + ".")
                balance = depositing_money + balance
                print("After this operation, Your balance is :", str(balance) + balance_course)
            else:
                balance = depositing_money + balance
                print("After this operation, Your balance is :", str(balance) + balance_course)

        elif depositing_money_course != "₾" and depositing_money_course != "$":
            while depositing_money_course != "₾" and depositing_money_course != "$":
                print("Invalid anwer, Enter GEL or USD (₾ / $)")
                if depositing_money_course == "₾" or depositing_money_course == "$":
                    break

    elif user_input == 3:
        print("You've chosen the third operation")
        print("                                                                                           ")
        print("Your balance is :", str(balance) + balance_course)
        print("                                                                                           ")
    

        bank_friends = ["Mom", "Dad", "Brother", "Sister", "Friend", "Grandmother", "GrandFather"]
        print("Your friends are:", bank_friends)

        who_to_transfer = input("Who do you want to transfer money to?: ")
        found_friend = False
        
        for i in bank_friends:
            if who_to_transfer == i:
                found_friend = True
                print("You are transfering money to", who_to_transfer, ".")
                break
                
        if not found_friend:
            wanna_add = input("Do you want to add this person in Friends? (Yes/No): ")
            if wanna_add == "Yes" or wanna_add == "yes":
                bank_friends = bank_friends.append(who_to_transfer)
                print("Your friends now are: ", bank_friends)
            elif wanna_add =="No" or wanna_add == "no":
                print("You are transfering money to", who_to_transfer)

            while wanna_add != "yes" and wanna_add != "Yes" and wanna_add != "No" and wanna_add != "no":
                print("Invalid answer, Enter your answer again.")
                if wanna_add == "Yes" or wanna_add == "yes" or wanna_add == "No" or wanna_add == "no":
                    break


        how_much_to_transfer = int(input("How much money do you want to transfer?: "))
        money_transfer_course = input("GEL or USD (₾ / $) : ")

        while money_transfer_course != "₾" and money_transfer_course != "$":
                print("Invalid anwer, Enter GEL or USD (₾ / $)")
                money_transfer_course = input("GEL or USD (₾ / $) : ")
                if money_transfer_course == "₾" or money_transfer_course == "$":
                    break
    
        if money_transfer_course == "₾" and balance_course == "$":
            new_how_much_to_transfer = int(how_much_to_transfer / 2.72)
            if new_how_much_to_transfer > balance:
                print(str(how_much_to_transfer) + money_transfer_course, "in", balance_course, "=", str(new_how_much_to_transfer) + balance_course, ". You don't have that much money on your account")
            else:
                print("You're transfering money in", money_transfer_course,",But balance is in", balance_course,".So your transfered money:", str(how_much_to_transfer) + money_transfer_course,"will be", str(new_how_much_to_transfer) + balance_course)
                balance =  balance - new_how_much_to_transfer
                print("After this operation your balance is :", str(balance) + balance_course)
    

        elif money_transfer_course == "$" and balance_course == "₾":
            new_how_much_to_transfer = int(how_much_to_transfer * 2.72)
            if new_how_much_to_transfer > balance:
                print(str(how_much_to_transfer) + money_transfer_course, "in", balance_course, "=", str(new_how_much_to_transfer) + balance_course, ". You don't have that much money on your account")
            else:
                print("You're transfering money in", money_transfer_course,",But balance is in", balance_course,".So your transfered money ", str(how_much_to_transfer) + money_transfer_course,"will be", str(new_how_much_to_transfer) + balance_course)
                balance = balance - new_how_much_to_transfer
                print("After this operation your balance is :", str(balance) + balance_course)

        #Both my balance and transfered money are in the same course (₾ or $)
        else:  
            if how_much_to_transfer > balance:
                print("You don't have that much money on your balance.")
            else:
                balance = balance - how_much_to_transfer
                print("You've transfered", str(how_much_to_transfer) + money_transfer_course, "to", who_to_transfer)
                print("Your balance now is :", str(balance) + balance_course)


    elif user_input == 4:

        opposite_of_balance_course = ""

        if balance_course == "$":
            opposite_of_balance_course = "₾"
        else:
            opposite_of_balance_course = "$"
        

        print("Your balance is :", str(balance) + balance_course)
        changing_course = input(f"Do you want to change your balance to {opposite_of_balance_course} (Yes/No)? : ")
        #გადაგვყავს თანხა დოლარში.
        if changing_course == "Yes" or changing_course =="yes" and balance_course == "₾":
            balance = int(balance / 2.72)
            print("Your new balance is :", str(balance) + opposite_of_balance_course)
            balance_course = opposite_of_balance_course
        #გადაგვყავს თანხა ლარში.
        elif changing_course == "Yes" or changing_course =="yes" and balance_course == "$":
            balance = int(balance * 2.72)
            print("Your new balance is :", str(balance) + opposite_of_balance_course)
            balance_course = opposite_of_balance_course
        elif changing_course =="No" or changing_course =="no":
            break


    elif user_input == 5:
        print("Your friends are :", bank_friends)  
    

    elif user_input == 6:
        print("Your balance is", str(balance) + balance_course)


    elif user_input == 7:
        print("Thank you for visiting, See you again!")
        break
    else:
        print("Invalid answer, Enter again!")
            


