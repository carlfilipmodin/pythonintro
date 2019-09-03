# variabler för att komma ihåg namn och ålder

# läsa in namn

name = input("skriv in ditt namn: ") 


# läsa in ålder

age = int(input("skriv din ålder"))

# skriva ut hej namn och du är x gammal 

print("hejsan", "name,","Välkommen till mitt program.")
print ("du är", age, " gammal")



# skriva ut om du är 18 eller inte 
if age < 18:
    print ("du har inte fyllt 18 ännu")
else:
    print ("du har fyllt 18")

