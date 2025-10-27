weight = 8.4

# Ground Shipping
flat_charge = 20.00
if weight <= 2:
  price_per_pound = 1.50
elif weight > 2 and weight <= 6:
  price_per_pound = 3.00
elif weight > 6 and weight <= 10:
  price_per_pound = 4.00
elif weight > 10:
  price_per_pound = 4.75

cost = weight * price_per_pound + flat_charge
print(f"Ground Shipping: ${cost}")


# Drone Shipping
weight = 1.5

# Ground Shipping
flat_charge = 0
if weight <= 2:
  price_per_pound = 4.50
elif weight > 2 and weight <= 6:
  price_per_pound = 9.00
elif weight > 6 and weight <= 10:
  price_per_pound =12.00
elif weight > 10:
  price_per_pound = 14.25

cost = weight * price_per_pound + flat_charge
print(f" Drone Shipping: ${cost}")



