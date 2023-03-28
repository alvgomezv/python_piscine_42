# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generator.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alvgomez <alvgomez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/24 12:29:48 by alvgomez          #+#    #+#              #
#    Updated: 2023/03/28 13:21:52 by alvgomez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from random import randint

def generator(text, sep=" ", option=None):
    '''Divide el texto de acuerdo al valor de sep y producirá las sub-strings.
        option especifica si una acción se realizará sobre las sub-strings antes de ser producidas.
    '''
    if isinstance(text, str) and isinstance(sep, str) and (option == None or option == "shuffle" or option == "unique" or option == "ordered"):
        list = text.split(sep)
        if option == "ordered":
            list.sort()
            return list
        elif option == "unique":
            new = set(list)
            return new
        elif option == "shuffle":
            new = []
            while len(new) != len(list):
                pos = randint(0, len(list) - 1)
                if list[pos] not in new:
                    new.append(list[pos])
            return new
        else:
         return list
    else:
        print("ERROR")

if __name__ == "__main__":
    text = "Le Lorem Ipsum est simplement du faux texte."
    for word in generator(text, sep=" ", option="shuffle"):
        print(word)