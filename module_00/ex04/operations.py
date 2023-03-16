# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alvgomez <alvgomez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/16 17:43:11 by alvgomez          #+#    #+#              #
#    Updated: 2023/03/16 18:07:41 by alvgomez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

n = len(sys.argv)
if n > 1:
	assert n < 4, "too many arguments"
	assert n != 2, "not enough arguments"
	A = sys.argv[1]
	B = sys.argv[2]
	assert A.isdigit() and B.isdigit(), "only integers"
	A = int(A)
	B = int(B)
	try:
		print("Sum:        ", A + B)
		print("Difference: ", A - B)
		print("Product:    ", A * B)
		print("Quotient:   ", A / B)
		print("Reminder:   ", A + B)
	except ZeroDivisionError:
		print("Quotient:    ERROR (division by zero)")
		print("Reminder:    ERROR (module by zero)")