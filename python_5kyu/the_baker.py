def cakes(recipe, available):
    ingredients = []
    recipe_list = []
    for key, value in available.items():
        ingredients.append(value)
    for key, value in recipe.items():
        recipe_list.append(value)
    print(ingredients)
    print(recipe_list)




recipe1 = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available1 = {"sugar": 500, "flour": 2000, "milk": 2000}

cakes(recipe1, available1)