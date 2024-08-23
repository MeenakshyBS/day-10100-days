myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
tip = float(input("what % of tip you want to leave?(15%, 18%, 20%): "))
tip = tip / 100
tip = myBill*tip
myBill = myBill + tip
answer = myBill / numberOfPeople
answer = round(answer, 2)
print("You all owe", answer)