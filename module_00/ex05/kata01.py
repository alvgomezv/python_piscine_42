# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alvgomez <alvgomez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/16 18:21:49 by alvgomez          #+#    #+#              #
#    Updated: 2023/04/13 12:19:29 by alvgomez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

kata = {
	'Python': 'Guido van Rossum',
	'Ruby': 'Yukihiro Matsumoto',
	'PHP': 'Rasmus Lerdorf',
}

if len(kata) == 0:
	exit("Dictionary is empty")
for key in kata:
	print(f"{key} was created by {kata[key]}")