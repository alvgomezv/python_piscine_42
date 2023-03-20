# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sos.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alvgomez <alvgomez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/20 10:08:20 by alvgomez          #+#    #+#              #
#    Updated: 2023/03/20 11:14:22 by alvgomez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string

code = { "a" : ".-", "b" : "-...", "c" : "-.-.", "d" : "-..", "e" : ".", 
		 "f" : "--.-", "g" : "--.", "h" : "....", "i" : "..","j" : ".---",
		 "k" : "-.-","l" : ".-..","m" : "--","n" : "-.","o" : "---",
		 "p" : ".--.","q" : "--.-","r" : ".-.","s" : "...","t" : "-",
		 "u" : "..-","v" : "...-","w" : ".--","x" : "-..-","y" : "-.--",
		 "z" : "--..","A" : ".-","B" : "-...","C" : "-.-.","D" : "-..",
		 "E" : ".","F" : "--.-","G" : "--.","H" : "....","I" : "..",
		 "J" : ".---","K" : "-.-","L" : ".-..","M" : "--","N" : "-.",
		 "O" : "---","P" : ".--.","Q" : "--.-","R" : ".-.","S" : "...",
		 "T" : "-","U" : "..-","V" : "...-","W" : ".--","X" : "-..-",
		 "Y" : "-.--","Z" : "--..","0" : "-----","1" : ".----","2" : "..---",
		 "3" : "...--","4" : "....-","5" : ".....","6" : "-....","7" : "--...",
		 "8" : "---..","9" : "----.",
}

def convert_to_morse(list):
	morse = []
	for word in list:
		new_word = word
		new_word = " ".join(new_word)
		for key in code:
			new_word = new_word.replace(key, code[key])
		morse.append(new_word)
	return morse
			
def create_list(string):
	list = string.split()
	return list

if __name__ == "__main__":	
	n = len(sys.argv)
	if n > 1:
		final = []
		for args in range(1, n):
			string = sys.argv[args]
			list = create_list(string)
			morse = convert_to_morse(list)
			final = final + morse
		print(" / ".join(final))