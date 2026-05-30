results = ["Mario", "Luigi"]

results.append("Princess")
results.append(["Yoshi", "Koopa Troopa", "Toad"])
results.remove(["Yoshi", "Koopa Troopa", "Toad"])
results.extend(["Yoshi", "Koopa Troopa", "Toad"])
results.remove("Luigi")
results.insert(0, "Luigi")
results.reverse()



print(results)