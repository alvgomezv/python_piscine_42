# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alvgomez <alvgomez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/16 13:20:30 by alvgomez          #+#    #+#              #
#    Updated: 2023/03/16 13:49:49 by alvgomez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

n = len(sys.argv)
if n > 1:
	final_str = sys.argv[1]
	for i in range(2, n):
		final_str = final_str + ' ' + sys.argv[i]
	final_str = final_str [::-1]
	final_str = final_str.swapcase()
	print(final_str)