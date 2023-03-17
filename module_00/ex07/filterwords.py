# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alvgomez <alvgomez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/17 11:56:01 by alvgomez          #+#    #+#              #
#    Updated: 2023/03/17 12:41:52 by alvgomez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string

def create_list(s, numb):
	words = s.split()
	for i in range(len(words)):
		words[i] = words[i].translate(str.maketrans("", "", string.punctuation))
	delete = []
	for item in words:
		if len(item) <= numb:
			delete.append(item)
	for item in delete:
		words.remove(item)
	print(words)

if __name__ == "__main__":
	n = len(sys.argv)
	if n == 3:
		if sys.argv[1].isdigit():
			print("ERROR")
		else:
			s = sys.argv[1]
			if sys.argv[2].isdigit():
				numb = int(sys.argv[2])
				create_list(s, numb)
			else:
				print("ERROR")
	else:
		print("ERROR")