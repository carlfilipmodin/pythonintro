print ("välkommen till mitt program där du kan addera")
operator = input("välj räknesätt(+,-,*): ")
try:
     tal1= int(input("mata in ett heltal"))
     tal2= int(input("mata in ett heltal"))
except:
    print ("du måste skriva in en siffra")
    tal1 = 0
    tal2 = 0
if operator == "+":
    summa = tal1 + tal2
elif operator == "-":
    summa="?"
elif operator == "/":
    summa= tal1/tal2
    try:
        tal1/tal2 
    except ZeroDivisionError:
      print("du kan inte dela med 0")
elif operator == "*":
    summa= tal1 * tal2

else:
    print("RÖR DEN INTE")
print("summa är:" + str(summa))




