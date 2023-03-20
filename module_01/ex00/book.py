# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alvgomez <alvgomez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/20 16:40:34 by alvgomez          #+#    #+#              #
#    Updated: 2023/03/20 18:35:30 by alvgomez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import datetime
from recipe import Recipe

class Book:
	def __init__(self, n, lu, cd, rl):
		if isinstance(n, str) and isinstance(lu, int) and isinstance(cd, int) and isinstance(rl, dict):
			self.name = n
			self.last_update = lu
			self.creation_date = cd
			self.recipes_list = rl
		else:
			return print("Format must be: Name(str), Last update(datetime), Creation date(datetime) Recipes list(dict)")

	def get_recipe_by_name(self, name):
		"""Imprime la receta con el nombre \texttt{name} y devolver la instancia"""
		
	def get_recipes_by_types(self, rt):
		"""Devuelve todas las recetas dado un recipe_type """ 
		
	def add_recipe(self, recipe):
		"""Añade una receta al libro y actualiza last_update""" 
		
if __name__ == "__main__":
	tourte = Recipe("omelette", 4, 50, ["eggs", "potato"], "Spanish dish", "lunch")
	print(str(tourte))
	uno = Book("uno", 20, 20, {"starter":[], "lunch":["tourte"], "dessert":[]})
	uno.get_recipe_by_name("omelette")
