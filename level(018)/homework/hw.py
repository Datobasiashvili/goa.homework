#Bank project using  if elif else
print("Welcome to Datos bank! \n")
print("ATTENTION! In input field, If you enter any other option, It will be an Error!\n")
answer = input("Do you have an account? (Yes/No): ")

if answer == "No" or answer == "no":
    print("Sign Up!\n")
    user_name = input("Enter your username: ")
    password = input("Enter your password (8 or less characters): ")

    while len(password) > 8:
        print("Invalid password, It should be less than 8 characters!\n")
        password = input("Enter your password (8 or less characters):\n ")
        if len(password) <= 8:
            break
    age = int(input("Enter your age: "))

elif answer == "Yes" or answer == "yes":
    print("Congratulations!")
else:
    print("Invalid answer!")

balance = int(input("Enter your balance: "))
balance_currency = input("Enter your currency (₾ / $ / €): ")

while balance_currency != "₾" and balance_currency != "$" and balance_currency != "€":
    print("Invalid input, Try again!")
    balance_currency = input("Enter your currency (₾ / $ / €): ")
    if balance_currency == "₾" or balance_currency == "$" or balance_currency == "€":
        break



user_balance = str(balance) + balance_currency
print("Your balance is: ", user_balance, "\n")

first_operation = "1. Depositing Money."
second_operation = "2. Withdraw Money."
third_operation = "3. Exchange The Currency."
fourth_operation = "4. Check Account Balance."
fifth_operation = "5. Exit.\n"

