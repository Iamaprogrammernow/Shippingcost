weight = 41.5
#ground shipping
if weight <= 2:
  groundcost = weight * 1.5
elif weight > 2 and weight <= 6 :
  groundcost = weight * 3
elif weight <= 10 > 6 :
  groundcost = weight * 4
elif weight >10:
  groundcost = weight * 4.75
groundcost = groundcost + 20
ground_shipping_premium = 125

#drone shipping
if weight <= 2:
  dronecost = weight * 4.5
elif weight <= 6 > 2:
  dronecost = weight * 9
elif weight <= 10 > 6 :
  dronecost = weight * 12
elif weight > 10:
  dronecost = weight * 14.25

print('Weight: ')
print(weight)

print('Ground Shipping Premium: ')
print(ground_shipping_premium)
print('Ground shipping cost: ')
print(groundcost)
print('Drone shipping cost: ')
print(dronecost)

