
mystring = "abcdefghijk"
# Indexing example is below, use numbers to pick what letter you want to grab from the varible.
#print(mystring[-2])

#Slicing Example
#Stop index goes UP TO but not including
#print(mystring[:3])

#print(mystring[3:6])

teams = ["Bengals", "Seahawks", "Bears", "49ers", "Bills"]

#for team in teams:
  #print(f"The {team.title()}, are a great team!")
  #print(f"Lets see what the {team.title()} do in the playoffs.")


favorite_pizzas = ["Pepperoni", "Margherita", "Barbecue Chicken"]

for i, pizza in enumerate(favorite_pizzas):
    print(f"{i+1}. {pizza}")
