def Coke_machine():
    ammount_due = 50
    accepted_coins = [5, 10, 25]
    
    while ammount_due>0:
        insert_coin = int(input(f"Ammount due: {ammount_due}, please insert coin (We accept 5, 10, 25 gold coins): "))
        if insert_coin in accepted_coins:
            ammount_due=ammount_due-insert_coin
        else:
            print("We do not accept this coin, here is your money back!")
    print(f"Charge owed: {abs(ammount_due)}")

Coke_machine()