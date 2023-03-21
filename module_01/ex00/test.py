# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alvgomez <alvgomez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/20 16:40:56 by alvgomez          #+#    #+#              #
#    Updated: 2023/03/21 17:34:51 by alvgomez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from book import Book
from recipe import Recipe

book = {
    "omelette" : {
		"cooking_lvl" : 4,
        "cooking_time" : 50,
        "ingredients" : ["eggs", "potato"],
        "description" : "Spanish dish",
        "type" : "lunch"
	},
    "cake" : {
    	"cooking_lvl" : 2,
        "cooking_time" : 30,
        "ingredients" : ["eggs", "flour", "milk"],
        "description" : "",
        "type" : "dessert"
	},
    "nachos" : {
		"cooking_lvl" : 1,
        "cooking_time" : 10,
        "ingredients" : ["nachos", "avocado", "cheese"],
        "description" : "super good",
        "type" : "starter"
	}
}

#omelette = Recipe("omelette", 4, 50, ["eggs", "potato"], "Spanish dish", "lunch")
#cake = Recipe ("cake", 2, 30, ["eggs", "flour", "milk"], "", "dessert")
#nachos = Recipe ("nachos", 1, 10, ["nachos", "avocado", "cheese"], "super good", "starter")

if __name__ == "__main__":
	my_book = Book("my_book")
	
	for key, value in book.items():
		temp = Recipe(key, value["cooking_lvl"], value["cooking_time"], value["ingredients"], value["description"], value["type"])
		my_book.add_recipe(temp)
	
	my_book.get_recipes_by_types("dessert")
	recipe = my_book.get_recipe_by_name("omelette")
	print()
	print(recipe)