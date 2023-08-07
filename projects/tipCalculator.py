#Data types
# print("Hello"[0]) H
# print("Hello"[:3]) Hel
# print(round(8/3,3))

# a = 8 // 3
# print("Result is" + a) #Error
# print(f"Result is {a}") #f-string to add other data typed values to string message
print("Welcome to the tip calculator")
bill = float(input("Total bill in dollar: $"))
tip = int(input("Percentage tip? 10,12 or 15: "))
people = int(input("Number of people: "))
share = (bill * (1 + tip/100))/people
# share = "{:.2f}".format(share)
# print(f"Person's share: ${round(share,2)}")
print(f"Person's share: ${'{:.2f}'.format(share)}")