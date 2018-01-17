def taxes():
  total = 0
  for x in range(3):
    prod = input("Is this item tobacco, gasoline, alcohol, or none?" )
    price = float(input("What is the price of this item?"))
    location = input("Is this purchased in Birmingham?")
    
    if location == "yes": #Birmingham products tax
      if prod == "gasoline":
        price = price + (price * 0.08) + 1.60
      if prod == "tobacco":
        price = price + (price * 0.08) + 2.00
      if prod == "alcohol":
        price = price + (price * 0.08) +5
      if prod == "none":
        price = price + (price * 0.08)
  
    if location == "no": #Non Birmingham products tax
      if prod == "gasoline":
        price = price + (price*0.04) + 1.60
      if prod == "tobacco":
        price = price + (price*0.04) + 2.00
      if prod == "alcohol":
        price = price + (price *0.04) +5
      if prod == "none":
        price = price + (price *0.04)
    print ("The price of this item is "+ str(price))
    total = total + price
  print ("Total price is " + str(total))

taxes()

