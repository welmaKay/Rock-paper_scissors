a = "Hello, World"
print(a[7])

a ="Hello, World"
print(a.upper())
# these are methods to use

a = "Hello, World!"
print(len(a))

b = "Hello, World!"
print(b[2:5])
# 2 is being included and 5 excluded
 
a = "juice"
b = "water"
c = (a[2:5])

print(c.capitalize() + " "+ b.capitalize())

a = "5"
b = 2
print(a*b)

def get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total_sqft = sqft_walls + sqft_ceiling
    gallons_needed = total_sqft / sqft_per_gallon
    total_cost = gallons_needed * cost_per_gallon
    return total_cost

# Example usage:
cost = get_cost(800, 200, 350, 25)
print(cost)