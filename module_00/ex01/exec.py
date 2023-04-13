# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alvgomez <alvgomez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/16 13:20:30 by alvgomez          #+#    #+#              #
#    Updated: 2023/04/13 11:52:46 by alvgomez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

n = len(sys.argv)
if n > 1:
	temp_str = sys.argv[1]
	final_str = ""
	for i in range(2, n):
		temp_str += ' ' + sys.argv[i]
	temp_str = temp_str[::-1]
	print(temp_str)
	for char in temp_str:
		if char.isalpha():
			final_str += char.swapcase()
		else:
			final_str += char
	print(final_str)