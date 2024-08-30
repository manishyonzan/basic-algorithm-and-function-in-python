import csv

name = input("whats your name?")
home  = input("whats your home?")

with open("students.csv","a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])

# with open("students.csv",'a') as file:
#     writer = csv.DictWriter(file, fieldnames=["home","name"])
#     writer.writerow({ "name":name, "home": home})