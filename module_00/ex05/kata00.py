# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata00.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alvgomez <alvgomez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/16 18:09:34 by alvgomez          #+#    #+#              #
#    Updated: 2023/04/13 12:52:33 by alvgomez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

kata = (1,23)

if len(kata) == 0:
	exit("Tuple is empty")
s = str(kata[0])
for i in range(1, len(kata)):
	s = s + ', ' + str(kata[i])
print(f"The {len(kata)} number(s) are: {s}")