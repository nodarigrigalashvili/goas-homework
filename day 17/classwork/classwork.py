def list(list):
       return " ".join(list)

print(list(["hello", "world"]))

def list(list):
       two = " wow ".join(list)
       one = 0
       for i in list:
              one += 1
       return one, two
print(list(["omg", "omg", "omg"]))

name = "nodo"

# მე დავადეკლარირე ცვლადი სახელად name და მივეცი მნიშვნელად "nodo" მერე ამ ცვლადის მნიშვნელი გამოვიძახე პრინტის საშვალებით
# და .capitalize(), .upper(), და .lower() ფუნქციის მეშვეობით მათი ასოების ფორმა შევცვალე
# და .find() ფუნქციის საშვალებით ცვლადში კონკრეტული ასოს მოძიება ვცადე
#.capitalize() ადიდებს პირველ ასოს სტრინგის
#.upper() აპატარავებს სუყველა ასოს სტრინგში
#.lower() ადიდებს ყველა ასოს სტრინგში
#.find() პოვულობს კონკრეტულ ასოს სტრინგში და იმ სტრინგის კნკრეტულ ასოს პირველად მისვლაზე ჩერდება და აღარ აგრძელებს მეტის პოვნას




print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.find("o"))
