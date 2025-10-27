# Your code below:
toppings = ["pepperoni", 'pineapple', 'cheese', 'sausage', 'cheese', 'olives', 'anchovies', 'mushrooms']

prices = [2, 6, 1,3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)
num_pizzas = len(toppings)

print(f"We sell {num_pizzas} different kinds of pizza!")

pizzas_and_prices = [[2, 'pepperoni'], 
  [6, 'pineapple'], [1, 'cheese'], [3, 'sausage', [2, 'olives'], [7, 'anchovies', [2, 'mushrooms']]]]

pizzas_and_prices.sort()
print(pizzas_and_prices)

cheapest_pizza = pizzas_and_prices[0]
priciest_pizza = pizzas_and_prices[-3]

pizzas_and_prices.insert(3, [2.5, "peppers"])
pizzas_and_prices.sort()
print(pizzas_and_prices)

three_cheapest = pizzas_and_prices[:3]
print(three_cheapest)