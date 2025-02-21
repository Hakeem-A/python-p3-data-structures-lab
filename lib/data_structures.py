spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [spicy_food["name"] for spicy_food in spicy_foods]
print(get_names(spicy_foods))

def get_spiciest_foods(spicy_foods):
    return [spicy_food for spicy_food in spicy_foods if spicy_food["heat_level"] > 5]
print(get_spiciest_foods(spicy_foods))

def print_spicy_foods(spicy_foods):
    for spicy_food in spicy_foods:
        heat_level =  "🌶" * spicy_food["heat_level"]
        print(f"{spicy_food['name']} ({spicy_food['cuisine']}) | Heat Level: {heat_level}")
print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    return next((food for food in spicy_foods if food ["cuisine"].lower() == cuisine.lower()), None)

print(get_spicy_food_by_cuisine(spicy_foods, "thai"))

def print_spiciest_foods(spicy_foods):
    for spicy_food in spicy_foods:
        if spicy_food["heat_level"] > 5:
            heat_level = "🌶" * spicy_food["heat_level"]
            print(f"{spicy_food['name']} ({spicy_food['cuisine']}) | Heat Level: {heat_level}")

def get_average_heat_level(spicy_foods):
    return sum(food["heat_level"] for food in spicy_foods) // len(spicy_foods)

def create_spicy_food(spicy_foods, new_food):
    spicy_foods.append(new_food)
    return spicy_foods
