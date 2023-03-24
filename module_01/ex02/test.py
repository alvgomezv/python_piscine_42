# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alvgomez <alvgomez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/22 12:15:02 by alvgomez          #+#    #+#              #
#    Updated: 2023/03/24 12:23:27 by alvgomez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from vector import Vector

if __name__ == "__main__":
    check = 0
    try: 
        v1 = Vector([[0.0], [1.0], [2.0], [3.0]]) 
        v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
        v3 = Vector([[0.0, 1.0, 2.0, 3.0]])
        v4 = Vector([[2.0, 1.5, 2.25, 4.0]])
    except:
        print("1) Error creating vectors with lists")
        check += 1
    try:  
        v5 = Vector(10,16)
    except:
        print("2) Error creating vectors with tuples")
        check += 1
    try:  
        v6 = Vector(3)
    except:
        print("3) Error creating vectors with ints")
        check += 1
    
    if (v6).values != [[0.0], [1.0], [2.0]]:
        print("4) Error in creating vector with ints")
        check += 1
    if (v1 + 5.0).values != [[5.0], [6.0], [7.0], [8.0]]:
        print("4) Error in sum")
        check += 1
    if (v3 + 5.0).values == [[5.0, 6.0, 7.0, 8.0]]:
        print("2) great!")
    if (5.0 + v1).values == [[5.0], [6.0], [7.0], [8.0]]:
        print("3) great!")
    if (5.0 + v3).values == [[5.0, 6.0, 7.0, 8.0]]:
        print("4) great!")
    if (v1 - 5.0).values == [[-5.0], [-4.0], [-3.0], [-2.0]]:
        print("5) great!")
    if (v3 - 5.0).values == [[-5.0, -4.0, -3.0, -2.0]]:
        print("6) great!")
    if (5.0 - v1).values == "NotImplementedError: Subtraction of a scalar by a Vector is not defined here":
        print("7) great!")
    if (5.0 - v3).values == "NotImplementedError: Subtraction of a scalar by a Vector is not defined here":
        print("8) great!")