while True:
    print(first_operation)
    print(second_operation)
    print(third_operation)
    print(fourth_operation)
    print(fifth_operation)

    choice = int(input("Enter your operation (1-5): "))
    
    if choice == 1:
        print("You've chosen the first operation!\n")
        print("Your balance is: ", str(balance) + balance_currency)
        depositing_money = int(input("Enter how much money do you want to Deposit?: "))
        if depositing_money < 0:
            print("Invalid answer")
            break
        currency = input("In what currency do you want to Deposit money? (₾ / $ / €): ")
        depo = str(depositing_money) + currency

        if balance_currency == "₾" and currency == "€":
            depositing_money = depositing_money * 3
            balance = balance + depositing_money
            print("You are depositing:", depo)
            print("Your depositing money in", balance_currency,"will be", str(depositing_money) + balance_currency + "\n")
            print("Your balance after this operation is: ", str(balance) + balance_currency)
        elif balance_currency == "₾" and currency == "$":
            depositing_money = int(depositing_money * 2.7)
            balance = balance + depositing_money
            print("Your are depositing:", depo)
            print("Your depositing money in", balance_currency,"will be", str(depositing_money) + balance_currency +'\n')
            print("Your balance after this operation is: ", str(balance) + balance_currency)
        elif balance_currency == "$" and currency == "₾":
            depositing_money = int(depositing_money / 2.7)
            balance = balance + depositing_money
            print("Your are depositing:", depo)
            print("Your depositing money in", balance_currency,"will be", str(depositing_money) + balance_currency +'\n')
            print("Your balance after this operation is: ", str(balance) + balance_currency)
        elif balance_currency == "$" and currency == "€":
            depositing_money = int(depositing_money / 0.9)
            balance = balance + depositing_money
            print("Your are depositing:", depo)
            print("Your depositing money in", balance_currency,"will be", str(depositing_money) + balance_currency +'\n')
            print("Your balance after this operation is: ", str(balance) + balance_currency)
        elif balance_currency == "€" and currency == "₾":
            depositing_money = int(depositing_money / 3)
            balance = balance + depositing_money
            print("Your are depositing:", depo)
            print("Your depositing money in", balance_currency,"will be", str(depositing_money) + balance_currency +'\n')
            print("Your balance after this operation is: ", str(balance) + balance_currency)
        elif balance_currency == "€" and currency == "$":
            depositing_money = int(depositing_money * 0.9)
            balance = balance + depositing_money
            print("Your are depositing:", depo)
            print("Your depositing money in", balance_currency,"will be", str(depositing_money) + balance_currency +'\n')
            print("Your balance after this operation is: ", str(balance) + balance_currency)
        elif balance_currency == currency:
            balance = balance + depositing_money
            print("You are depositing:", depo, "\n")
            print("Your balance after this operation is: ", str(balance) + balance_currency)
        else:
            print("Invalid answer!")
    
    elif choice == 2:
        print("You've chosen second operation!\n")
        print("Your balance is: ",str(balance) + balance_currency)

        withdraw_money = int(input("How much money do you want to withdraw?: "))
        if withdraw_money < 0:
            break
        withdraw_money_currency = input("In which course do you want to withdraw money? (₾ / $ / €): ")
        
        if balance_currency == "₾" and withdraw_money_currency == "$":
            withdraw_money_dollar = int(withdraw_money * 2.7)
            if withdraw_money_dollar > balance:
                print("You don't have that much money on your account!\n")
            else:
                balance = balance - withdraw_money_dollar
                print("You withdrew:", str(withdraw_money) + withdraw_money_currency, "\n")
                print("This Amount in", balance_currency,"is", str(withdraw_money_dollar) + balance_currency, "\n")
                print("Your balance after this operation is: ", str(balance) + balance_currency)
        elif balance_currency == "₾" and withdraw_money_currency == "€":
            withdraw_money_euro = int(withdraw_money * 3)
            if withdraw_money_euro > balance:
                print("You withdrew:", str(withdraw_money) + withdraw_money_currency, ",that in", balance_currency, "is", str(withdraw_money_euro) + balance_currency, "\n")
                print("You don't have that much money on your account!\n")
            else:
                balance = balance - withdraw_money_euro
                print("You withdrew:", str(withdraw_money) + withdraw_money_currency, "\n")
                print("This Amount in", balance_currency,"is", str(withdraw_money_euro) + balance_currency, "\n")
                print("Your balance after this operation is: ", str(balance) + balance_currency)
        elif balance_currency == "$" and withdraw_money_currency == "₾":
            withdraw_money_dollar = int(withdraw_money / 2.7)
            if withdraw_money_dollar > balance:
                print("You withdrew:", str(withdraw_money) + withdraw_money_currency, ",that in", balance_currency, "is", str(withdraw_money_dollar) + balance_currency, "\n")
                print("You don't have that much money on your account!\n")
            else:
                balance = balance - withdraw_money_dollar
                print("You withdrew:", str(withdraw_money) + withdraw_money_currency, "\n")
                print("This Amount in", balance_currency,"is", str(withdraw_money_dollar) + balance_currency, "\n")
                print("Your balance after this operation is: ", str(balance) + balance_currency)
        elif balance_currency == "$" and withdraw_money_currency == "€":
            withdraw_money_dollar = int(withdraw_money / 0.9)
            if withdraw_money_dollar > balance:
                print("You withdrew:", str(withdraw_money) + withdraw_money_currency, ",that in", balance_currency, "is", str(withdraw_money_dollar) + balance_currency, "\n")
                print("You don't have that much money on your account!\n")
            else:
                balance = balance - withdraw_money_dollar
                print("You withdrew:", str(withdraw_money) + withdraw_money_currency, "\n")
                print("This Amount in", balance_currency,"is", str(withdraw_money_dollar) + balance_currency, "\n")
                print("Your balance after this operation is: ", str(balance) + balance_currency)
        elif balance_currency == "€" and withdraw_money_currency == "$":
            withdraw_money_dollar = int(withdraw_money * 0.9)
            if withdraw_money_dollar > balance:
                print("You withdrew:", str(withdraw_money) + withdraw_money_currency, ",that in", balance_currency, "is", str(withdraw_money_dollar) + balance_currency, "\n")
                print("You don't have that much money on your account!\n")
            else:
                balance = balance - withdraw_money_dollar
                print("You withdrew:", str(withdraw_money) + withdraw_money_currency, "\n")
                print("This Amount in", balance_currency,"is", str(withdraw_money_dollar) + balance_currency, "\n")
                print("Your balance after this operation is: ", str(balance) + balance_currency)
        elif balance_currency == "€" and withdraw_money_currency == "₾":
            withdraw_money_dollar = int(withdraw_money / 3)
            if withdraw_money_dollar > balance:
                print("You withdrew:", str(withdraw_money) + withdraw_money_currency, ",that in", balance_currency, "is", str(withdraw_money_dollar) + balance_currency, "\n")
                print("You don't have that much money on your account!\n")
            else:
                balance = balance - withdraw_money_dollar
                print("You withdrew:", str(withdraw_money) + withdraw_money_currency, "\n")
                print("This Amount in", balance_currency,"is", str(withdraw_money_dollar) + balance_currency, "\n")
                print("Your balance after this operation is: ", str(balance) + balance_currency)
        elif balance_currency == withdraw_money_currency:
            if withdraw_money > balance:
                print("You don't have that much money on your account!")
            else:
                balance = balance - withdraw_money
                print("You withdrew:", str(withdraw_money) + withdraw_money_currency)
                print("Your balance after this operation is: ", str(balance) + balance_currency)
        else:
            print("Invalid answer")
            break

    elif choice == 3:
        print("You've chosen the third operation!\n")
        exchange = input("In what currency do you want to exchange your balance in? (₾ / $ / €): ")
        if exchange == "₾" or exchange == "$" or exchange == "€":
            if exchange == balance_currency:
                print("Your Balance is in that currency\n")
            else:
                if exchange == "₾" and balance_currency == "$":
                    balance = int(balance * 2.7)
                    balance_currency = exchange
                    print("You are exchanging your balance in", exchange, "\n")
                    print("Your balance after this operation is: ", str(balance) + balance_currency)
                elif exchange == "₾" and balance_currency == "€":
                    balance = int(balance * 3)
                    balance_currency = exchange
                    print("You are exchanging your balance in", exchange, "\n")
                    print("Your balance after this operation is: ", str(balance) + balance_currency)
                elif exchange == "$" and balance_currency == "₾":
                    balance = int(balance / 2.7)
                    balance_currency = exchange
                    print("You are exchanging your balance in", exchange, "\n")
                    print("Your balance after this operation is: ", str(balance) + balance_currency)
                elif exchange == "$" and balance_currency == "€":
                    balance = int(balance * 0.9)
                    balance_currency = exchange
                    print("You are exchanging your balance in", exchange, "\n")
                    print("Your balance after this operation is: ", str(balance) + balance_currency)
                elif exchange == "€" and balance_currency == "$":
                    balance = int(balance * 0.9)
                    balance_currency = exchange
                    print("You are exchanging your balance in", exchange, "\n")
                    print("Your balance after this operation is: ", str(balance) + balance_currency)
                elif exchange == "€" and balance_currency == "₾":
                    balance = int(balance / 3)
                    balance_currency = exchange
                    print("You are exchanging your balance in", exchange, "\n")
                    print("Your balance after this operation is: ", str(balance) + balance_currency)
    
    elif choice == 4:
        print("You've chose the fourth operation!\n")
        print("Your balance is: ", str(balance) + balance_currency, "\n")
    
    elif choice == 5:
        print("Your exiting DATOs bank. Have a nice day!\n")
        break