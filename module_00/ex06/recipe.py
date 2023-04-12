# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alvgomez <alvgomez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/17 10:22:31 by alvgomez          #+#    #+#              #
#    Updated: 2023/04/12 17:58:27 by alvgomez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

cookbook = {
    "sandwich" : [["ham", "bread", "cheese", "tomato"], "lunch", 10],
    "cake" : [["flour", "sugar", "eggs"], "dessert", 60],
    "salad" : [["avocado", "arugula", "tomato", "spinach"], "lunch", 15],
}

def print_recipe_names():
    i = 1
    for key in cookbook:
        print(f"   recipe {i}: {key}")
        i += 1
    print('')
    
def print_details(key):
    print("Recipe for cake:")
    print(f"    Ingredients list: {cookbook[key][0]}")
    print(f"    To be eaten for {cookbook[key][1]}")
    print(f"    Takes {cookbook[key][2]} minutes of cooking")
    print('')

def delete_recipe(key):
    del cookbook[key]
    print('')

def add_recipe():
    n = len(cookbook)
    print("Enter a name:")
    name = input()
    print("Enter ingredients:")
    ing = []
    value = input()
    while value:
        ing.append(value)
        value = input()
    print("Enter a meal type:")
    meal = input()
    print("Enter a preparation time:")
    time = input()
    cookbook[name] = [ing, meal, time]
    print('')
    
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
            add_recipe()
        elif n == '2':
            print("Please enter a recipe name:")
            key = input()
            if key in cookbook:
                delete_recipe(key)
            else:
                print("Recipe does not exist")
                print("")
        elif n == '3':
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
        