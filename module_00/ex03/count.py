# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alvgomez <alvgomez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/16 15:50:54 by alvgomez          #+#    #+#              #
#    Updated: 2023/03/16 17:40:10 by alvgomez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def text_analyzer(s=""):
	import string
	'''
	This function counts the number of upper characters, lower characters, 
	punctuation and spaces in a given text.'''
	if not s:
		print("What is the text to analyze?")
		s = input()
		assert s.isdigit() == False, "argument is not a string"
	assert isinstance(s, str), "argument is not a string"
	print(f"The text contains {len(s)} character(s):")
	print(f"- {sum(1 for c in s if c.isupper())} upper letter(s)")
	print(f"- {sum(1 for c in s if c.islower())} lower letter(s)")
	print(f"- {sum(1 for c in s if c in string.punctuation)} punctuation mark(s)")
	print(f"- {s.count(' ')} space(s)")

if __name__ == "__main__":
	n = len(sys.argv)
	assert n < 3 , "more than one argument are provided"
	if n == 1:
		text_analyzer()
	elif n == 2:
		s = sys.argv[1]
		assert s.isdigit() == False, "argument is not a string"
		text_analyzer(s)