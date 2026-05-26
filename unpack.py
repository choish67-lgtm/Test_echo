#first, last = input("what's your name? ").split(" ")
#first, _ = input("what's your name? ").split(" ")
#print(f"hello, {first}")

def total(galleons, sickles, knuts):
    return (galleons *17 + sickles) * 29 +knuts

#coins = [100, 50, 25]
coins = {"galleons": 100, "sickles": 50, "knuts": 25}


#print(total(100, 50, 25), "Knuts")
#print(total(coins[0], coins[1], coins[2]), "Knuts")
#print(total(*coins), "Knuts")   # '*' shows how to unpack coins for list
#print(total(coins), "Knuts")   # This doesn't work

print(total(**coins), "Knuts") # '**' shows how to unpack coins for dictionary