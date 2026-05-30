def main():
    coke_price = 50
    coin_inserted = 0
    print("Amount Due: ", coke_price)
    while (coin_inserted < coke_price):
        coin = int(input("Insert Coin: "))
        if coin in [25, 10, 5]:
            coin_inserted += coin
            amount_due = coke_price - coin_inserted
            if amount_due > 0:
                print("Amount Due: ", amount_due)
            else:
                print("Change Owed: ", coin_inserted-coke_price)
        else:
            print("Invalid Coin Inserted!!")
            exit()
        

main()