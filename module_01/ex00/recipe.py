# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alvgomez <alvgomez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/20 16:40:47 by alvgomez          #+#    #+#              #
#    Updated: 2023/03/21 17:33:41 by alvgomez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Recipe:
	def __init__(self, n, l, tm, i, d, rt):
		if not n:
			print("There must be a name")
		else:
			self.name = n
		try:
			self.cooking_lvl = int(l)
			self.cooking_time = int(tm)
		except:
			print("cooking_lvl and cooking_time must be integers")
		if isinstance(i, list):
			self.ingredients = i
		else:
			print("Ingredients must be a list")
		try:
			self.recipe_type = rt
		except:
			print("There must be a recipe type")
		self.description = d
		
	def __str__(self):
		txt = f"Name: {self.name}\nCooking level(1-5): {self.cooking_lvl}\nCooking time: {self.cooking_time} min\nIngredients: {self.ingredients}\nDescription: {self.description}\nRecipe type: {self.recipe_type}\n"
		return txt
	
	def get_recipe_type(self):
		return self.recipe_type
	
	def get_recipe_by_name(self):
		return self.name
