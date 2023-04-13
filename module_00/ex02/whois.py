# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alvgomez <alvgomez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/16 15:03:38 by alvgomez          #+#    #+#              #
#    Updated: 2023/04/12 17:44:02 by alvgomez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

n = len(sys.argv)
if n > 1:
	assert n == 2, "more than one argument are provided"
	numb = sys.argv[1]
	assert numb.isdigit(), "argument is not an integer"
	numb = int(numb)
	if numb == 0:
		print("I'm Zero")
	elif numb % 2 == 0:
		print("I'm Even")
	else:
		print("I'm Odd")