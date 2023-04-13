# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alvgomez <alvgomez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/22 12:15:02 by alvgomez          #+#    #+#              #
#    Updated: 2023/04/13 16:15:25 by alvgomez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from vector import Vector

if __name__ == "__main__":
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]]) 
    v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
    v3 = Vector([[0.0, 1.0, 2.0, 3.0]])
    v4 = Vector([[2.0, 1.5, 2.25, 4.0]])
    v5 = Vector((10,16))
    v6 = Vector(3)
    
    print(v5.values)
    print(v6.values)
    print((v1 + v2).values)
    print((v3 - v4).values)
    print((v1 * 5.0).values)
    print((3.0 * v2).values)
    print((v4 / 2.0).values)
    
    v7 = v1 / 0.0  
    v8 = 2.0 / v2