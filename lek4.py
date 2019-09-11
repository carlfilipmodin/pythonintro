# slup generator
# program som rullar en tärning

import random # laddarin in random klassen så att vi kan använda den 

print("vill du rulla en tärning?") # meddela till användaren 
# försök läsa sides som int vid fel sätt sides till 1 
try:
    sides = int(input("hur många sidor?"))
except: 
    print("tärningen behöver 1+ sidor")  
    sides = 1  

run = "y" # vi ger run värdet y som standard 
# så länge tun == y kör loopen 
while run.lower() == "y":

    randomNumber = random.randint(1, sides) # slumpa ett tal mellan 1 och sides 
 
    print(randomNumber) # skriv ut 
    run = input("vill du rulla en till tärning [y/n]: ") # fråga om användaren vill fortsätta rulla en tärning 


