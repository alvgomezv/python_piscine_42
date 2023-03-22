# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alvgomez <alvgomez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/22 12:15:02 by alvgomez          #+#    #+#              #
#    Updated: 2023/03/22 13:43:38 by alvgomez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from vector import Vector

if __name__ == "__main__":
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]]) 
    v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
    
    v3 = Vector([[0.0, 1.0, 2.0, 3.0]])
    v4 = Vector([[2.0, 1.5, 2.25, 4.0]])


    #if (v1 + 5.0).values == [[5.0], [6.0], [7.0], [8.0]]:
    #    print("1) great!")
    #if print(v3 + 5.0) == [[5.0, 6.0, 7.0, 8.0]]:
    #    print("2) great!")
    #if print(5.0 + v1) == [[5.0], [6.0], [7.0], [8.0]]:
    #    print("3) great!")
    #if print(5.0 + v3) == [[5.0, 6.0, 7.0, 8.0]]:
    #    print("4) great!")
    #if print(v1 - 5.0) == [[-5.0], [-4.0], [-3.0], [-2.0]]:
    #    print("5) great!")
    #if print(v3 - 5.0) == [[-5.0, -4.0, -3.0, -2.0]]:
    #    print("6) great!")
    #if print(5.0 - v1) == "NotImplementedError: Subtraction of a scalar by a Vector is not defined here":
    #    print("7) great!")
    #if print(5.0 - v3) == "NotImplementedError: Subtraction of a scalar by a Vector is not defined here":
    #    print("8) great!")
