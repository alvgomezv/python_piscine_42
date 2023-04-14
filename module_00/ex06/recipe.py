# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alvgomez <alvgomez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/17 10:22:31 by alvgomez          #+#    #+#              #
#    Updated: 2023/04/14 11:29:38 by alvgomez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

cookbook = {
    "sandwich" : {
        "ingredients" : ["ham", "bread", "cheese", "tomato"], 
        "meal" : "lunch", 
        "prep_time" : 1
    },
    "cake" : {
        "ingredients" : ["flour", "sugar", "eggs"], 
        "meal" :"dessert", 
        "prep_time" : 60
    },
    "salad" : {
        "ingredients" : ["avocado", "arugula", "tomato", "spinach"], 
        "meal" :"lunch", 
        "prep_time" : 15
    },
}

def print_recipe_names():
    i = 1
    if not cookbook:
        print("No recipes in cookbook")
    else:
        for key in cookbook:
            print(f"   recipe {i}: {key}")
            i += 1
    print('')
    
def print_details(key):
    print(f"Recipe for {key}:")
    print(f"    Ingredients list: {cookbook[key]['ingredients']}")
    print(f"    To be eaten for {cookbook[key]['meal']}")
    print(f"    Takes {cookbook[key]['prep_time']} minutes of cooking")
    print('')

def delete_recipe(key):
    del cookbook[key]
    print(f"Recipe {key} has been deleted")
    print('')

def add_recipe():
    n = len(cookbook)
    print("Enter a name:")
    name = input()
    if name in cookbook:
        print("Recipe already in cookbook")
        return False
    if not name:
        print("Recipe must have name")
        return False
    print("Enter ingredients:")
    ing = []
    value = input()
    while value:
        ing.append(value)
        value = input()
    print("Enter a meal type:")
    meal = input()
    if not meal:
        print("Recipe must have a meal type")
        return False
    meals = ["appetizer", "lunch", "dessert"]
    if meal not in meals:
        print(f"Not a meal type, It must be: {meals}")
        return False
    print("Enter a preparation time:")
    time = input()
    cookbook[name] = {"ingredients" : ing, "meal": meal, "prep_time": time}
    print('')
    return True
    
if __name__ == "__main__":
    print("Welcome to the Python Cookbook!")
    print("List of available options:")
    print("  1: Add a recipe")
    print("  2: Delete a recipe")
    print("  3: Print a recipe")
    print("  4: Print the cookbook")
    print("  5: Quit\n")
    print("Please select an option:")
    print(">> ", end="")
    n = input()
    while n != '5':
        if n == '1':
            if add_recipe() == True:
                print("Recipe added")
            else:
                print("Error at adding recipe, please try again")
        elif n == '2':
            print("Please enter a recipe name:")
            key = input()
            if key in cookbook:
                delete_recipe(key)
            else:
                print("Recipe does not exist")
                print("")
        elif n == '3':
            print("Please enter a recipe name:")
            key = input()
            if key in cookbook:
                print_details(key)
            else:
                print("Recipe does not exist")
                print("")
        elif n == '4':
            print_recipe_names()
        else:
            print("")
            print("Sorry, this option does not exist")
            print("")
            print("List of available options:")
            print("  1: Add a recipe")
            print("  2: Delete a recipe")
            print("  3: Print a recipe")
            print("  4: Print the cookbook")
            print("  5: Quit\n")
        print("Please select an option:")
        print(">> ", end="")
        n = input()
    print("")
    print("Cookbook closed. Goodbye!")
        