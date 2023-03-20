# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alvgomez <alvgomez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/20 16:40:47 by alvgomez          #+#    #+#              #
#    Updated: 2023/03/20 17:20:19 by alvgomez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Recipe:
	def __init__(self, n, l, tm, i, d, rt):
		if isinstance(n, str) and isinstance(l, int) and isinstance(tm, int) and isinstance(i, list) and isinstance(rt, str):
			self.name = n
			self.cooking_lvl = l
			self.cooking_time = tm
			self.ingredients = i
			self.recipe_type = rt
			self.description = d
		else:
			return print("Format must be: Name(str), Cooking level(int), Cooking time(int) Ingredients(list), Recipe type(str)")
		
	def __str__(self):
		txt = f"Name: {self.name}\nCooking level(1-5): {self.cooking_lvl}\nCooking time: {self.cooking_time} min\nIngredients: {self.ingredients}\nDescription: {self.description}\nRecipe type: {self.recipe_type}\n"
		return txt

if __name__ == "__main__":
	tourte = Recipe("omelette", 4, 50, ["eggs", "potato"], "Spanish dish", "lunch")
	print(str(tourte))