# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alvgomez <alvgomez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/20 16:40:34 by alvgomez          #+#    #+#              #
#    Updated: 2023/03/21 17:35:23 by alvgomez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from datetime import date

class Book:
	def __init__(self, n):
			self.name = n
			self.last_update = date.today()
			self.creation_date = date.today()
			self.recipes_list = {"starter":[], "lunch":[], "dessert":[]}

	def get_recipe_by_name(self, name):
		"""Imprime la receta con el nombre \texttt{name} y devolver la instancia"""
		for recipe_name in self.recipes_list:
			for recipe in self.recipes_list[recipe_name]:
				if recipe.name == name:
					print(name)
					return recipe
		
	def get_recipes_by_types(self, rt):
		"""Devuelve todas las recetas dado un recipe_type """ 
		for recipes in self.recipes_list[rt]:
			print(recipes)
		
	def add_recipe(self, recipe):
		"""Añade una receta al libro y actualiza last_update"""
		self.recipes_list[recipe.recipe_type].append(recipe)
		self.last_update = date.today()
		
